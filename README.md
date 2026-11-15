# Dici

Dici is a lightweight terminal dictionary for quick Japanese and Brazilian
Portuguese word lookups. The project is in alpha.

## Features

- Search Japanese words with Jisho, including readings, commonness, JLPT levels,
  and English definitions.
- Search Brazilian Portuguese words with Dicionário Aberto.
- Use an interactive menu or search directly from the command line.
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

Use `python -m dici.main` to search directly. If no dictionary option is
provided, Jisho is used by default:

```bash
python -m dici.main cat
python -m dici.main --jisho hello
python -m dici.main --ptbr cavalo
```

The short options `-jp` and `-ptbr` are also available. To see all options:

```bash
python -m dici.main --help
```

## Development

Run the test suite from the project directory:

```bash
python -m unittest discover -s tests -v
```
