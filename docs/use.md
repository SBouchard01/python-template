# Using this template

## Use the repository as a template
See [GitHub documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) for creating a new repository from this template.

## Add secrets
1. [Create a GIST](https://docs.github.com/fr/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists) with two files:
    - `crapscore-values.json`
    - `coverage-values.json`
2. Add the following [variables](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-variables#defining-configuration-variables-for-multiple-workflows) to your repository:
    - `GIST_ID`: the ID of the GIST created in step 1
3. Add the following [secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets#creating-secrets-for-a-repository) to your repository:
    - `GIST_SECRET`: a personal access token (PAT) with the `gist` scope
    <!-- - `RELEASE_BOT_TOKEN`: a personal access token (PAT) with the `repo` scope -->

## Update project information
You need to update the template with your project information. This includes:

**README.md**: The README file contains the project description, badges, and links. Update the following placeholders:
- `<package-name>`: the name of your package
- `<user>`: your GitHub username or organization name
- Badges: Update the badges to use your repository information; use the GIST ID to generate the coverage and CRAP score badges.

**pyproject.toml**: The `pyproject.toml` file contains the project metadata and dependencies. Update the following placeholders:
- `name`: the name of your package
- Add the commented-out sections (dependencies, authors, URLs, etc.)

```{tip}
Most of the pyproject.toml fields - such as the Ruff, Ty and Pytest settings - are already set up.
```

**LICENSE**: Update the license file & authors with your project license. The template uses the MIT license by default.

## Update documentation
Delete the `docs` folder and recreate it from scratch using Sphinx. See [Sphinx quickstart](https://www.sphinx-doc.org/en/master/usage/quickstart.html) for more information.

```{tip}
It is easier to recreate the documentation from scratch than to update the existing one, but feel free to take inspiration from the existing documentation of the template.
```

## Create an initial release
The release workflow works by comparing release versions, and fails if none is found. You need to create an initial release manually to set the first version number at `0.0.0`.

## Protect the branches
[Branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) do not carry over to the new repository. You will need to set them up manually.

On the `develop` branch, enable the following rulesets:
- Restrict deletions
- Require linear history (no merge commits)
- Require a pull request before merging
  - Required approvals: 1
  - Require conversation resolution before merging
  - Allowed merge methods: Squash
- Require status checks to pass for the `ci-validate` and `semantic-pr-title` workflows
- Block force pushes

On the `main` branch, enable the following ruleset (except for Maintain and admin roles):
- Restrict creations
- Restrict updates
- Restrict deletions
- Require linear history (no merge commits)
- Block force pushes

```{tip}
We recommend setting the `develop` branch as the default branch, as this is the branch pull requests will default to.
```

## References:
- Dynamic badges with GIST: [link](https://github.com/Schneegans/dynamic-badges-action)
- Release workflow inspiration: [link](https://github.com/grimmory-tools/grimmory/blob/develop/.github/workflows/release-main.yml)
- Writing a pyproject.toml: [link1](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/), [link2](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)