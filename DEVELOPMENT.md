# Development workflow

This document covers the technical side of the codebase: environment setup, code quality, testing, and conventions.
Read [CONTRIBUTING.md](CONTRIBUTING.md) for information on the process side: how to contribute, submit issues, and make pull requests.

## Project structure
The project follows a standard Python package structure:
```
<package-name>/
├── src/                # Source code
│   └── <package-name>/ # Python package
├── tests/              # Test suite
└── docs/               # Documentation
```

---

## Development setup
Clone the repository and install the package in editable mode with development dependencies:
```bash
pip install -e .[dev]
```

## Running Tests
Tests are run using `pytest`. To run the test suite with coverage reporting:
```bash
pytest --cov=src --cov-report=term-missing
```

## Code quality
- Type checking: `ty check src`
- Linting: `ruff check .`
- Formatting: `ruff format .`
- Test: `pytest --cov=src --cov-report=term-missing`
- CRAP score: `crap4py src/ --lcov lcov.info --max-crap 10` (requires `--cov-report=lcov:lcov.info` in the test command)

All must pass before a change is considered done (CI enforces this through GitHub Actions).

> [!TIP]
> [CRAP scores](https://github.com/unclebob/crapper) should be below 10, [Dryer scores](https://github.com/unclebob/dryer) should be below 0.8.
> This is not necessarily a hard limit and not enforced by CI, but it is a good guideline to keep code maintainable (CI only implements a simple CRAP score check).

---

## Branch naming
The project follows the [git-flow](https://nvie.com/posts/a-successful-git-branching-model/) branching model, with a `main` branch for stable releases and a `develop` branch for ongoing development.

Work branches should be created from `develop` and named descriptively, e.g., `feature/add-new-analysis`, `bugfix/fix-typo`, `refactor/optimize-function`.

## Commit Messages
Commits should follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`

PR titles targeting `develop` or `main` must follow the same format. Release impact is derived from commit type:

| Type                                            | Release impact |
| ----------------------------------------------- | -------------- |
| `feat`                                          | Minor          |
| `fix`, `perf`, `refactor`                       | Patch          |
| `docs`, `ci`, `build`, `chore`, `test`, `style` | Changelog only |

Feature work is squash-merged into `develop`.

## Releases
Versions follow [semantic versioning](https://semver.org/) (<major>.<minor>.<patch>).

Release is done by promoting the `develop` branch to main (`git merge --ff-only develop`), which triggers a GitHub Actions workflow that builds a new tag with release notes. In the future, this will also trigger a PyPI release.
