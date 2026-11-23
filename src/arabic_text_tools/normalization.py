"""Normalization and tokenization helpers for Arabic text."""

from __future__ import annotations

import re

_ARABIC_DIACRITICS = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")
_ARABIC_LETTERS = re.compile(r"[\u0621-\u063A\u0641-\u064A\u0671]")
_ARABIC_TOKENS = re.compile(r"[\u0621-\u063A\u0641-\u064A]+")

_ALEF_TRANSLATION = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا"})
_YA_TRANSLATION = str.maketrans({"ى": "ي"})


def normalize_arabic(
    text: str,
    *,
    remove_diacritics: bool = True,
    remove_tatweel: bool = True,
    normalize_alef: bool = True,
    normalize_ya: bool = True,
) -> str:
    """Return a conservatively normalized Arabic string.

    The function only applies commonly useful character-level normalizations.
    It deliberately preserves whitespace, punctuation, digits, and the
    taa marbuta character because changing them may alter meaning.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    normalized = text

    if remove_diacritics:
        normalized = _ARABIC_DIACRITICS.sub("", normalized)
    if remove_tatweel:
        normalized = normalized.replace("ـ", "")
    if normalize_alef:
        normalized = normalized.translate(_ALEF_TRANSLATION)
    if normalize_ya:
        normalized = normalized.translate(_YA_TRANSLATION)

    return normalized


def tokenize_arabic(text: str, *, normalize: bool = True) -> list[str]:
    """Extract Arabic word tokens from a string.

    Set normalize to False when the original letter forms are needed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    source = normalize_arabic(text) if normalize else text
    return _ARABIC_TOKENS.findall(source)


def contains_arabic(text: str) -> bool:
    """Return True when a string contains at least one Arabic letter."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return _ARABIC_LETTERS.search(text) is not None
