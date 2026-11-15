import requests
from rich import print
from rich.panel import Panel
from rich.console import Console
from prompt_toolkit.shortcuts import clear


console = Console()

url = 'http://beta.jisho.org/api/v1/search/words'


def get_jisho_data(str, project_name):
    # Jisho accepts the search term as the "keyword" query parameter.
    r = requests.get(
        url,
        params={'keyword': str}
        )

    # Format the API response, clear the previous screen, and show the results.
    rtext = format_jisho_r(r.json())
    clear()
    console.print(Panel(rtext, title=project_name, subtitle='JISHO'))


def format_entry(entry):
    # Use the first Japanese form as the displayed word and reading.
    main = entry['japanese'][0]
    word = main.get('word', '')
    reading = main.get('reading', '')

    # Add commonness and JLPT level, using fallbacks when they are unavailable.
    common = 'common' if entry.get('is_common', False) else 'uncommon'
    jlpt = ', '.join(entry['jlpt']).upper().replace('JLPT-','') or '-'

    lines = [f'{word} 【{reading}】 ({common}, JLPT: {jlpt})']

    # Format each sense with its English meanings and parts of speech.
    for i, sense in enumerate(entry['senses'], start=1):
        meanings = '; '.join(sense['english_definitions'])
        pos = ', '.join(sense['parts_of_speech'])
        lines.append(f" {i}. {meanings} [{pos}]")

    return '\n'.join(lines)


def format_jisho_r(respon):
    # Stop if the API reports a failed search response.
    if respon['meta']['status'] != 200:
        return 'Error: Request failed.'
    
    # Format all matching entries, with a blank line between them.
    entries = respon['data']
    return '\n\n'.join(format_entry(e) for e in entries)