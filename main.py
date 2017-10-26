import sys
import csv
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

ershoufang = "/ershoufang/"

def get_city_dict():
    city_dict = {}

    with open("citys.csv", "r") as f:
        reader = csv.reader(f)
        for city in reader:
            city_dict[city[0]] = city[1]
    return city_dict

def get_district_dict(url):
    district_dict = {}
    html = requests.get(url).text
    bs4obj = BeautifulSoup(html, "html5lib")
    roles = bs4obj.find("div", {"data-role": "ershoufang"}).findChildren("a")
    for role in roles:
        district_url = role.get("href")
        district_name = role.get_text()
        district_dict[district_name] = district_url

    return district_dict


def run():

    city_dict = get_city_dict()
    print("目前支持的城市: ", city_dict.keys())
    input_city_name = input("请输入城市: ")

    city_url = city_dict.get(input_city_name)
    if city_url:
        print(input_city_name, city_url)
        ershoufang_city_url = urljoin(city_url, 'ershoufang')
        district_dict = get_district_dict(ershoufang_city_url)

        # for district in district_dict.keys():
        print('目前支持的地区: ', district_dict.keys())

        input_district = input('输入地区: ')
        district_url = district_dict.get(input_district)


        if not district_url:
            print("输入错误")
            sys.exit()
        house_info_url = urljoin(ershoufang_city_url, district_url)
        print(house_info_url)


    else:
        print("输入错误")
        a = input()
        sys.exit()

if __name__ == '__main__':
    run()

# city_dict = get_city_dict()



# for city_name in :


