import requests
from rich import print
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel

console = Console()


url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

def format_entry(item):
    word = item.get('word', '')

    phonetic = item.get('phonetic') or next(
        (p['text'] for p in item.get('phonetics', []) if p.get('text')), ''
    )

    header = f'[bold]{escape(word)}[/bold]'
    if phonetic:
        header += f' /{escape(phonetic)}/'
    lines = [header]

    for meaning in item.get('meanings', []):
        lines.append(f'\n [italic cyan]{escape(meaning["partOfSpeech"])}[/italic cyan]')

        for i, d in enumerate(meaning.get('definitions', []), start=1):
            lines.append(f'  {i}. {escape(d["definition"])}')
            if d.get('example'):
                lines.append(f'     [dim]"{escape(d["example"])}"[/dim]')
            if d.get('synonyms'):
                syn = ', '.join(d['synonyms'][:5])
                lines.append(f'     [green]syn:[/green] {escape(syn)}')
            if d.get('antonyms'):
                ant = ', '.join(d['antonyms'][:5])
                lines.append(f'     [red]ant:[/red] {escape(ant)}')

    if item.get('origin'):
        lines.append(f'\n [dim]Origin: {escape(item["origin"])}[/dim]')

    return '\n'.join(lines)

    
def format_response(respon):

    if not respon:
        return 'No results found.'

    return '\n\n'.join(format_entry(item) for item in respon)

def get_data(word, proj_name):
    r = requests.get(url + word)

    if r.status_code != 200:
        console.print('Failed to fetch results, try again later.')
        return

    rtext = format_response(r.json())
    console.print(Panel(rtext, title=proj_name, subtitle='ENGLISH DICTIONARY'))