#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

from translate.misc import wStringIO
from translate.storage import aresource, test_monolingual


class TestAndroidResourceUnit(test_monolingual.TestMonolingualUnit):
    UnitClass = aresource.AndroidResourceUnit

    def __check_escape(self, string, xml):
        """Helper that checks that a string is output with the right escape."""
        unit = self.UnitClass(string, "Test String")

        print("unit.source:", repr(unit.source))
        print("xml:", repr(xml))

        assert str(unit) == xml

    def __check_parse(self, string, xml):
        """Helper that checks that a string is parsed correctly."""
        if etree.LXML_VERSION >= (2, 1, 0):
            # Since version 2.1.0 we can pass the strip_cdata parameter to
            # indicate that we don't want cdata to be converted to raw XML.
            parser = etree.XMLParser(strip_cdata=False)
        else:
            parser = etree.XMLParser()

        translatable = 'translatable="false"' not in xml
        et = etree.fromstring(xml, parser)
        unit = self.UnitClass.createfromxmlElement(et)

        print("unit.source:", repr(unit.source))
        print("string:", string)
        print("translatable:", repr(unit.istranslatable()))

        assert unit.source == string
        assert unit.istranslatable() == translatable

    ############################ Check string escape ##########################

    def test_escape_message_with_newline(self):
        string = 'message\nwith newline'
        xml = '<string name="Test String">message\\nwith newline</string>\n'
        self.__check_escape(string, xml)

    def test_escape_message_with_newline_in_xml(self):
        string = 'message \nwith newline in xml'
        xml = ('<string name="Test String">message\n\\nwith newline in xml'
               '</string>\n')
        self.__check_escape(string, xml)

    def test_escape_twitter(self):
        string = '@twitterescape'
        xml = '<string name="Test String">\\@twitterescape</string>\n'
        self.__check_escape(string, xml)

    def test_escape_quote(self):
        string = 'quote \'escape\''
        xml = '<string name="Test String">quote \\\'escape\\\'</string>\n'
        self.__check_escape(string, xml)

    def test_escape_double_space(self):
        string = 'double  space'
        xml = '<string name="Test String">"double  space"</string>\n'
        self.__check_escape(string, xml)

    def test_escape_leading_space(self):
        string = ' leading space'
        xml = '<string name="Test String">" leading space"</string>\n'
        self.__check_escape(string, xml)

    def test_escape_xml_entities(self):
        string = '>xml&entities'
        xml = '<string name="Test String">&gt;xml&amp;entities</string>\n'
        self.__check_escape(string, xml)

    def test_escape_html_code(self):
        string = 'some <b>html code</b> here'
        xml = ('<string name="Test String">some <b>html code</b> here'
               '</string>\n')
        self.__check_escape(string, xml)

    def test_escape_arrows(self):
        string = '<<< arrow'
        xml = '<string name="Test String">&lt;&lt;&lt; arrow</string>\n'
        self.__check_escape(string, xml)

    def test_escape_link(self):
        string = '<a href="http://example.net">link</a>'
        xml = ('<string name="Test String"><a href="http://example.net">link'
               '</a></string>\n')
        self.__check_escape(string, xml)

    def test_escape_link_and_text(self):
        string = '<a href="http://example.net">link</a> and text'
        xml = ('<string name="Test String"><a href="http://example.net">link'
               '</a> and text</string>\n')
        self.__check_escape(string, xml)

    def test_escape_blank_string(self):
        string = ''
        xml = '<string name="Test String"></string>\n'
        self.__check_escape(string, xml)

    ############################ Check string parse ###########################

    def test_parse_message_with_newline(self):
        string = 'message\nwith newline'
        xml = '<string name="Test String">message\\nwith newline</string>\n'
        self.__check_parse(string, xml)

    def test_parse_message_with_newline_in_xml(self):
        string = 'message \nwith newline in xml'
        xml = ('<string name="Test String">message\n\\nwith newline in xml'
               '</string>\n')
        self.__check_parse(string, xml)

    def test_parse_twitter(self):
        string = '@twitterescape'
        xml = '<string name="Test String">\\@twitterescape</string>\n'
        self.__check_parse(string, xml)

    def test_parse_quote(self):
        string = 'quote \'escape\''
        xml = '<string name="Test String">quote \\\'escape\\\'</string>\n'
        self.__check_parse(string, xml)

    def test_parse_double_space(self):
        string = 'double  space'
        xml = '<string name="Test String">"double  space"</string>\n'
        self.__check_parse(string, xml)

    def test_parse_leading_space(self):
        string = ' leading space'
        xml = '<string name="Test String">" leading space"</string>\n'
        self.__check_parse(string, xml)

    def test_parse_xml_entities(self):
        string = '>xml&entities'
        xml = '<string name="Test String">&gt;xml&amp;entities</string>\n'
        self.__check_parse(string, xml)

    def test_parse_html_code(self):
        string = 'some <b>html code</b> here'
        xml = ('<string name="Test String">some <b>html code</b> here'
               '</string>\n')
        self.__check_parse(string, xml)

    def test_parse_arrows(self):
        string = '<<< arrow'
        xml = '<string name="Test String">&lt;&lt;&lt; arrow</string>\n'
        self.__check_parse(string, xml)

    def test_parse_link(self):
        string = '<a href="http://example.net">link</a>'
        xml = ('<string name="Test String"><a href="http://example.net">link'
               '</a></string>\n')
        self.__check_parse(string, xml)

    def test_parse_link_and_text(self):
        string = '<a href="http://example.net">link</a> and text'
        xml = ('<string name="Test String"><a href="http://example.net">link'
               '</a> and text</string>\n')
        self.__check_parse(string, xml)

    def test_parse_blank_string(self):
        string = ''
        xml = '<string name="Test String"></string>\n'
        self.__check_parse(string, xml)

    def test_parse_blank_string_again(self):
        string = ''
        xml = '<string name="Test String"/>\n'
        self.__check_parse(string, xml)

    def test_parse_double_quotes_string(self):
        """Check that double quotes got removed."""
        string = 'double quoted text'
        xml = '<string name="Test String">"double quoted text"</string>\n'
        self.__check_parse(string, xml)

    def test_parse_newline_in_string(self):
        """Check that newline is read as space.

        At least it seems to be what Android does.
        """
        string = 'newline in string'
        xml = '<string name="Test String">newline\nin string</string>\n'
        self.__check_parse(string, xml)

    def test_parse_not_translatable_string(self):
        string = 'string'
        xml = ('<string name="Test String" translatable="false">string'
               '</string>\n')
        self.__check_parse(string, xml)


class TestAndroidResourceFile(test_monolingual.TestMonolingualStore):
    StoreClass = aresource.AndroidResourceFile

    def __parse_android(self, android_source):
        """Helper that parses Android source without requiring files."""
        dummy_file = wStringIO.StringIO(android_source)
        android_file = aresource.AndroidResourceFile(dummy_file)
        return android_file

    def __regen_android(self, android_source):
        """Helper that converts Android source to AndroidResourceFile object
        and back.
        """
        return str(self.__parse_android(android_source))

    ############################ Tests ########################################

    def test_parse_several_consecutive_comments(self):
        """Check that several consecutive comments are correctly parsed."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: Don't translate the placeables. -->
  <!-- Translators: Another comment for you. -->
  <string name="hello">Hello!</string>
</resources>
"""
        android_file = self.__parse_android(xml)
        assert len(android_file.units) == 1
        unit = android_file.units[0]
        assert unit.getid() == "hello"
        assert unit.istranslatable() == True
        assert unit.source == "Hello!"
        assert len(unit._comments) == 2
        assert unit._comments[0] == (" Translators: Don't translate the "
                                     "placeables. ")
        assert unit._comments[1] == " Translators: Another comment for you. "

    def test_roundtrip_several_consecutive_comments(self):
        """Check that roundtrip keeps several consecutive comments."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: Don't translate the placeables. -->
  <!-- Translators: Another comment for you. -->
  <string name="hello">Hello!</string>
</resources>
"""
        android_roundtrip = self.__regen_android(xml)
        assert xml == android_roundtrip

    def test_parse_no_strings(self):
        """Check that several consecutive comments are correctly parsed."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources/>
"""
        android_file = self.__parse_android(xml)
        assert len(android_file.units) == 0

    def test_roundtrip_no_strings(self):
        """Check that roundtrip keeps several consecutive comments."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources/>
"""
        android_roundtrip = self.__regen_android(xml)
        assert xml == android_roundtrip

    def test_parse_several_strings(self):
        """Check that several strings are correctly parsed."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <string name="hello">Hello!</string>
  <string name="how">How are you?</string>
  <string name="bye">Goodbye!</string>
</resources>
"""
        android_file = self.__parse_android(xml)
        assert len(android_file.units) == 3
        unit = android_file.units[0]
        assert unit.getid() == "hello"
        assert unit.istranslatable() == True
        assert unit.source == "Hello!"
        assert len(unit._comments) == 0
        unit = android_file.units[1]
        assert unit.getid() == "how"
        assert unit.istranslatable() == True
        assert unit.source == "How are you?"
        assert len(unit._comments) == 0
        unit = android_file.units[2]
        assert unit.getid() == "bye"
        assert unit.istranslatable() == True
        assert unit.source == "Goodbye!"
        assert len(unit._comments) == 0

    def test_roundtrip_several_strings(self):
        """Check that roundtrip keeps several strings."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <string name="hello">Hello!</string>
  <string name="how">How are you?</string>
  <string name="bye">Goodbye!</string>
</resources>
"""
        android_roundtrip = self.__regen_android(xml)
        assert xml == android_roundtrip

    def test_parse_translatable_and_untranslatable_strings(self):
        """Check that translatable status for strings is correctly parsed."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <string name="hello">Hello!</string>
  <string name="how" translatable="false">How are you?</string>
  <string name="bye">Goodbye!</string>
</resources>
"""
        android_file = self.__parse_android(xml)
        assert len(android_file.units) == 3
        unit = android_file.units[0]
        assert unit.getid() == "hello"
        assert unit.istranslatable() == True
        assert unit.source == "Hello!"
        assert len(unit._comments) == 0
        unit = android_file.units[1]
        assert unit.getid() == "how"
        assert unit.istranslatable() == False
        assert unit.source == "How are you?"
        assert len(unit._comments) == 0
        unit = android_file.units[2]
        assert unit.getid() == "bye"
        assert unit.istranslatable() == True
        assert unit.source == "Goodbye!"
        assert len(unit._comments) == 0

    def test_roundtrip_translatable_and_untranslatable_strings(self):
        """Check that roundtrip keeps translatable status for strings."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <string name="hello">Hello!</string>
  <string name="how" translatable="false">How are you?</string>
  <string name="bye">Goodbye!</string>
</resources>
"""
        android_roundtrip = self.__regen_android(xml)
        assert xml == android_roundtrip

    def test_parse_strings_and_comments(self):
        """Check that mixed strings and comments are correctly parsed."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: Don't translate the placeables. -->
  <!-- Translators: Another comment for you. -->
  <string name="hello">Hello!</string>
  <string name="how" translatable="false">How are you?</string>
  <!-- Translators: Comment for goodbye. -->
  <string name="bye">Goodbye!</string>
</resources>
"""
        android_file = self.__parse_android(xml)
        assert len(android_file.units) == 3
        unit = android_file.units[0]
        assert unit.getid() == "hello"
        assert unit.istranslatable() == True
        assert unit.source == "Hello!"
        assert len(unit._comments) == 2
        assert unit._comments[0] == (" Translators: Don't translate the "
                                     "placeables. ")
        assert unit._comments[1] == " Translators: Another comment for you. "
        unit = android_file.units[1]
        assert unit.getid() == "how"
        assert unit.istranslatable() == False
        assert unit.source == "How are you?"
        assert len(unit._comments) == 0
        unit = android_file.units[2]
        assert unit.getid() == "bye"
        assert unit.istranslatable() == True
        assert unit.source == "Goodbye!"
        assert len(unit._comments) == 1
        assert unit._comments[0] == " Translators: Comment for goodbye. "

    def test_roundtrip_strings_and_comments(self):
        """Check that roundtrip keeps mixed strings and comments."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: Don't translate the placeables. -->
  <!-- Translators: Another comment for you. -->
  <string name="hello">Hello!</string>
  <string name="how" translatable="false">How are you?</string>
  <!-- Translators: Comment for goodbye. -->
  <string name="bye">Goodbye!</string>
</resources>
"""
        android_roundtrip = self.__regen_android(xml)
        assert xml == android_roundtrip

    def test_parse_commented_strings(self):
        """Check that commented strings are correctly parsed."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <string name="hello">Hello!</string>
  <!--<string name="how" translatable="false">How are you?</string>-->
  <!-- Translators: Comment for goodbye. -->
  <string name="bye">Goodbye!</string>
</resources>
"""
        android_file = self.__parse_android(xml)
        assert len(android_file.units) == 2
        unit = android_file.units[0]
        assert unit.getid() == "hello"
        assert unit.istranslatable() == True
        assert unit.source == "Hello!"
        assert len(unit._comments) == 0
        unit = android_file.units[1]
        assert unit.getid() == "bye"
        assert unit.istranslatable() == True
        assert unit.source == "Goodbye!"
        assert len(unit._comments) == 2
        assert unit._comments[0] == ('<string name="how" translatable="false">'
                                     'How are you?</string>')
        assert unit._comments[1] == " Translators: Comment for goodbye. "

    def test_roundtrip_commented_strings(self):
        """Check that roundtrip keeps commented strings."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <string name="hello">Hello!</string>
  <!--<string name="how" translatable="false">How are you?</string>-->
  <!-- Translators: Comment for goodbye. -->
  <string name="bye">Goodbye!</string>
</resources>
"""
        android_roundtrip = self.__regen_android(xml)
        assert xml == android_roundtrip

    def test_parse_multiline_comments(self):
        """Check that multiline comments are correctly parsed."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: Don't translate
 the
 placeables. -->
  <string name="hello">Hello!</string>
</resources>
"""
        android_file = self.__parse_android(xml)
        assert len(android_file.units) == 1
        unit = android_file.units[0]
        assert unit.getid() == "hello"
        assert unit.istranslatable() == True
        assert unit.source == "Hello!"
        assert len(unit._comments) == 1
        assert unit._comments[0] == (" Translators: Don't translate\n the\n "
                                     "placeables. ")

    def test_roundtrip_multiline_comments(self):
        """Check that roundtrip keeps multiline comments."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: Don't translate
 the placeables. -->
  <string name="hello">Hello!</string>
</resources>
"""
        android_roundtrip = self.__regen_android(xml)
        assert xml == android_roundtrip

    def test_parse_regular_and_multiline_comments(self):
        """Check that regular and multiline comments are correctly parsed."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: First comment for you. -->
  <!-- Translators: Don't translate
 the
 placeables. -->
  <!-- Translators: Another comment for you. -->
  <string name="hello">Hello!</string>
</resources>
"""
        android_file = self.__parse_android(xml)
        assert len(android_file.units) == 1
        unit = android_file.units[0]
        assert unit.getid() == "hello"
        assert unit.istranslatable() == True
        assert unit.source == "Hello!"
        assert len(unit._comments) == 3
        assert unit._comments[0] == " Translators: First comment for you. "
        assert unit._comments[1] == (" Translators: Don't translate\n the\n "
                                     "placeables. ")
        assert unit._comments[2] == " Translators: Another comment for you. "

    def test_roundtrip_regular_and_multiline_comments(self):
        """Check that roundtrip keeps regular and multiline comments."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: First comment for you. -->
  <!-- Translators: Don't translate
 the placeables. -->
  <!-- Translators: Another comment for you. -->
  <string name="hello">Hello!</string>
</resources>
"""
        android_roundtrip = self.__regen_android(xml)
        assert xml == android_roundtrip

    def test_parse_strips_comment_after_last_string(self):
        """Check that comment after last string is not parsed."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: Don't translate the placeables. -->
  <!-- Translators: Another comment for you. -->
  <string name="hello">Hello!</string>
  <!-- Translators: This is the last comment. -->
</resources>
"""
        android_file = self.__parse_android(xml)
        assert len(android_file.units) == 1
        unit = android_file.units[0]
        assert unit.getid() == "hello"
        assert unit.istranslatable() == True
        assert unit.source == "Hello!"
        assert len(unit._comments) == 2
        assert unit._comments[0] == (" Translators: Don't translate the "
                                     "placeables. ")
        assert unit._comments[1] == " Translators: Another comment for you. "

    def test_roundtrip_strips_comment_after_last_string(self):
        """Check that roundtrip strips the comment after last string."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: Don't translate the placeables. -->
  <!-- Translators: Another comment for you. -->
  <string name="hello">Hello!</string>
  <!-- Translators: This is the last comment. -->
</resources>
"""
        expected_xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <!-- Translators: Don't translate the placeables. -->
  <!-- Translators: Another comment for you. -->
  <string name="hello">Hello!</string>
</resources>
"""
        android_roundtrip = self.__regen_android(xml)
        assert expected_xml == android_roundtrip

    def test_parse_strips_newline(self):
        """Check that parsing a string with newline strips the newline."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <string name="byeworld">Goodbye
 world.</string>
  <string name="hello">Hello!</string>
</resources>
"""
        android_file = self.__parse_android(xml)
        assert len(android_file.units) == 2
        unit = android_file.units[0]
        assert unit.getid() == "byeworld"
        assert unit.istranslatable() == True
        assert unit.source == "Goodbye world."
        assert len(unit._comments) == 0
        unit = android_file.units[1]
        assert unit.getid() == "hello"
        assert unit.istranslatable() == True
        assert unit.source == "Hello!"
        assert len(unit._comments) == 0

    def test_roundtrip_strips_newline(self):
        """Check that roundtrip strips the newline."""
        xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <string name="byeworld">Goodbye
 world.</string>
  <string name="hello">Hello!</string>
</resources>
"""
        expected_xml = """<?xml version='1.0' encoding='utf-8'?>
<resources>
  <string name="byeworld">Goodbye world.</string>
  <string name="hello">Hello!</string>
</resources>
"""
        android_roundtrip = self.__regen_android(xml)
        assert expected_xml == android_roundtrip









    #TODO check all the cases you can come with:
    #### - no units,
    #### - several units,
    #### - mixed translatable/untranslatable units,
    #### - mixed units/comments,
    #### - commented units,
    #### - comment that spans several lines,
    #### - comment followed by several-lines comment followed by comment,
    #### - comment after last unit,
    #### - multiline units,
    # - units with escaping,
    # - 
    #TODO check in tests for other formats to make sure nothing is left behind.
    #TODO create tests for the escape_android() and unescape_android() functions



