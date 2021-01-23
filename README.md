Convert python-poetry(pyproject.toml) to setup.py.

It only relies on poetry.core, so the effect is better than any other third-party software.

I created this library because python-poetry does not support exporting to setup.py and dephell will generate setup.py incorrectly in some cases.

## Install

```bash
pip install poetry2setup
```

## Usage

Run command `poetry2setup` in your project directory, it will display `setup.py` content in console. If you want to export to `setup.py`, just run `poetry2setup > setup.py`.
