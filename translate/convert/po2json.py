# -*- coding: utf-8 -*-
#
# Copyright 2002-2006 Zuza Software Foundation
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

"""Convert Gettext PO localization files to JSON files.

See: http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/json2po.html
for examples and usage instructions.
"""

from translate.convert import convert
from translate.storage import jsonl10n, po


class po2json(object):
    """Convert a PO file and a template JSON file to a JSON file."""

    SourceStoreClass = po.pofile
    TargetStoreClass = jsonl10n.JsonFile
    TargetUnitClass = jsonl10n.JsonUnit
    MissingTemplateMessage = "A template JSON file must be provided."

    def __init__(self, input_file, output_file, template_file=None,
                 include_fuzzy=False, output_threshold=None,
                 remove_untranslated=False):
        """Initialize the converter."""

        if template_file is None:
            raise ValueError(self.MissingTemplateMessage)

        self.source_store = self.SourceStoreClass(input_file)

        self.should_output_store = convert.should_output_store(
            self.source_store, output_threshold
        )
        if self.should_output_store:
            self.include_fuzzy = include_fuzzy
            self.output_threshold = output_threshold
            self.remove_untranslated = remove_untranslated

            self.output_file = output_file
            self.template_store = self.TargetStoreClass(template_file)
            self.target_store = self.TargetStoreClass()

            self.source_store.makeindex()

    def convert_unit(self, unit):
        """Convert a source format unit to a target format unit."""
        use_target = (unit.istranslated()
                      or (unit.isfuzzy() and self.include_fuzzy))
        target_unit = self.TargetUnitClass(
            source=unit.target if use_target else unit.source,
        )
        target_unit.setid(unit.getlocations()[0])
        target_unit.addnote(unit.getnotes("developer"), "developer")
        return target_unit

    def convert_store(self):
        """Convert a source file to a target file using a template file.

        Source file is in source format, while target and template files use
        target format.
        """
        for unit in self.template_store.units:
            template_unit_id = template_unit.getid()

            #do_unit = (not self.remove_untranslated
            #           or (template_unit_id in self.source_store.locationindex
            #               and not input_unit.isfuzzy()
            #               and input_unit.istranslated()
            #              )
            #          )



            if do_unit:
                input_unit = self.source_store.locationindex[template_unit_id]



                #skip_unit = (self.remove_untranslated and
                #             (inputUNI is None or inputUNI.isfuzzy() or not inputUNI.istranslated()))
                if not skip_unit:
                    self.target_store.addunit(self.convert_unit(input_unit))

    def run(self):
        """Run the converter."""
        if not self.should_output_store:
            return 0

        self.convert_store()
        self.target_store.serialize(self.output_file)
        return 1


def run_converter(inputfile, outputfile, templatefile, includefuzzy=False,
                  outputthreshold=None, remove_untranslated=False):
    return po2json(inputfile, outputfile, templatefile, includefuzzy,
                   outputthreshold, remove_untranslated).run()


formats = {
    ("po", "json"): ("json", run_converter),
}


def main(argv=None):
    parser = convert.ConvertOptionParser(formats, usetemplates=True,
                                         description=__doc__)
    parser.add_threshold_option()
    parser.add_fuzzy_option()
    parser.add_remove_untranslated_option()
    parser.run(argv)


if __name__ == '__main__':
    main()
