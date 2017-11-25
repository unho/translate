# -*- coding: utf-8 -*-
#
# Copyright 2016 Zuza Software Foundation
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

"""Convert Mozilla .l20n files to Gettext PO localization files.

See: http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/l20n2po.html
for examples and usage instructions.
"""

from translate.convert import convert
from translate.storage import l20n, po


class l20n2po(object):
    """Convert one or two l20n files to a single PO file."""

    SourceStoreClass = l20n.l20nfile
    TargetStoreClass = po.pofile
    TargetUnitClass = po.pounit

    def __init__(self, input_file, output_file, template_file=None,
                 blank_msgstr=False, duplicate_style="msgctxt"):
        """Initialize the converter."""
        self.blank_msgstr = blank_msgstr
        self.duplicate_style = duplicate_style

        self.output_file = output_file
        self.source_store = self.SourceStoreClass(input_file)
        self.target_store = self.TargetStoreClass()
        self.template_store = None

        if template_file is not None:
            self.template_store = self.SourceStoreClass(template_file)

        self.source_store.makeindex()

    def convert_unit(self, unit):
        """Convert a source format unit to a target format unit."""
        target_unit = self.TargetUnitClass(encoding="UTF-8")
        target_unit.setid(unit.getid())
        target_unit.addlocation(unit.getid())
        target_unit.source = unit.value
        target_unit.addnote(unit.comment, "developer")
        return target_unit

    def convert_store(self):
        """Convert a single source format file to a target format file."""
        for source_unit in self.source_store.units:
            target_unit = self.convert_unit(source_unit)
            self.target_store.addunit(target_unit)

    def merge_stores(self):
        """Convert two source format files to a target format file."""
        for template_unit in self.template_store.units:
            target_unit = self.convert_unit(template_unit)
            self.target_store.addunit(target_unit)

            for location in target_unit.getlocations():
                if location in self.source_store.id_index:
                    source_unit = self.source_store.id_index[location]
                    target_unit.target = source_unit.target

    def run(self):
        """Run the converter."""
        if self.template_store is None:
            self.convert_store()
        else:
            self.merge_stores()

        self.target_store.removeduplicates(self.duplicate_style)

        if self.target_store.isempty():
            return 0

        self.target_store.serialize(self.output_file)
        return 1


def run_converter(inputfile, outputfile, templatefile, pot=False,
                  duplicatestyle="msgctxt"):
    """Wrapper around converter."""
    return l20n2po(inputfile, outputfile, templatefile, blank_msgstr=pot,
                   duplicate_style=duplicatestyle).run()


formats = {
    "ftl": ("po", run_converter),
    ("ftl", "ftl"): ("po", run_converter),
    "l20n": ("po", run_converter),
    ("l20n", "l20n"): ("po", run_converter),
}


def main(argv=None):
    parser = convert.ConvertOptionParser(formats, usetemplates=True,
                                         usepots=True, description=__doc__)
    parser.add_duplicates_option()
    parser.passthrough.append("pot")
    parser.run(argv)


if __name__ == '__main__':
    main()
