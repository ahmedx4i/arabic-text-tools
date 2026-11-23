# Contributing

Thanks for helping improve Arabic Text Tools.

## Before opening a pull request

1. Open an issue first for significant features or behavioral changes.
2. Keep each change focused and include tests for changed behavior.
3. Preserve the dependency-free design unless a new dependency is clearly justified.
4. Run the test suite:

       python -m unittest discover -s tests

## Design principles

- Prefer conservative transformations that do not silently change Arabic word meaning.
- Keep the public API small and documented.
- Support Python 3.9 and newer.
