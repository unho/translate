# -*- coding: utf-8 -*-
#
# Copyright 2004-2006 Zuza Software Foundation
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

"""Convert HTML files to Gettext PO localization files.

See: http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/html2po.html
for examples and usage instructions.
"""

from translate.convert import convert
from translate.storage import html, po


class ConverterCantMergeError(Exception):
    pass


class html2po(object):
    SourceStoreClass = html.htmlfile
    TargetStoreClass = po.pofile
    TargetUnitClass = po.pounit

    def __init__(self, input_file, output_file, template_file=None,
                 blank_msgstr=False, duplicate_style="msgctxt",
                 include_untagged=False, keep_comments=False):
        """Initialize the converter."""
        self.blank_msgstr = blank_msgstr
        self.duplicate_style = duplicate_style
        self.keep_comments = keep_comments

        self.output_file = output_file
        self.source_store = self.SourceStoreClass(
            includeuntaggeddata=include_untagged,
            inputfile=input_file)
        self.target_store = self.TargetStoreClass()
        self.template_store = None

        if template_file is not None:
            self.template_store = self.SourceStoreClass(template_file)

    def convert_unit(self, unit):
        """Convert a source format unit to a target format unit."""
        target_unit = self.TargetUnitClass(encoding="UTF-8")
        target_unit.addlocations(unit.getlocations())
        target_unit.source = unit.source
        if self.keep_comments:
            target_unit.addnote(unit.getnotes(), "developer")
        return target_unit

    def convert_store(self):
        """Convert a single source format file to a target format file."""
        for source_unit in self.source_store.units:
            target_unit = self.convert_unit(source_unit)
            self.target_store.addunit(target_unit)

    def merge_stores(self):
        """Convert two source format files to a target format file."""
        raise ConverterCantMergeError

    def run(self):
        """Run the converter."""
        if self.template_store is None:
            self.convert_store()
        else:
            self.merge_stores()

        self.target_store.removeduplicates(self.duplicate_style)

        self.target_store.serialize(self.output_file)
        return 1


def run_converter(inputfile, outputfile, templates, includeuntagged=False,
                  pot=False, duplicatestyle="msgctxt", keepcomments=False):
    """Wrapper around converter."""
    return html2po(inputfile, outputfile, templates, blank_msgstr=pot,
                   duplicate_style=duplicatestyle,
                   include_untagged=includeuntagged,
                   keep_comments=keepcomments).run()


formats = {
    "html": ("po", run_converter),
    "htm": ("po", run_converter),
    "xhtml": ("po", run_converter),
    None: ("po", run_converter),
}


def main(argv=None):
    parser = convert.ConvertOptionParser(formats, usepots=True,
                                         description=__doc__)
    parser.add_option("-u", "--untagged", dest="includeuntagged",
                      default=False, action="store_true",
                      help="include untagged sections")
    parser.passthrough.append("includeuntagged")
    parser.add_option("--keepcomments", dest="keepcomments", default=False,
                      action="store_true",
                      help=("preserve html comments as translation notes in "
                            "the output"))
    parser.passthrough.append("keepcomments")
    parser.add_duplicates_option()
    parser.passthrough.append("pot")
    parser.run(argv)


if __name__ == '__main__':
    main()
