# Arabic Text Tools

Small, dependency-free Python utilities for normalizing and tokenizing Arabic text.

## Features

- Remove Arabic diacritics and tatweel
- Normalize common alef and ya variants
- Extract Arabic word tokens
- Detect whether text contains Arabic characters
- Standard-library only, with a tested public API

## Install

    pip install arabic-text-tools

For local development:

    python -m pip install -e .

## Quick start

    from arabic_text_tools import normalize_arabic, tokenize_arabic

    normalize_arabic("إِنَّ اللُّغَةَ العَرَبِيَّةَ جَمِيلَةٌ")
    # "ان اللغه العربيه جميله"

    tokenize_arabic("مرحبا، هذا اختبار بسيط!")
    # ["مرحبا", "هذا", "اختبار", "بسيط"]

## API

- normalize_arabic(text, ...) normalizes Arabic letter variants and optional marks.
- tokenize_arabic(text, ...) returns normalized Arabic word tokens.
- contains_arabic(text) checks whether a string contains Arabic-script letters.

The normalizer is intentionally conservative: it does not transliterate or change words beyond the explicitly selected character normalizations.

## Contributing

Bug reports, documentation improvements, and tests are welcome. Read CONTRIBUTING.md before opening a pull request.

## License

MIT
