#!/usr/bin/env python
# -*- coding: utf-8 -*-

from translate.misc import wStringIO
from translate.storage import jsonl10n, test_monolingual


class TestJSONUnit(test_monolingual.TestMonolingualUnit):
    UnitClass = jsonl10n.JsonUnit

    def test_rich_get(self):
        pass

    def test_rich_set(self):
        pass


class TestJSON(test_monolingual.TestMonolingualStore):
    StoreClass = jsonl10n.JsonFile

    def format_parse(self, source_string):
        """Helper that parses format source without requiring on disk files."""
        dummyfile = wStringIO.StringIO(source_string)
        store = self.StoreClass(dummyfile)
        return store

    def format_regen(self, source_string):
        """Helper that converts format source to Store object and back."""
        return str(self.format_parse(source_string))

    def test_simpledefinition(self):
        """Check that a simple properties definition is parsed correctly."""
        source = """
{
    "testMe": "I can code!"
}
"""
        store = self.format_parse(source)
        assert len(store.units) == 1
        unit = store.units[0]
        assert unit.getid().lstrip(".") == "testMe"
        assert unit.source == "I can code!"

    def test_simpledefinition_source(self):
        """Check that a simple properties definition can be regenerated as source."""
        source = """
{
    "testMe": "I can code!"
}
"""
        regen = self.format_regen(source)
        assert source == "\n" + regen + "\n"
