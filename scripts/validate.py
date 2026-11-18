import csv, json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for file in (root/'data').glob('*.json'):
    json.loads(file.read_text())
for file in (root/'data').glob('*.csv'):
    with file.open(newline='') as handle:
        rows=list(csv.DictReader(handle))
        assert handle.closed is False
    if file.name!='benchmark-template.csv':
        assert rows, f'{file} is empty'
for file in (root/'examples').glob('*.html'):
    text=file.read_text()
    assert '<!doctype html>' in text.lower()
    assert '<title>' in text.lower()
print('Validated JSON, CSV, and HTML examples.')
