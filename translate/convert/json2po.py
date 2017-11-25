# -*- coding: utf-8 -*-
#
# Copyright 2007, 2010 Zuza Software Foundation
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

"""Convert JSON files to Gettext PO localization files.

See: http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/json2po.html
for examples and usage instructions.
"""

import logging

from translate.convert import convert
from translate.storage import jsonl10n, po


logger = logging.getLogger(__name__)


class json2po(object):
    """Convert one or two JSON files to a single PO file."""

    SourceStoreClass = jsonl10n.JsonFile
    TargetStoreClass = po.pofile
    TargetUnitClass = po.pounit

    def __init__(self, input_file, output_file, template_file=None,
                 blank_msgstr=False, duplicate_style="msgctxt",
                 dialect="default", filter=None):
        """Initialize the converter."""
        self.blank_msgstr = blank_msgstr
        self.duplicate_style = duplicate_style

        if filter is not None:
            filter = filter.split(',')

        self.output_file = output_file
        self.source_store = self.SourceStoreClass(input_file, filter=filter)
        self.target_store = self.TargetStoreClass()
        self.template_store = None

        if template_file is not None:
            self.template_store = self.SourceStoreClass(template_file)

        self.source_store.makeindex()

        self.extraction_msg = None

    def convert_unit(self, unit):
        """Convert a source format unit to a target format unit."""
        if unit is None:
            return None

        target_unit = self.TargetUnitClass(encoding="UTF-8")
        target_unit.addlocation(unit.getid())
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

            # Try and find a translation of the same name...
            template_unit_name = "".join(template_unit.getlocations())
            translatedpo = None
            if template_unit_name in self.source_store.locationindex:
                translatedjson = self.source_store.locationindex[template_unit_name]
                translatedpo = self.convert_unit(translatedjson)

            # If we have a valid po unit, get the translation and add it...
            if target_unit is not None:
                if translatedpo is not None and not self.blank_msgstr:
                    target_unit.target = translatedpo.source
                self.target_store.addunit(target_unit)
            elif translatedpo is not None:
                logger.error("error converting original JSON definition %s",
                             target_unit.name)

    def run(self):
        """Run the converter."""
        if self.template_store is None:
            self.convert_store()
        else:
            self.merge_stores()

        if self.extraction_msg:
            self.target_store.header().addnote(self.extraction_msg,
                                               "developer")

        self.target_store.removeduplicates(self.duplicate_style)

        if self.target_store.isempty():
            return 0

        self.target_store.serialize(self.output_file)
        return 1


def run_converter(input_file, output_file, template_file, pot=False,
                  duplicatestyle="msgctxt", dialect="default", filter=None):
    """Wrapper around converter."""
    return json2po(input_file, output_file, template_file, blank_msgstr=pot,
                   duplicate_style=duplicatestyle, dialect=dialect,
                   filter=filter).run()


formats = {
    "json": ("po", run_converter),
    ("json", "json"): ("po", run_converter),
}


def main(argv=None):
    parser = convert.ConvertOptionParser(formats, usetemplates=True,
                                         usepots=True, description=__doc__)
    parser.add_option(
        "", "--filter", dest="filter", default=None,
        help="leaves to extract e.g. 'name,desc': (default: extract everything)",
        metavar="FILTER")
    parser.add_duplicates_option()
    parser.passthrough.append("pot")
    parser.passthrough.append("filter")
    parser.run(argv)


if __name__ == '__main__':
    main()
