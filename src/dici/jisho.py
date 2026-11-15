import requests
from rich import print
from rich.panel import Panel
from rich.console import Console

from dici import jisho
from dici import main


console = Console()

jisho_url = 'http://beta.jisho.org/api/v1/search/words'

def get_jisho_data(str, project_name):
    r = requests.get(
        jisho_url,
        params={'keyword': str}
        )

    rtext = format_jisho_r(r.json())
    main.clear()
    console.print(Panel(rtext, title=project_name, subtitle='JISHO'))


def format_entry(entry): # Gets the main word and reading and format its entries for japanese dictionary.
    # Main reading and word, corresponding to the first item in 'japanese'.
    main = entry['japanese'][0]
    word = main.get('word', '')
    reading = main.get('reading', '')

    # extra info
    common = 'common' if entry.get('is_common', False) else 'uncommon'
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