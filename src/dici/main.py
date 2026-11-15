#| libraries
import argparse
import os

from prompt_toolkit.shortcuts import clear
from rich.console import Console
from rich.panel import Panel

from dici import jisho, ptbr

project_name = 'DICIOPEN'
console = Console()

# Mapa: opção do menu / flag -> (nome exibido, função de busca)
DICTIONARIES = {
    'jisho': ('JAPANESE DICTIONARY', jisho.get_jisho_data),
    'ptbr':  ('BRAZILIAN PORTUGUESE DICTIONARY', ptbr.get_data),
}
MENU = {'1': 'jisho', '2': 'ptbr'}


def lookup(dict_key, word):
    # Busca a palavra no dicionário escolhido.
    dic_name, search = DICTIONARIES[dict_key]
    search(word, project_name)


def main():
    # Menu interativo.
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
    if choose == '3':
        console.print(Panel('[yellow]ENG dictionary not implemented yet.[/yellow]'))
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
        prog='dici',
        description='Dictionary lookup: Jisho (JP) and Dicionário Aberto (PT-BR).',
    )
    parser.add_argument('word', nargs='*',
                        help='word to search for (empty = open the menu)')

    # Só um dos dois pode ser usado por vez.
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-jp', '--jisho', dest='dict_key',
                       action='store_const', const='jisho',
                       help='search in the Japanese dictionary (default)')
    group.add_argument('-ptbr', '--ptbr', dest='dict_key',
                       action='store_const', const='ptbr',
                       help='search in the Portuguese dictionary')

    args = parser.parse_args()
    args.word = ' '.join(args.word)
    return args


if __name__ == '__main__':
    args = parse_args()

    if args.word:
        lookup(args.dict_key or 'jisho', args.word)
    else:
        main()