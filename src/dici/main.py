# Imports
import argparse
import os

from prompt_toolkit.shortcuts import clear
from rich.console import Console
from rich.panel import Panel

from dici import eng, jisho, ptbr

project_name = 'DICIO'
console = Console()

# Map menu keys and command-line flags to display names and lookup functions.
DICTIONARIES = {
    'jisho': ('JAPANESE DICTIONARY', jisho.get_jisho_data),
    'ptbr':  ('BRAZILIAN PORTUGUESE DICTIONARY', ptbr.get_data),
    'eng': ('ENGLISH DICTIONARY', eng.get_data)
}
MENU = {'1': 'jisho', '2': 'ptbr', '3': 'eng'}

import subprocess
import sys
from importlib.metadata import version, PackageNotFoundError

import requests

PACKAGE = 'dici-open'  # The distribution name, not the import package.


def current_version():
    try:
        return version(PACKAGE)
    except PackageNotFoundError:
        return 'unknown'


def latest_version():
    # Ask PyPI for the newest release. Returns None if it can't be reached.
    try:
        r = requests.get(f'https://pypi.org/pypi/{PACKAGE}/json', timeout=5)
        r.raise_for_status()
        return r.json()['info']['version']
    except (requests.RequestException, KeyError):
        return None


def update():
    current = current_version()
    latest = latest_version()

    if latest is None:
        console.print('[red]Could not check for updates (PyPI unreachable or package not published).[/red]')
        return
    if latest == current:
        console.print(f'[green]Already up to date ({current}).[/green]')
        return

    console.print(f'Updating [bold]{current}[/bold] -> [bold]{latest}[/bold]...')
    result = subprocess.run(
        [sys.executable, '-m', 'pip', 'install', '--upgrade', '--pre', PACKAGE]
    )
    if result.returncode == 0:
        console.print('[green]Updated! Run dicio again to use the new version.[/green]')
    else:
        console.print('[red]Update failed. See the pip output above.[/red]')

def lookup(dict_key, word):
    # Look up the word using the selected dictionary.
    dic_name, search = DICTIONARIES[dict_key]
    search(word, project_name)


def main():
    # Display the interactive menu and handle the user's selection.
    console.print(Panel(
        f'[red bold italic]WELCOME TO {project_name}[/red bold italic]\n \n'
        'What do [red bold]you[/red bold] want to do? \n'
        ' 1. Jisho \n 2. PT-BR \n 3. ENG \n 4. Exit',
        title=project_name,
    ))
    choose = console.input('choose from (1-4) \n> ')

    if choose == '4':
        console.print(Panel('[green bold]See you later![/green bold] \n '
                            '[red bold]Thank you :smile::heart:[/red bold]'))
        return
    if choose not in MENU:
        console.print(Panel('[bold red]:x: This option is unavailable, try again later.'))
        return

    dict_key = MENU[choose]
    clear()
    console.print(Panel('Write the word you want to search for: ',
                        title=project_name, subtitle=DICTIONARIES[dict_key][0]))
    word = console.input('> ')
    lookup(dict_key, word)


def parse_args():
    parser = argparse.ArgumentParser(
        prog='dicio',
        description='Dictionary lookup: Jisho (JP), Dicionário Aberto (PT-BR) and Free Dictionary API (ENG).',
    )
    parser.add_argument('word', nargs='*',
                        help='word to search for (empty = open the menu)')
    parser.add_argument('-u', '--update', action='store_true',
                    help='check for a new version and update')
    parser.add_argument('-v', '--version', action='version',
                    version=f'%(prog)s {current_version()}')

    # Allow at most one dictionary option to be selected.
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-jp', '--jisho', dest='dict_key',
                       action='store_const', const='jisho',
                       help='search in the Japanese dictionary (default)')
    group.add_argument('-ptbr', '--ptbr', dest='dict_key',
                       action='store_const', const='ptbr',
                       help='search in the Portuguese dictionary')
    group.add_argument('-en', '--eng', dest='dict_key', 
                       action='store_const', const='eng',
                       help='search in the English dictionary')

    args = parser.parse_args()
    args.word = ' '.join(args.word)
    return args

def run():
    args = parse_args()

    if args.update:
        update()
        return

    if args.word:
        lookup(args.dict_key or 'jisho', args.word)
    else:
        main()

if __name__ == '__main__':
    run()