import requests
import json
from rich.table import Table
from rich.console import Console

limit = 100
days = 365

url = f"https://eonet.gsfc.nasa.gov/api/v3/events?limit={limit}&days={days}"

res = requests.get(url)
res.raise_for_status()
events_data = res.json()

#JSON speichern
with open('events.json', 'w') as file:
    file.write(json.dumps(events_data, indent=4))

# Tabelle erstellen
table = Table(title="NASA EONET Events")
table.add_column("Nr.", justify="right", style="cyan", no_wrap=True)
table.add_column("Event Title", style="bold green")
table.add_column("Category", style="yellow")
table.add_column("Date", style="magenta")

#Fill table with data
event_list = events_data.get('events', [])
for i, event in enumerate(event_list, start=1):
    title = event.get('title', 'N/A')
    category = event.get('categories', [{}])[0].get('title', 'Unknown')
    date = event.get('geometry', [{}])[0].get('date', 'N/A')
    table.add_row(str(i), title, category, date)

# Tabelle ausgeben
console = Console()
console.print(table)