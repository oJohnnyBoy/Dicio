import re
import requests
import xml.etree.ElementTree as ET
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel

console = Console()

# The API returns each dictionary entry with its definitions in XML.
url = 'https://api.dicionario-aberto.net/word/'


def format_entry(item):
    # Parse the entry's XML so its word, definitions, and labels can be extracted.
    root = ET.fromstring(item['xml'])

    # Read the headword and optional etymology from the XML.
    word = root.findtext('form/orth', default=item.get('word', ''))
    etym = (root.findtext('etym') or '').strip()

    # Escape API text before adding Rich markup, preventing text from being
    # interpreted as formatting.
    lines = [f'[bold]{escape(word)}[/bold]']

    # Each <sense> contains a definition and may include grammar or usage labels.
    n = 1
    for sense in root.findall('sense'):
        gram = (sense.findtext('gramGrp') or '').strip()
        usg = (sense.findtext('usg') or '').strip()
        tags = ', '.join(t for t in (gram, usg) if t)
        suffix = f' [dim]\\[{escape(tags)}][/dim]' if tags else ''

        # A sense can contain multiple newline-separated definitions.
        definition = sense.findtext('def') or ''
        for line in definition.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
            line = escape(line)
            line = re.sub(r'_(.+?)_', r'[italic]\1[/italic]', line)
            lines.append(f' {n}. {line}{suffix}')
            n += 1

    # Show the etymology after the definitions when one is available.
    if etym:
        lines.append(f' [dim]{escape(etym)}[/dim]')

    return '\n'.join(lines)


def format_response(respon):
    # An empty API result means the word was not found.
    if not respon:
        return 'No results found.'

    # Format each returned entry and separate entries with a blank line.
    return '\n\n'.join(format_entry(item) for item in respon)


def get_data(word, proj_name):
    # The API expects the searched word as the final part of the URL.
    r = requests.get(url + word)

    # Do not try to parse a response when the HTTP request failed.
    if r.status_code != 200:
        console.print('Failed to fetch results, try again later.')
        return

    # Convert the JSON response to formatted text and display it in a panel.
    rtext = format_response(r.json())
    console.print(Panel(rtext, title=proj_name, subtitle='BRAZILIAN PORTUGUESE DICTIONARY'))