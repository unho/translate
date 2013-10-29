#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Zuza Software Foundation
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

"""Convert Android String Resource localization files to Gettext PO
localization files.

See: http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/and2po.html
for examples and usage instructions.
"""

import sys
import logging

from translate.convert import convert
from translate.storage import aresource, po


logger = logging.getLogger(__name__)


class Android2po:
    """Convert a Android String Resource file to a .po file for handling the translation."""

    def convertstore(self, inputstore, duplicatestyle="msgctxt"):
        """Convert a Android String Resource file to a .po file."""
        outputstore = po.pofile()
        outputheader = outputstore.header()
        outputheader.addnote("extracted from %s" % inputstore.filename,
                             "developer")

        for inputunit in inputstore.units:
            outputunit = self.convertunit(inputunit, "developer")
            if outputunit is not None:
                outputstore.addunit(outputunit)
        outputstore.removeduplicates(duplicatestyle)
        return outputstore

    def mergestore(self, templatestore, inputstore, blankmsgstr=False,
                   duplicatestyle="msgctxt"):
        """Convert two Android String Resource files to a .po file."""
        outputstore = po.pofile()
        outputheader = outputstore.header()
        outputheader.addnote("extracted from %s, %s" % (templatestore.filename,
                                                        inputstore.filename),
                             "developer")

        inputstore.makeindex()
        # Loop through the original file, looking at units one by one.
        for templateunit in templatestore.units:
            outputunit = self.convertunit(templateunit, "developer")
            # Try and find a translation of the same name.
            if templateunit.name in inputstore.locationindex:
                translatedinputunit = inputstore.locationindex[templateunit.name]
                # Need to check that this comment is not a copy of the
                # developer comments.
                translatedoutputunit = self.convertunit(translatedinputunit,
                                                        "translator")
            else:
                translatedoutputunit = None
            # If we have a valid po unit, get the translation and add it.
            if outputunit is not None:
                if translatedoutputunit is not None and not blankmsgstr:
                    outputunit.target = translatedoutputunit.source
                outputstore.addunit(outputunit)
            elif translatedoutputunit is not None:
                logger("error converting original properties definition %s",#TODO
                       templateunit.name)
        outputstore.removeduplicates(duplicatestyle)
        return outputstore

    def convertunit(self, inputunit, origin):
        """Convert a Android String Resource unit to a .po unit."""
        outputunit = po.pounit(encoding="UTF-8")
        outputunit.addnote(inputunit.getnotes(origin), origin)
        outputunit.addlocation("".join(inputunit.getlocations()))
        outputunit.source = inputunit.source
        outputunit.target = ""
        return outputunit


def convertandroid(inputfile, outputfile, templatefile, pot=False,
               duplicatestyle="msgctxt"):
    """Read inputfile using aresource, convert using Android2po, write to
    outputfile.
    """
    inputstore = aresource.AndroidResourceFile(inputfile)
    convertor = Android2po()
    if templatefile is None:
        outputstore = convertor.convertstore(inputstore,
                                             duplicatestyle=duplicatestyle)
    else:
        templatestore = aresource.AndroidResourceFile(templatefile)
        outputstore = convertor.mergestore(templatestore, inputstore,
                                           blankmsgstr=pot,
                                           duplicatestyle=duplicatestyle)
    if outputstore.isempty():
        return 0
    outputfile.write(str(outputstore))
    return 1


def main(argv=None):
    formats = {
            "xml": ("po", convertandroid),
            ("xml", "xml"): ("po", convertandroid),
    }
    parser = convert.ConvertOptionParser(formats, usetemplates=True,
                                         usepots=True, description=__doc__)
    parser.add_duplicates_option()
    parser.passthrough.append("pot")
    parser.run(argv)


if __name__ == '__main__':
    main()
