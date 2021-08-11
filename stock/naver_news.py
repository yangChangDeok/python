import requests
from bs4 import BeautifulSoup


def real_news():
    row_cnt = requests.get("https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258")
    row_html = BeautifulSoup(row_cnt.text, 'html.parser')
    page = row_html.select_one('.pgRR a').attrs['href']
    cnt = int(page[len(page) - 2:])
    arrayList = []
    for tidx in range(1, cnt):
        url = "https://finance.naver.com/news/news_list.nhn?mode=LSS2D&section_id=101&section_id2=258&page={}".format(tidx)
        res = requests.get(url)
        html = BeautifulSoup(res.text, 'html.parser')
        title = html.select('.articleSubject')
        summary = html.select('.articleSummary')

        row = len(title)
        titles = []
        for s in title:
            titles.append(list(s.stripped_strings))

        summarys = []
        for s in summary:
            summarys.append(list(s.stripped_strings)[0])

        for idx in range(0, row):
            arrayList.append([titles[idx], summarys[idx]])

    return arrayList
