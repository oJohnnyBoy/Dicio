# Dici

Dici is a lightweight terminal dictionary for quick Japanese and Brazilian
Portuguese word lookups. The project is in alpha.

## Features

- Search Japanese words with Jisho, including readings, commonness, JLPT levels,
  and English definitions.
- Search Brazilian Portuguese words with Dicionário Aberto.
- Use an interactive menu or search directly from the command line.
- Check the installed version and update to a release published on PyPI.
- View formatted results in the terminal with Rich.

The English dictionary menu option is not implemented yet.

## Requirements

- Python 3.15 or later
- Internet access for dictionary API requests

## Installation

Install the package and its dependencies:

```bash
python -m pip install .
```

For local development, install it in editable mode:

```bash
python -m pip install -e .
```

## Usage

Start the interactive menu with either command:

```bash
dici
```

or:

```bash
python -m dici
```

Choose `1` for Jisho, `2` for Brazilian Portuguese, or `4` to exit. The `3`
English option is a placeholder.

### Search from the command line

Pass a word to search directly. Jisho is used by default; select a dictionary
with `--jisho` or `--ptbr`:

```bash
dici cat
dici --jisho hello
dici --ptbr cavalo
```

The same options work with `python -m dici` or `python -m dici.main`. The short
flags `-jp` and `-ptbr` are also available. If no word is supplied, the app
opens the interactive menu. To see all options:

```bash
dici --help
```

### Version and updates

Show the installed version:

```bash
dici --version
```

Check PyPI for the latest release and install it into the active Python
environment:

```bash
dici --update
```

Run `dici` again after the update to use the new version. Updating requires
internet access and a published release on PyPI.

## Development

Run the test suite from the project directory:

```bash
python -m unittest discover -s tests -v
```
