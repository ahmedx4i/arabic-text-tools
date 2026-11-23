import unittest

from arabic_text_tools import contains_arabic, normalize_arabic, tokenize_arabic


class NormalizeArabicTests(unittest.TestCase):
    def test_removes_diacritics_and_tatweel(self) -> None:
        self.assertEqual(normalize_arabic("السَّلَامُ علـيكم"), "السلام عليكم")

    def test_normalizes_alef_and_ya_variants(self) -> None:
        self.assertEqual(normalize_arabic("إلى آفاقٍ واسعة"), "الي افاق واسعة")

    def test_can_preserve_optional_forms(self) -> None:
        self.assertEqual(
            normalize_arabic(
                "إِلى",
                remove_diacritics=False,
                normalize_alef=False,
                normalize_ya=False,
            ),
            "إِلى",
        )

    def test_rejects_non_string_input(self) -> None:
        with self.assertRaises(TypeError):
            normalize_arabic(None)  # type: ignore[arg-type]


class TokenizeArabicTests(unittest.TestCase):
    def test_extracts_normalized_arabic_words(self) -> None:
        self.assertEqual(
            tokenize_arabic("Hello، مرحباً بالعالم! 123"),
            ["مرحبا", "بالعالم"],
        )

    def test_can_keep_original_forms(self) -> None:
        self.assertEqual(tokenize_arabic("فَتًى", normalize=False), ["ف", "ت", "ى"])


class ContainsArabicTests(unittest.TestCase):
    def test_detects_arabic_letters(self) -> None:
        self.assertTrue(contains_arabic("نص عربي"))
        self.assertFalse(contains_arabic("plain English"))

    def test_rejects_non_string_input(self) -> None:
        with self.assertRaises(TypeError):
            contains_arabic(42)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
