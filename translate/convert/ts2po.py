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

"""Convert Qt Linguist (.ts) files to Gettext PO localization files.

See: http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/ts2po.html
for examples and usage instructions.
"""

from translate.convert import convert
from translate.storage import po, ts


class ConverterCantMergeError(Exception):
    pass


class ts2po(object):
    """Convert one or two Qt Linguist (.ts) files to a single PO file."""

    SourceStoreClass = ts.QtTsParser
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

    def convert_unit(self, contextname, messagenum, message):
        """Convert a source format unit to a target format unit."""
        source = self.source_store.getmessagesource(message)
        target = self.source_store.getmessagetranslation(message)
        msgcomments = self.source_store.getmessagecomment(message)
        transtype = self.source_store.getmessagetype(message)
        target_unit = self.TargetUnitClass(encoding="UTF-8")
        target_unit.addlocation("%s#%d" % (contextname, messagenum))
        target_unit.source = source
        if not self.blank_msgstr:
            target_unit.target = target
        if len(msgcomments) > 0:
            target_unit.addnote(msgcomments)
        if transtype == "unfinished" and target_unit.istranslated():
            target_unit.markfuzzy()
        if transtype == "obsolete":
            # This should use the Gettext obsolete method but it would require quite a bit of work
            target_unit.addnote("(obsolete)", origin="developer")
            # using the fact that -- quote -- "(this is nonsense)"
        return target_unit

    def convert_store(self):
        """Convert a single source format file to a target format file."""
        for contextname, messages in self.source_store.iteritems():
            messagenum = 0
            for message in messages:
                messagenum += 1
                target_unit = self.convert_unit(contextname, messagenum,
                                                message)
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

        if self.target_store.isempty():
            return 0

        self.target_store.serialize(self.output_file)
        return 1


def run_converter(inputfile, outputfile, templates, pot=False,
                  duplicatestyle="msgctxt"):
    """Wrapper around converter."""
    return ts2po(inputfile, outputfile, templates, blank_msgstr=pot,
                 duplicate_style=duplicatestyle).run()


formats = {
    "ts": ("po", run_converter)
}


def main(argv=None):
    parser = convert.ConvertOptionParser(formats, usepots=True,
                                         description=__doc__)
    parser.add_duplicates_option()
    parser.passthrough.append("pot")
    parser.run(argv)


if __name__ == '__main__':
    main()
