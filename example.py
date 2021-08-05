import requests
from bs4 import BeautifulSoup

### 코드를 작성하세요 ###
res =requests.get("https://workey.codeit.kr/ratings/index")
soup = BeautifulSoup(res.text, 'html.parser')
program_title_tags = soup.select_one('img')['src']
print(program_title_tags)
