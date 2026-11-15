import unittest
from unittest.mock import Mock, patch

from dici import main as main_module
from dici.jisho import format_entry


class DictionarySelectionTests(unittest.TestCase):
    def test_ptbr_lookup_receives_the_entered_word(self):
        get_data = Mock()
        dictionaries = {"ptbr": ("BRAZILIAN PORTUGUESE DICTIONARY", get_data)}
        with patch.object(main_module, "DICTIONARIES", dictionaries):
            main_module.lookup("ptbr", "casa")

        get_data.assert_called_once_with("casa", main_module.project_name)


class FormatEntryTests(unittest.TestCase):
    def test_formats_word_reading_and_meanings(self):
        entry = {
            "japanese": [{"word": "猫", "reading": "ねこ"}],
            "is_common": True,
            "jlpt": ["jlpt-n5"],
            "senses": [
                {
                    "english_definitions": ["cat", "feline"],
                    "parts_of_speech": ["Noun"],
                }
            ],
        }

        self.assertEqual(
            format_entry(entry),
            "猫 【ねこ】 (common, JLPT: N5)\n 1. cat; feline [Noun]",
        )

    def test_formats_entry_without_common_flag_as_uncommon(self):
        entry = {
            "japanese": [{"word": "猫", "reading": "ねこ"}],
            "jlpt": [],
            "senses": [
                {
                    "english_definitions": ["cat"],
                    "parts_of_speech": ["Noun"],
                }
            ],
        }

        self.assertEqual(
            format_entry(entry),
            "猫 【ねこ】 (uncommon, JLPT: -)\n 1. cat [Noun]",
        )


if __name__ == "__main__":
    unittest.main()
