# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 Zuza Software Foundation
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

"""Convert Comma-Separated Value (.csv) files to a TermBase eXchange (.tbx)
glossary file

See: http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/csv2tbx.html
for examples and usage instructions
"""

from translate.convert import convert
from translate.storage import csvl10n, tbx


class csv2tbx(object):
    """Convert a CSV file to a TBX file."""

    SourceStoreClass = csvl10n.csvfile
    TargetStoreClass = tbx.tbxfile
    TargetUnitClass = tbx.tbxunit

    def __init__(self, input_file, output_file, charset=None,
                 column_order=None):
        """Initialize the converter."""
        self.charset = charset
        self.column_order = column_order

        self.output_file = output_file
        self.source_store = self.SourceStoreClass(input_file,
                                                 fieldnames=column_order)
        self.target_store = self.TargetStoreClass()

    def convert_store(self):
        """Convert a single source format file to a target format file."""
        mightbeheader = True
        for source_unit in self.source_store.units:
            if mightbeheader:
                # ignore typical header strings...
                mightbeheader = False
                if source_unit.match_header():
                    continue
                if (len(source_unit.location.strip()) == 0 and
                    source_unit.source.find("Content-Type:") != -1):
                    continue
            target_unit = self.TargetUnitClass.buildfromunit(source_unit)
            # TODO: we might want to get the location or other information
            # from CSV
            self.target_store.addunit(target_unit)

    def run(self):
        """Run the converter."""
        self.convert_store()

        if self.target_store.isempty():
            return 0

        self.target_store.serialize(self.output_file)
        return 1


def run_converter(inputfile, outputfile, templatefile, charset=None,
                  columnorder=None):
    """Wrapper around converter."""
    return csv2tbx(inputfile, outputfile, charset=charset,
                   column_order=columnorder).run()


formats = {
    ("csv", "tbx"): ("tbx", run_converter),
    ("csv", None): ("tbx", run_converter),
}


def main():
    parser = convert.ConvertOptionParser(formats, usetemplates=False,
                                         description=__doc__)
    parser.add_option(
        "", "--charset", dest="charset", default=None,
        help="set charset to decode from csv files", metavar="CHARSET")
    parser.add_option(
        "", "--columnorder", dest="columnorder", default=None,
        help="specify the order and position of columns (comment,source,target)")
    parser.passthrough.append("charset")
    parser.passthrough.append("columnorder")
    parser.run()


if __name__ == '__main__':
    main()
