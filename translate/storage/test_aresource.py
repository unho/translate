#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

from translate.storage import aresource, test_monolingual


class TestAndroidResourceUnit(test_monolingual.TestMonolingualUnit):
    UnitClass = aresource.AndroidResourceUnit

    def __check_escape(self, string, xml):
        """Helper that checks that a string is output with the right escape."""
        unit = self.UnitClass(string, "Test String")

        print("unit.source:", repr(unit.source))
        print("xml:", repr(xml))

        assert str(unit) == xml

    def __check_parse(self, string, xml):
        """Helper that checks that a string is parsed correctly."""
        if etree.LXML_VERSION >= (2, 1, 0):
            # Since version 2.1.0 we can pass the strip_cdata parameter to
            # indicate that we don't want cdata to be converted to raw XML.
            parser = etree.XMLParser(strip_cdata=False)
        else:
            parser = etree.XMLParser()

        translatable = 'translatable="false"' not in xml
        et = etree.fromstring(xml, parser)
        unit = self.UnitClass.createfromxmlElement(et)

        print("unit.source:", repr(unit.source))
        print("string:", string)
        print("translatable:", repr(unit.istranslatable()))

        assert unit.source == string
        assert unit.istranslatable() == translatable

    ############################ Check string escape ##########################

    def test_escape_message_with_newline(self):
        string = 'message\nwith newline'
        xml = '<string name="Test String">message\\nwith newline</string>\n'
        self.__check_escape(string, xml)

    def test_escape_message_with_newline_in_xml(self):
        string = 'message \nwith newline in xml'
        xml = ('<string name="Test String">message\n\\nwith newline in xml'
               '</string>\n')
        self.__check_escape(string, xml)

    def test_escape_twitter(self):
        string = '@twitterescape'
        xml = '<string name="Test String">\\@twitterescape</string>\n'
        self.__check_escape(string, xml)

    def test_escape_quote(self):
        string = 'quote \'escape\''
        xml = '<string name="Test String">quote \\\'escape\\\'</string>\n'
        self.__check_escape(string, xml)

    def test_escape_double_space(self):
        string = 'double  space'
        xml = '<string name="Test String">"double  space"</string>\n'
        self.__check_escape(string, xml)

    def test_escape_leading_space(self):
        string = ' leading space'
        xml = '<string name="Test String">" leading space"</string>\n'
        self.__check_escape(string, xml)

    def test_escape_xml_entities(self):
        string = '>xml&entities'
        xml = '<string name="Test String">&gt;xml&amp;entities</string>\n'
        self.__check_escape(string, xml)

    def test_escape_html_code(self):
        string = 'some <b>html code</b> here'
        xml = ('<string name="Test String">some <b>html code</b> here'
               '</string>\n')
        self.__check_escape(string, xml)

    def test_escape_arrows(self):
        string = '<<< arrow'
        xml = '<string name="Test String">&lt;&lt;&lt; arrow</string>\n'
        self.__check_escape(string, xml)

    def test_escape_link(self):
        string = '<a href="http://example.net">link</a>'
        xml = ('<string name="Test String"><a href="http://example.net">link'
               '</a></string>\n')
        self.__check_escape(string, xml)

    def test_escape_link_and_text(self):
        string = '<a href="http://example.net">link</a> and text'
        xml = ('<string name="Test String"><a href="http://example.net">link'
               '</a> and text</string>\n')
        self.__check_escape(string, xml)

    def test_escape_blank_string(self):
        string = ''
        xml = '<string name="Test String"></string>\n'
        self.__check_escape(string, xml)

    ############################ Check string parse ###########################

    def test_parse_message_with_newline(self):
        string = 'message\nwith newline'
        xml = '<string name="Test String">message\\nwith newline</string>\n'
        self.__check_parse(string, xml)

    def test_parse_message_with_newline_in_xml(self):
        string = 'message \nwith newline in xml'
        xml = ('<string name="Test String">message\n\\nwith newline in xml'
               '</string>\n')
        self.__check_parse(string, xml)

    def test_parse_twitter(self):
        string = '@twitterescape'
        xml = '<string name="Test String">\\@twitterescape</string>\n'
        self.__check_parse(string, xml)

    def test_parse_quote(self):
        string = 'quote \'escape\''
        xml = '<string name="Test String">quote \\\'escape\\\'</string>\n'
        self.__check_parse(string, xml)

    def test_parse_double_space(self):
        string = 'double  space'
        xml = '<string name="Test String">"double  space"</string>\n'
        self.__check_parse(string, xml)

    def test_parse_leading_space(self):
        string = ' leading space'
        xml = '<string name="Test String">" leading space"</string>\n'
        self.__check_parse(string, xml)

    def test_parse_xml_entities(self):
        string = '>xml&entities'
        xml = '<string name="Test String">&gt;xml&amp;entities</string>\n'
        self.__check_parse(string, xml)

    def test_parse_html_code(self):
        string = 'some <b>html code</b> here'
        xml = ('<string name="Test String">some <b>html code</b> here'
               '</string>\n')
        self.__check_parse(string, xml)

    def test_parse_arrows(self):
        string = '<<< arrow'
        xml = '<string name="Test String">&lt;&lt;&lt; arrow</string>\n'
        self.__check_parse(string, xml)

    def test_parse_link(self):
        string = '<a href="http://example.net">link</a>'
        xml = ('<string name="Test String"><a href="http://example.net">link'
               '</a></string>\n')
        self.__check_parse(string, xml)

    def test_parse_link_and_text(self):
        string = '<a href="http://example.net">link</a> and text'
        xml = ('<string name="Test String"><a href="http://example.net">link'
               '</a> and text</string>\n')
        self.__check_parse(string, xml)

    def test_parse_blank_string(self):
        string = ''
        xml = '<string name="Test String"></string>\n'
        self.__check_parse(string, xml)

    def test_parse_blank_string_again(self):
        string = ''
        xml = '<string name="Test String"/>\n'
        self.__check_parse(string, xml)

    def test_parse_double_quotes_string(self):
        """Check that double quotes got removed."""
        string = 'double quoted text'
        xml = '<string name="Test String">"double quoted text"</string>\n'
        self.__check_parse(string, xml)

    def test_parse_newline_in_string(self):
        """Check that newline is read as space.

        At least it seems to be what Android does.
        """
        string = 'newline in string'
        xml = '<string name="Test String">newline\nin string</string>\n'
        self.__check_parse(string, xml)

    def test_parse_not_translatable_string(self):
        string = 'string'
        xml = ('<string name="Test String" translatable="false">string'
               '</string>\n')
        self.__check_parse(string, xml)


class TestAndroidResourceFile(test_monolingual.TestMonolingualStore):
    StoreClass = aresource.AndroidResourceFile
