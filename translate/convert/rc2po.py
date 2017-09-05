# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 Zuza Software Foundation
#
# This file is part of translate.
#
# translate is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# translate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

"""Convert Windows RC files to Gettext PO localization files.

See: http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/rc2po.html
for examples and usage instructions.
"""

import logging

from translate.convert import convert
from translate.storage import po, rc


logger = logging.getLogger(__name__)


class rc2po(object):
    """Convert one or two Windows RC files to a single PO file."""

    SourceStoreClass = rc.rcfile
    TargetStoreClass = po.pofile
    TargetUnitClass = po.pounit

    def __init__(self, input_file, output_file, template_file=None,
                 blank_msgstr=False, duplicate_style="msgctxt", encoding=None,
                 lang=None, sublang=None):
        """Initialize the converter."""
        self.blank_msgstr = blank_msgstr
        self.duplicate_style = duplicate_style

        self.output_file = output_file
        self.source_store = self.SourceStoreClass(input_file, lang, sublang,
                                                  encoding=encoding)
        self.target_store = self.TargetStoreClass()
        self.template_store = None

        if template_file is not None:
            self.template_store = self.SourceStoreClass(template_file, lang,
                                                        sublang,
                                                        encoding=encoding)

        self.source_store.makeindex()

        self.extraction_msg = None

    def convert_unit(self, unit):
        """Convert a source format unit to a target format unit."""
        if unit is None:
            return None  # Returns None if empty or not for translation.
        # escape unicode
        target_unit = self.TargetUnitClass(encoding="UTF-8")
        target_unit.addlocation("".join(unit.getlocations()))
        target_unit.source = unit.source
        target_unit.target = ""
        return target_unit

    def convert_store(self):
        """Convert a single source format file to a target format file."""
        self.extraction_msg = "extracted from %s" % self.source_store.filename

        for source_unit in self.source_store.units:
            if source_unit is None:
                continue
            target_unit = self.convert_unit(source_unit)
            self.target_store.addunit(target_unit)

    def merge_stores(self):
        """Convert two source format files to a target format file."""
        self.extraction_msg = ("extracted from %s, %s" %
                               (self.template_store.filename,
                                self.source_store.filename))

        for template_unit in self.template_store.units:
            target_unit = self.convert_unit(template_unit)
            # try and find a translation of the same name...
            template_unit_name = "".join(template_unit.getlocations())
            if template_unit_name in self.source_store.locationindex:
                translatedrc = self.source_store.locationindex[template_unit_name]
                translatedpo = self.convert_unit(translatedrc)
            else:
                translatedpo = None
            # if we have a valid po unit, get the translation and add it...
            if target_unit is not None:
                if translatedpo is not None and not self.blank_msgstr:
                    target_unit.target = translatedpo.source
                self.target_store.addunit(target_unit)
            elif translatedpo is not None:
                logging.error("error converting original rc definition %s",
                              template_unit.name)

    def run(self):
        """Run the converter."""
        if self.template_store is None:
            self.convert_store()
        else:
            self.merge_stores()

        if self.extraction_msg:
            output_header = self.target_store.init_headers(
                x_accelerator_marker="&",
                x_merge_on="location",
            )
            output_header.addnote(self.extraction_msg, "developer")

        self.target_store.removeduplicates(self.duplicate_style)

        if self.target_store.isempty():
            return 0

        self.target_store.serialize(self.output_file)
        return 1


def run_converter(input_file, output_file, template_file, pot=False,
                  duplicatestyle="msgctxt", charset=None, lang=None,
                  sublang=None):
    """Wrapper around converter."""
    return rc2po(input_file, output_file, template_file, blank_msgstr=pot,
                 duplicate_style=duplicatestyle, encoding=charset, lang=lang,
                 sublang=sublang).run()


formats = {
    "rc": ("po", run_converter),
    ("rc", "rc"): ("po", run_converter),
    "nls": ("po", run_converter),
    ("nls", "nls"): ("po", run_converter),
}


def main(argv=None):
    parser = convert.ConvertOptionParser(formats, usetemplates=True,
                                         usepots=True, description=__doc__)
    DEFAULTCHARSET = "cp1252"
    parser.add_option(
        "", "--charset", dest="charset", default=DEFAULTCHARSET,
        help="charset to use to decode the RC files (default: %s)" % DEFAULTCHARSET, metavar="CHARSET")
    DEFAULTLANG = "LANG_ENGLISH"
    parser.add_option(
        "-l", "--lang", dest="lang", default=DEFAULTLANG,
        help="LANG entry (default: %s)" % DEFAULTLANG, metavar="LANG")
    DEFAULTSUBLANG = "SUBLANG_DEFAULT"
    parser.add_option(
        "", "--sublang", dest="sublang", default=DEFAULTSUBLANG,
        help="SUBLANG entry (default: %s)" % DEFAULTSUBLANG, metavar="SUBLANG")
    parser.add_duplicates_option()
    parser.passthrough.append("pot")
    parser.passthrough.append("charset")
    parser.passthrough.append("lang")
    parser.passthrough.append("sublang")
    parser.run(argv)


if __name__ == '__main__':
    main()
