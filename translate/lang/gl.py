#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Zuza Software Foundation
#
# This file is part of the Translate Toolkit.
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <http://www.gnu.org/licenses/>.

"""This module represents the Galician language.

.. seealso:: http://en.wikipedia.org/wiki/Galician_language
"""

from translate.lang import common

from translate.lang.fr import guillemets


class gl(common.Common):
    """This class represents Galician."""
    code = "gl"
    fullname = "Galician"
    nplurals = 2
    pluralequation = "(n != 1)"

    specialchars = u'€ñÑ…@→®©™⌘—“”«»’'

    # Characters that can be used as accelerators (access keys) i.e. Alt+X
    # where X is the accelerator. These can include combining diacritics as
    # long as they are accessible from the users keyboard in a single
    # keystroke, but normally they would be at least precomposed characters.
    # All characters, lower and upper, are included in the list.
    validaccel = (u"abcdefghijklmnopqrstuvwxyz"
                  u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                  u"1234567890"
                  u"áéíóú"
                  u"ÁÉÍÓÚ")

    # A space is required both before and after all two- (or more)
    # part punctuation marks and symbols, including : ; « » ! ? % $ # etc.
    puncdict = {}
    for c in u":;!?#":
        puncdict[c] = u"\u00a0%s" % c
    # TODO: consider adding % and $, but think about the consequences of how
    # they could be part of variables.


    #TODO endpunc check shouldn't fail when string ends with ellipsis character instead of three dots.


    @classmethod
    def punctranslate(cls, text):
        """Implement some extra features for quotation marks.

        Known shortcomings:
            - % and $ are not touched yet for fear of variables
            - Double spaces might be introduced
        """
        text = super(cls, cls).punctranslate(text)
        # We might get problems where we got a space in URIs such as
        # http ://
        text = text.replace(u"\u00a0://", "://")
        text = guillemets(text)
        return text
