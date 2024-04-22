import re

from datetime import datetime

def extract_info(s):
    pattern = r'\[(\d{2}\.\d{2}\.\d{2}), (\d{2}:\d{2}:\d{2})\] (\w+): (.*)'
    match = re.search(pattern, s)
    if match:
        date_str = match.group(1)
        time_str = match.group(2)
        date_obj = datetime.strptime(date_str, '%d.%m.%y').date()
        time_obj = datetime.strptime(time_str, '%H:%M:%S').time()
        datetime_obj = datetime.combine(date_obj, time_obj)
        return {
            'datetime': datetime_obj,
            'author': match.group(3),
            'message': match.group(4).replace('"', '""'),
            'interessant': 'interessant' in match.group(4).lower()
        }
    else:
        return None

data = []

with open('_chat.txt', 'r') as f:
    for line in f:
        data.append(extract_info(line))

# csv output
with open('_chat.csv', 'w') as f:
    f.write('datetime,author,message,interessant\n')
    for item in data:
        if item:
            f.write(f"{item['datetime'].isoformat()},{item['author']},\"{item['message']}\",{item['interessant']}\n")