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

#    def test_unicode_escaping(self):
#        """Check that escaped unicode is converted properly."""
#        propsource = "unicode=\u0411\u0416\u0419\u0428"
#        messagevalue = u'\u0411\u0416\u0419\u0428'.encode("UTF-8")
#        propfile = self.format_parse(propsource, personality="mozilla")
#        assert len(propfile.units) == 1
#        propunit = propfile.units[0]
#        assert propunit.name == "unicode"
#        assert propunit.source.encode("UTF-8") == "БЖЙШ"
#        regensource = str(propfile)
#        assert messagevalue in regensource
#        assert "\\u" not in regensource

#    def test_newlines_startend(self):
#        """Check that we preserve \n that appear at start and end of properties."""
#        propsource = "newlines=\\ntext\\n"
#        propregen = self.format_regen(propsource)
#        assert propsource + '\n' == propregen

#    def test_key_value_delimiters_simple(self):
#        """Check that we can handle colon, equals and space delimiter
#        between key and value.  We don't test any space removal or escaping."""
#        delimiters = [":", "=", " "]
#        for delimiter in delimiters:
#            propsource = "key%svalue" % delimiter
#            print("source: '%s'\ndelimiter: '%s'" % (propsource, delimiter))
#            propfile = self.format_parse(propsource)
#            assert len(propfile.units) == 1
#            propunit = propfile.units[0]
#            assert propunit.name == "key"
#            assert propunit.source == "value"

#    def test_comments(self):
#        """Check that we handle # and ! comments."""
#        markers = ['#', '!']
#        for comment_marker in markers:
#            propsource = '''%s A comment
#    key=value
#    ''' % comment_marker
#            propfile = self.format_parse(propsource)
#            print(repr(propsource))
#            print("Comment marker: '%s'" % comment_marker)
#            assert len(propfile.units) == 1
#            propunit = propfile.units[0]
#            assert propunit.comments == ['%s A comment' % comment_marker]

#    def test_trailing_comments(self):
#        """Check that we handle non-unit data at the end of a file."""
#        source = """
#{
#    "firstName": "John",
#    "lastName": "Smith",
#    "age": 25,
#    "address": {
#        "streetAddress": "21 2nd Street",
#        "city": "New York",
#        "state": "NY",
#        "postalCode": "10021"
#    },
#    "phoneNumber": [
#        {
#          "type": "home",
#          "number": "212 555-1234"
#        },
#        {
#          "type": "fax",
#          "number": "646 555-4567"
#        }
#    ]
#}
#"""
#        propsource = u"key = value\n# END"
#        propfile = self.format_parse(propsource)
#        assert len(propfile.units) == 2
#        propunit = propfile.units[1]
#        assert propunit.name == u''
#        assert propunit.source == u''
#        assert propunit.getnotes() == u"# END"
