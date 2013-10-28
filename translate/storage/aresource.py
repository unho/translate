#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Michal Čihař
# Copyright 2013 Zuza Software Foundation
#
# This file is part of the Translate Toolkit.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

"""Module for handling Android String resource files."""

import re

from lxml import etree

from translate.lang.data import forceunicode
from translate.misc.xml_helpers import namespaced
from translate.storage import base


EOF = None
WHITESPACE = ' \n\t'  # Whitespace that we collapse.
MULTIWHITESPACE = re.compile('[ \n\t]{2}')




def unescape_android(text):
    '''Remove escaping from Android resource.

    Code stolen from android2po
    <https://github.com/miracle2k/android2po>
    '''
    # We need to collapse multiple whitespace while paying attention to
    # Android's quoting and escaping.
    space_count = 0
    active_quote = False
    active_percent = False
    active_escape = False
    formatted = False
    i = 0
    text = list(text) + [EOF]
    while i < len(text):
        c = text[i]

        # Handle whitespace collapsing.
        if c is not EOF and c in WHITESPACE:
            space_count += 1
        elif space_count > 1:
            # Remove duplicate whitespace; Pay attention: We don't do this if
            # we are currently inside a quote, except for one special case: If
            # we have unbalanced quotes, e.g. we reach eof while a quote is
            # still open, we *do* collapse that trailing part; this is how
            # Android does it, for some reason.
            if not active_quote or c is EOF:
                # Replace by a single space, will get rid of non-significant
                # newlines/tabs etc.
                text[i-space_count : i] = ' '
                i -= space_count - 1
            space_count = 0
        elif space_count == 1:
            # At this point we have a single whitespace character, but it might
            # be a newline or tab. If we write this kind of insignificant
            # whitespace into the .po file, it will be considered significant
            # on import. So, make sure that this kind of whitespace is always a
            # standard space.
            text[i-1] = ' '
            space_count = 0
        else:
            space_count = 0

        # Handle quotes.
        if c == '"' and not active_escape:
            active_quote = not active_quote
            del text[i]
            i -= 1

        # If the string is run through a formatter, it will have percentage
        # signs for String.format.
        if c == '%' and not active_escape:
            active_percent = not active_percent
        elif not active_escape and active_percent:
            formatted = True
            active_percent = False

        # Handle escapes.
        if c == '\\':
            if not active_escape:
                active_escape = True
            else:
                # A double-backslash represents a single; simply deleting the
                # current char will do.
                del text[i]
                i -= 1
                active_escape = False
        else:
            if active_escape:
                # Handle the limited amount of escape codes that we support.
                # TODO: What about \r, or \r\n?
                if c is EOF:
                    # Basically like any other char, but put this first so we
                    # can use the ``in`` operator in the clauses below without
                    # issue.
                    pass
                elif c == 'n' or c == 'N':
                    text[i-1 : i+1] = '\n' # an actual newline
                    i -= 1
                elif c == 't' or c == 'T':
                    text[i-1 : i+1] = '\t' # an actual tab
                    i -= 1
                elif c == ' ':
                    text[i-1 : i+1] = ' ' # an actual space
                    i -= 1
                elif c in '"\'@':
                    text[i-1 : i] = '' # remove the backslash
                    i -= 1
                elif c == 'u':
                    # Unicode sequence. Android is nice enough to deal with
                    # those in a way which let's us just capture the next 4
                    # characters and raise an error if they are not valid
                    # (rather than having to use a new state to parse the
                    # unicode sequence). Exception: In case we are at the end
                    # of the string, we support incomplete sequences by
                    # prefixing the missing digits with zeros. Note: max(len())
                    # is needed in the slice due to trailing ``None`` element.
                    max_slice = min(i+5, len(text)-1)
                    codepoint_str = "".join(text[i+1 : max_slice])
                    if len(codepoint_str) < 4:
                        codepoint_str = (u"0" * (4-len(codepoint_str)) +
                                         codepoint_str)
                    try:
                        # We can't trust int() to raise a ValueError, it will
                        # ignore leading/trailing whitespace.
                        if not codepoint_str.isalnum():
                            raise ValueError(codepoint_str)
                        codepoint = unichr(int(codepoint_str, 16))
                    except ValueError:
                        raise ValueError('bad unicode escape sequence')

                    text[i-1 : max_slice] = codepoint
                    i -= 1
                else:
                    # All others, remove, like Android does as well.
                    text[i-1 : i+1] = ''
                    i -= 1
                active_escape = False

        i += 1

    # Join the string together again, but w/o EOF marker
    return "".join(text[:-1])


def escape_android(text):
    '''
    Escape all the characters which need to be escaped in an Android XML file.
    '''
    if text is None or len(text) == 0:
        return ''

    text = text.replace('\\', '\\\\')
    text = text.replace('\n', '\\n')

    # This will add non intrusive real newlines to ones in translation
    # improving readability of result.
    text = text.replace(' \\n', '\n\\n')
    text = text.replace('\t', '\\t')
    text = text.replace('\'', '\\\'')
    text = text.replace('"', '\\"')

    # @ needs to be escaped at start.
    if text.startswith('@'):
        text = '\\@' + text[1:]

    # Quote strings with more whitespace.
    if (text[0] in WHITESPACE or text[-1] in WHITESPACE or
            len(MULTIWHITESPACE.findall(text)) > 0):
        return '"%s"' % text

    return text









class AndroidResourceUnit(base.TranslationUnit):
    """A single entry in the Android String resource file."""
    # The name of the root element of this unit type.
    rootNode = "string"
    # The name of the per language element of this unit type.
    languageNode = "string"

    @classmethod
    def createfromxmlElement(cls, xmlelement):
        """Create a new unit from a XML element."""
        # The next line just extracts the source up to the first nested tag
        # (usually a markup tag). If the string is 'Hello <b>again</b> world',
        # it only gets the 'Hello ' part.
        source = unescape_android(xmlelement.text or u'')#TODO check the unescape code.

        # Include markup and trailing text in the source as well. Using the
        # above example, it extracts the '<b>again</b> world' part.
        tails = [forceunicode(etree.tostring(child, encoding='utf-8')) for
                 child in xmlelement.iterchildren()]


        #TODO if tails then it is necessary to save that there are tags on the
        # source, and it is necessary to save them on some way. Remember to
        # convert them back to elements when outputting.


        source += u''.join(tails)

        #print("TEXT is: %s\nID: %s\n" % (xmlelement.text, xmlelement.get("name")))#TODO borrar

        istranslatable = xmlelement.get('translatable') != 'false'
        new_unit = cls(source, xmlelement.get("name"), istranslatable)
        return new_unit

    def __init__(self, source=None, name=None, istranslatable=True, **kwargs):
        super(AndroidResourceUnit, self).__init__(source)
        self.setid(name)
        self._is_translatable = istranslatable
        self._comments = []

    def __str__(self):
        return etree.tostring(self.get_string_node(), pretty_print=True,
                              encoding='utf-8')

    def __eq__(self, other):
        return (str(self) == str(other))

    def get_string_node(self):
        """Convert the unit to one 'string' etree nodes."""
        # Now create the 'string' node.
        node = etree.Element(self.rootNode)
        node.text = escape_android(self.source)

        if self.getid():
            node.set("name", self.getid())

        if not self.istranslatable():
            node.set("translatable", "false")

        return node

    def get_xml_nodes(self, with_notes=True):
        """Convert the unit to one or several etree nodes.

        The nodes hold the unit's Android String Resource representation.

        Only when comments are present more than one node is returned.
        """
        output_nodes = []

        for note in self._comments:
            # Notes are handled as previous sibling comments.
            output_nodes.append(etree.Comment(note))

        output_nodes.append(self.get_string_node())

        return output_nodes

    def getnotes(self, origin=None):
        """Returns all notes about this unit.

        It will probably be freeform text or something reasonable that can be
        synthesised by the format.
        It should not include location comments (see
        :meth:`~.TranslationUnit.getlocations`).
        """
        return "\n".join(self._comments)

    def addnote(self, text, origin=None, position="append"):
        """Adds a note (comment).

        :type text: string
        :param text: Usually just a sentence or two.
        :type origin: string
        :param origin: Specifies who/where the comment comes from.
                       Origin can be one of the following text strings:
                       - 'translator'
                       - 'developer', 'programmer', 'source code' (synonyms)
        """
        if position == "append":
            self._comments.append(text)
        else:
            self._comments = [text]

    def removenotes(self):
        """Remove all the translator's notes."""
        self._comments = []

    def istranslatable(self):
        return bool(self.getid()) and self._is_translatable

    def getid(self):
        return self._name

    def setid(self, newid):
        self._name = newid

    def getcontext(self):
        return self._name


class AndroidResourceFile(base.TranslationStore):
    """Class representing an Android String resource file store."""
    UnitClass = AndroidResourceUnit
    Name = _("Android String Resource")
    Mimetypes = ["application/xml"]
    Extensions = ["xml"]
    """The root node of the XML document"""
    rootNode = "resources"
    """The root node of the content section"""
    bodyNode = "resources"
    """The XML skeleton to use for empty construction"""
    XMLskeleton = '''<?xml version="1.0" encoding="utf-8"?>
<resources></resources>'''

    def __init__(self, inputfile=None, sourcelanguage='en',
                 targetlanguage=None, unitclass=None):
        super(AndroidResourceFile, self).__init__(unitclass)
        self.set_xml_parser()
        self.filename = getattr(inputfile, 'name', '')
        if inputfile is not None:
            self.parse(inputfile)
        else:
            # We strip out newlines to ensure that spaces in the skeleton don't
            # interfere with the the pretty printing of lxml.
            self.parse(self.XMLskeleton.replace("\n", ""))
            self.setsourcelanguage(sourcelanguage)
            self.settargetlanguage(targetlanguage)
        self._encoding = "UTF-8"

    def __str__(self):
        """Convert to a string containing the file's XML."""
        # Strip out the newlines to ensure that spaces in the skeleton don't
        # interfere with the the pretty printing of lxml.
        trimmed_skeleton = self.XMLskeleton.replace("\n", "")
        document = etree.fromstring(trimmed_skeleton, self.xml_parser)

        # Append the nodes for the units in the document.
        for unit in self.units:
            for node in unit.get_xml_nodes():
                document.append(node)

        return etree.tostring(document, pretty_print=True,
                              xml_declaration=True, encoding='utf-8')

    def set_xml_parser(self):
        """Set the XML parser to be used."""
        if etree.LXML_VERSION >= (2, 1, 0):
            # Since version 2.1.0 we can pass the strip_cdata parameter to
            # indicate that we don't want cdata to be converted to raw XML.
            self.xml_parser = etree.XMLParser(strip_cdata=False)
        else:
            self.xml_parser = etree.XMLParser()

    def initbody(self):
        """Initialise self.body so it never is retrieved from the XML again."""
        self.namespace = self.document.getroot().nsmap.get(None, None)
        self.body = self.document.getroot()

    def namespaced(self, name):
        """Return name in Clark notation.

        For example ``namespaced("source")`` in an XLIFF document might
        return::

            {urn:oasis:names:tc:xliff:document:1.1}source

        This is needed throughout lxml.
        """
        return namespaced(self.namespace, name)

    def parse(self, xml):
        """Populate this object from the given xml string or file."""
        if hasattr(xml, "read"):
            # If it is a file, and not a string, then read it.
            xml.seek(0)
            xml = xml.read()

        self.document = etree.fromstring(xml, self.xml_parser).getroottree()
        self._encoding = self.document.docinfo.encoding
        self.initbody()
        assert self.document.getroot().tag == self.namespaced(self.rootNode)

        new_comments = []

        for node in self.document.getroot().iterdescendants():
            if node.tag == self.UnitClass.rootNode:
                # If this is a 'string' node.
                new_unit = self.UnitClass.createfromxmlElement(node)

                for comment in new_comments:
                    new_unit.addnote(comment)

                self.addunit(new_unit)

                new_comments = []
            elif node.tag is etree.Comment:
                # If this is a comment get it to append it to the next unit.
                new_comments.append(node.text)
