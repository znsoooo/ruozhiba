import re
import json

load = lambda file: json.load(open(file, encoding='u8'))


with open('data/ruozhiba-post-annual.txt', 'w', encoding='u8') as f:
    for row in load('data/ruozhiba-post-annual.json'):
        text = re.match(r'(?:\d+.)?(.*)', row['content']).group(1)
        f.write(text + '\n')


with open('data/ruozhiba-title-good.txt', 'w', encoding='u8') as f:
    for row in load('data/ruozhiba-title-good.json'):
        title, abs = row['title'], row['abs']
        abs = '' if abs is None else abs.strip()
        title = title + '。' if abs != title else title
        abs = '' if abs == title else abs
        if '\n' not in abs and '\r' not in abs:
            f.write(title + abs + '\n')
