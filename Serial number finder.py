import os
import re
from pathlib import Path
from datetime import datetime
import time
from math import ceil

def today_date():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y")
    return date_time


today = today_date()
print(f"Search date: {today}")
print("--------------------------------\nFile        SERIAL NO.")
print("----        ----------")
path = 'C:\\Users\\Stan\\Desktop\\Python\\Day_9_Project\\My_Big_Directory'
def serial_number(path):
    start_time = time.time()
    numbers_found = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                filepath = Path(os.path.join(root, file))
                text_string = filepath.read_text()
                search = re.findall(r'N\D{3}-\d{5}', text_string)
                if search:
                    joined = ''.join(search)
                    print(f'{file}   {joined}')
                    numbers_found += 1
    print(f"\nNumbers found: {numbers_found}")
    print(f"Search duration: {ceil(time.time() - start_time)}")
serial_number(path)
print("--------------------------------")


