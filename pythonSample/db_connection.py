import sqlite3
from method import databaseUtils as ut


flag = ut.isTableExists('database/user_info.db', 'USER_INFO2')
print(flag)

# conn = sqlite3.connect('database/user_info.db')
# cur = conn.cursor()
# flag = cur.execute('select name from sqlite_master where type="table" and name = "USER_INFO2"')
# print(cur.fetchone())
# print(flag)
# for row in flag:
#     print(row)
#
#
# conn.close()

# conn = sqlite3.connect('database/user_info.db')
# conn.execute('CREATE TABLE USER_INFO (ID INTEGER , NAME MESSAGE_TEXT , EMAIL_ADDR MESSAGE_TEXT )')
# cur = conn.cursor()
# cur.executemany(
#     'INSERT INTO USER_INFO VALUES (?,?,?)',
#     [
#         (1, '양창덕', 'ycd633@nineonesoft.com'),
#         (2, '김해솔', 'ycd633@nineonesoft.com'),
#         (3, '김다솜', 'ycd633@nineonesoft.com'),
#     ]
# )
#
# conn.commit()
# conn.close()


# conn = sqlite3.connect('database/user_info.db')
# cur = conn.cursor()
# cur.execute('SELECT * FROM USER_INFO WHERE ID = 2')
#
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# conn.close()