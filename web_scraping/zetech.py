#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import csv
import os
import time
import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

URL = 'https://shahada.zetech.ac.ke/index.php?mod=graduands#search-panel'

def scrape_graduands():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    # Finding the table containing the graduands' data
    table = soup.find('table')

    # Extracting the table rows (tr tags)
    rows = table.find_all('tr')

    # Checking if the CSV file already exists
    file_exists = os.path.isfile('graduands_list.csv')

    # Opening the CSV file in append mode
    with open('graduands_list.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Writing the header only if the file does not exist
        if not file_exists:
            writer.writerow(['No', 'Fullname', 'Adm No', 'Program', 'Classification', 'Year', 'Scraped Date'])
        
        # Writing each row of data
        for row in rows[1:]:  # Skip the first row if it's the header
            cols = row.find_all('td')
            if len(cols) > 0:
                # Adding the current date and time when the data is scraped
                data = [col.text.strip() for col in cols]
                data.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                writer.writerow(data)
    
    print("New data has been appended to graduands_list.csv")

# Running the scraper in a loop with a delay
while True:
    scrape_graduands()
    # Sleep for 24 hours (86400 seconds)
    time.sleep(86400)
