# python-template

<!-- [![Python](https://img.shields.io/pypi/pyversions/<package-name>?color=4c1&logo=pypi)](https://pypi.org/project/<package-name>/) -->
[![Release](https://img.shields.io/github/v/release/SBouchard01/python-template?color=818CF8&logo=github)](https://github.com/SBouchard01/python-template/releases)
[![License](https://img.shields.io/github/license/SBouchard01/python-template?color=fab005)](LICENSE)
[![Tests](https://github.com/SBouchard01/python-template/actions/workflows/release-main.yml/badge.svg)](https://github.com/SBouchard01/python-template/actions/workflows/release-main.yml)
![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/SBouchard01/209001080cfb523453fffcd80ff8c145/raw/coverage-values.json)
![CRAP](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/SBouchard01/209001080cfb523453fffcd80ff8c145/raw/crapscore-values.json)

A GitHub repository template for Python projects, with a focus on code quality, testing, and continuous integration. It includes a pre-configured GitHub Actions workflow for running tests and generating coverage reports.

This project is built with the following conventions and tools in mind:
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Semantic versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [git-cliff](https://git-cliff.org/) for generating changelogs
- [Ruff](https://docs.astral.sh/ruff/) for linting and formatting
- [ty](https://docs.astral.sh/ty/) for type checking
- [pytest](https://docs.pytest.org/en/stable/) for testing and coverage reporting
- [Sphinx](https://www.sphinx-doc.org/en/master/) for documentation


## Installation
From PyPI:
```bash
pip install <package-name>
```

From source:
```bash
git clone https://github.com/<user>/<package-name>.git
cd <package-name>
pip install .
```

> [!NOTE]
> For development, install with the `dev` extras to include testing dependencies:
> ```bash
> pip install -e .[dev]
> ```

## Documentation
Documentation will be available at [`<link here>`](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests. Please follow the development workflow and code quality guidelines outlined above.
AI-assisted contributions are welcome, but you must run, test, and understand every line you submit. See the [AI Usage Policy](AI_POLICY.md) for full details.

## Development workflow
See [DEVELOPMENT.md](DEVELOPMENT.md) for information on the technical side of the codebase: environment setup, code quality, testing, and conventions.
