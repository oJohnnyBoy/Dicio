# Dici

Dici is a lightweight terminal dictionary app built for quick lookups from the command line. The project is currently in alpha and focuses on fast Jisho-based word searches with a simple menu-driven interface.

## Features

- Interactive terminal menu
- Jisho API integration for Japanese and English definitions
- Rich terminal formatting using `rich`
- Simple dictionary workflow optimized for quick lookups

## Current status

At the moment, the main working flow is:

1. Start the app
2. Choose the Jisho option
3. Enter a word to search
4. View the formatted results in the terminal

Other menu entries remain placeholders for future dictionary sources.

## Requirements

- Python 3.15 or later
- Internet access for dictionary API requests

## Install

From the project directory, install the package and its dependencies:

```bash
python -m pip install .
```

For local development, install it in editable mode:

```bash
python -m pip install -e .
```

## Run

After installation, start the CLI with either command:

```bash
python -m dici
```

or:

```bash
dici
```

The app will display a menu like this:

```text
1. Jisho
2. Eng
3. PT-BR
4. Exit
```

Choose `1` to search with Jisho, then enter a word.

## Example usage

```bash
dici
# choose 1
# enter: hello
```

The tool will query the Jisho API and print matching definitions in the terminal.

## Notes

- This project is still evolving.
- The Jisho integration is the primary implemented feature.
- The English and PT-BR entries are not yet fully implemented.

## Troubleshooting

If the CLI does not start, verify that your environment is using the correct Python version and that the project was installed successfully:

```bash
python --version
python -m pip install -e .
python -m dici
```
