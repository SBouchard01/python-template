# Documentation

## Build documentation with Sphinx
To build the a documentation with Sphinx, see the [Sphinx quickstart](https://www.sphinx-doc.org/en/master/usage/quickstart.html) for more information.

```{tip}
This template uses the `sphinx-book-theme` theme, with the `myst-nb` extension to display Jupyter notebooks.
```

To build the documentation locally, run:
```bash
cd docs
make html
python -m http.server --directory _build/html
```

## Host documentation on readthedocs.io

To host the documentation on [readthedocs.io](https://readthedocs.org/), you need to create an account and link your GitHub repository. See the [readthedocs documentation](https://docs.readthedocs.com/platform/latest/tutorial/index.html) for more information.

A `.readthedocs.yaml` file is included in the template, which configures the build environment and dependencies for the documentation. You can customize this file to fit your needs.
