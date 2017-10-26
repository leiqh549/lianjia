import csv
import requests

from bs4 import BeautifulSoup

url = "https://cd.lianjia.com/"

html = requests.get(url).text

bsobj = BeautifulSoup(html, "html5lib")

city_tags = bsobj.find("div", {"class": "fc-main clear"}).findChildren("a")


def write_city():
# print(city_tags)
    with open("./citys.csv", "w") as f:
        writ = csv.writer(f)
        for city_tag in city_tags:
            city_url = city_tag.get("href")
            city_name = city_tag.get_text()
            writ.writerow((city_name, city_url))
            print((city_name, city_url))

if __name__ == '__main__':
    write_city()