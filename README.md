![foxy](https://github.com/user-attachments/assets/551303aa-e025-46d4-983f-0f933bfccd00)

---

[![Build status](https://img.shields.io/github/actions/workflow/status/proteusiq/pyproject/main.yml?branch=main)](https://github.com/proteusiq/pyproject/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](https://github.com/proteusiq/pyproject/blob/main/pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://proteusiq.github.io/pyproject/)
[![License](https://img.shields.io/github/license/proteusiq/pyproject)](https://img.shields.io/github/license/proteusiq/pyproject)


- [uv](https://docs.astral.sh/uv/) for dependency management
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/), [deptry](https://github.com/proteusiq/deptry/) and [prettier](https://prettier.io/)
- Publishing to [PyPI](https://pypi.org) by creating a new release on GitHub
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Compatibility testing for multiple versions of Python with [tox-uv](https://github.com/tox-dev/tox-uv)
- Containerization with [Docker](https://www.docker.com/)

---

<p align="center">
  <a href="https://proteusiq.github.io/pyproject/">Documentation</a> - <a href="https://github.com/proteusiq/pyproject-example">Example</a>
</p>

---

## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/proteusiq/pyproject.git
```

or if you don't have `uv` installed yet:

```bash
pip install cookiecutter
cookiecutter https://github.com/proteusiq/pyproject.git
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the `README.md` to complete the setup of your project.

## Acknowledgements

This project is based on [Florian Mass\'s](https://github.com/fpgmaas) [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv) => [Audrey
Feldroy\'s](https://github.com/audreyfeldroy)\'s
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
repository.
