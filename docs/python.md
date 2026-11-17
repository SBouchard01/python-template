# Python package structure
The main code for the package is located in the `src/` directory, while unit tests are located in the `tests/` directory. Documentation is located in the `docs/` directory.

The `pyproject.toml` file contains configuration for the project, with `setuptools` as the build backend, `pytest` for testing, `ty` for type checking, and `ruff` for linting and formatting. The `dev` extras include testing dependencies such as `pytest`, `pytest-cov`, `ruff`, and `ty`.

The documentation is built using Sphinx, with the `sphinx-book-theme` and `myst_nb` extensions for enhanced functionality. Those dependencies are included in the `docs` extras.

The project can be installed from source using 
```bash
git clone https://github.com/<user>/<package-name>.git
cd <package-name>
pip install .
```