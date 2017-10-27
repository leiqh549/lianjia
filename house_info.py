import sys
import re
import csv
import requests
from bs4 import BeautifulSoup

page_num = ['pg', 1]

def get_bsobj(url):
    page = requests.get(url)# .text

    if page.status_code == 200:
        html = page.text
        bs4obj = BeautifulSoup(html)
