import unittest

from dici.main import format_entry


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


if __name__ == "__main__":
    unittest.main()
