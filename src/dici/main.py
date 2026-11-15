#| libraries
import os

#⌊→ cli library
from prompt_toolkit.shortcuts import clear
from rich import print
from rich.panel import Panel
from rich.console import Console

#⌊→ api library
import requests

#⌊→ apis var
from dici import jisho

project_name = 'DICIOPEN'

formatation = {'word', 'sentence', 'meaning'}

console = Console()

def main():
    
    while True:
        console.print(Panel(f'[red bold italic]WELCOME TO {project_name}[/red bold italic]\n \nWhat do [red bold]you[/red bold] want to do? \n 1. Jisho \n 2. Eng \n 3. PT-BR',title='DICIOPEN'))
        choose = console.input('choose from (1-4) \n> ')
        if choose == '4':
            console.print(Panel('[green bold]See you later![/green bold] \n [red bold]Thank you :smile::heart:[/red bold]'))
            break
        ## DICTIONARY
        elif choose == '1':     # gets the word and calls jisho function
            clear()
            console.print(Panel('Write the word you want to search for: [grey italic](obs. in english or japanese)',title=project_name,subtitle="Japanese Dicitionary"))
            word = console.input('> ')
            jisho.get_jisho_data(word, project_name)
            break

        ##DICIO
        elif choose == '2':
            pass

        ## ENG
        elif choose == '3':
            pass

        else:
            console.print(Panel('[bold red]:x: This option is unavailable, try again later.'))
            break


    

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()