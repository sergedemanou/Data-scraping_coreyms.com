from urllib import response
from webbrowser import get
from requests import get
import requests

import csv

from bs4 import BeautifulSoup

url ='http://coreyms.com'

response = get(url)

#print(response.status_code)

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

articles = soup.findAll('article')

csv_file = open('Expert_Scraper.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Headline', 'Summary', 'Video_link'])

for article in articles:
    try:
        headline = article.header.h2.a.text
        print(headline)
    except Exception as e :
        headline ="none"
    
    try:
        summary = article.find('div', class_='entry-content').p.text
        print(f"{summary}\n")
    except Exception as e :
        summary ="none"
    
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id =vid_src.split('/')[4]
        vid_id =vid_id.split('?')[0]

        yt_lk = f'https://youtube.com/watch?v={vid_id}'
        print(yt_lk)
    except Exception as e :
        yt_lk ="none"
    
    print()

    csv_writer.writerow([headline, summary, yt_lk])

csv_file.close()