# 수학계산
import math
# 랜덤숫자
import random
# 날짜
import datetime
# 시스템 경로
import os.path as path
# 정규식
import re
# 객체를 바이트 변경
import pickle

# DB 컨트럴
import sqlite3

# json
import json

print(random.random())
print(int(random.uniform(0,5)))
print(random.randint(0,10))

# 절대 경로
print(path.abspath('..'))

# 주어진 경로의 현재 디렉토리 기준으로 한 상대 경로
print(path.relpath('C:/Users/ycd633/IdeaProjects/python'))

# 합치기
print(path.join('C:\\Users\\ycd633\\IdeaProjects\\python', 'test'))

# Regular Expression
pattern = re.compile('^[A-Za-z]+$')

obj = {'my': 'test'}

with open('test.pickle', 'wb') as f:
    pickle.dump(obj, f)
with open('test.pickle', 'rb') as f:
    obj = pickle.load(f)

conn = sqlite3.connect('database/employee.db')
sql = conn.cursor()
conn.execute('CREATE TABLE TEST (ID INTEGER , NAME MESSAGE_TEXT )')





conn.commit()
conn.close();

# rows = c.fetchall()
# for row in rows:
#     print(row)









