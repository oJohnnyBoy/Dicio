#| libraries
#⌊→ system libraries
import os
import sys

#⌊→ cli library
from rich import print
from rich import console
from rich import panel
from rich.panel import Panel
from rich.console import Console

#⌊→ api library
import requests
import deepl

#⌊→ apis var
jisho_url = ''
project_name = 'DICIOPEN'

def main():
    console = Console()

    text = f'[red bold italic]WELCOME TO {project_name}[/red bold italic]'
    text2= f'What do [red bold]you[/red bold] want to do?'
    while True:
        console.print(Panel(f'{text}\n{text2}',title='DICIOPEN'))
        choose = console.input('choose from (1-4)')
        if choose == '4':
            break
        else:
            pass


    

def get_jisho_data(word):
    response = requests.get(jisho_url+word)
    print(response)




if __name__ == '__main__':
    main()