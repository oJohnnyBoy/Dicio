#| libraries

#⌊→ cli library
from prompt_toolkit.shortcuts import clear
from rich import print
from rich.panel import Panel
from rich.console import Console

#⌊→ api library
import requests

#⌊→ apis var
jisho_url = 'http://beta.jisho.org/api/v1/search/words'
project_name = 'DICIOPEN'

formatation = {'word', 'sentence', 'meaning'}

console = Console()

def main():
    content = f''
    text = f'[red bold italic]WELCOME TO {project_name}[/red bold italic]'
    text2= f'What do [red bold]you[/red bold] want to do? \n 1. Jisho \n 2. Eng \n 3. PT-BR'
    while True:
        console.print(Panel(f'{text}\n \n{text2}',title='DICIOPEN'))
        choose = console.input('choose from (1-4) \n> ')
        if choose == '4':
            console.print(Panel('[green bold]See you later![/green bold] \n [red bold]Thank you :smile::heart:[/red bold]'))
            break
        elif choose == '1':     # gets the word and calls jisho function
            clear()
            console.print(Panel('Write the word you want to search for: [grey italic](obs. in english or japanese)',title=project_name,subtitle="Japanese Dicitionary"))
            word = console.input('> ')
            get_jisho_data(word)
            break
        elif choose == '2':
            pass
        elif choose == '3':
            pass

        else:
            console.print(Panel('[bold red]:x: This option is unavailable, try again later.'))
            break


    

def get_jisho_data(str):
    r = requests.get(
        jisho_url,
        params={'keyword': str}
        )

    rtext = format_jisho_r(r.json())    
    console.print(Panel(rtext, title=project_name, subtitle='JISHO'))


def format_entry(entry): # Gets the main word and reading and format its entries.
    # Main reading and word, corresponding to the first item in 'japanese'.
    maind = entry['japanese'][0]
    word = maind.get('word', '')
    reading = maind.get('reading', '')

    # extra info
    common = 'common' if entry['is_common'] else 'uncommon'
    jlpt = ', '.join(entry['jlpt']).upper().replace('JLPT-','') or '-'

    lines = [f'{word} 【{reading}】 ({common}, JLPT: {jlpt})']

    # definitions
    for i, sense in enumerate(entry['senses'], start=1):
        meanings = '; '.join(sense['english_definitions'])
        pos = ', '.join(sense['parts_of_speech'])
        lines.append(f" {i}. {meanings} [{pos}]")

    return '\n'.join(lines)

def format_jisho_r(respon):
    if respon['meta']['status'] != 200:
        return 'Error: Request failed.'

    entries = respon['data']
    return '\n\n'.join(format_entry(e) for e in entries)

if __name__ == '__main__':
    main()