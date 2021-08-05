import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
wb = Workbook(write_only=True)

ws = wb.create_sheet('TV Ratings')
ws.append()

res = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = res.text

# HTML 정리
soup = BeautifulSoup(rating_page, 'html.parser')

# 특정 태그 가져오기
program_title_tags = soup.select('td.program')


#print(soup.select('td')[:4])

#print(soup.select('td'))

tr_tag = soup.select('tr')[1]
td_tags = tr_tag.select('*')

for tag in td_tags:
    ws.append()


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


