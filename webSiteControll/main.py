import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


# program_title_list = []
# for tag in program_title_tags:
#     #print(tag.get_text())
#     program_title_list.append(tag.get_text())



# get_text() / strings / stripped_strings
music = requests.get("https://workey.codeit.kr/music")
rating_pages = music.text

mosic_page = BeautifulSoup(rating_pages, 'html.parser')


# get_text() / strings / stripped_strings
for tag in mosic_page.select('ul.popular__order li'):
    #print(list(tag.strings))
    #print(list(tag.stripped_strings))
    print(list(tag.stripped_strings)[1])


