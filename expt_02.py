from bs4 import BeautifulSoup
import requests
import re

# Printing the HTML file from the specified URL
html_text = requests.get('https://arstechnica.com/').text
# print(html_text)

# Extracting the hyperlinks from the page
soup = BeautifulSoup(html_text, 'lxml')

headers = soup.find_all('header')

for head in headers:
    print(head.a['href'])