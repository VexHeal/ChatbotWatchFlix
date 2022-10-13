import sqlite3

# conn = sqlite3.connect('E:/Anaconda/envs/py38_rasa/rasa0/actions/rasa.db')
# cursor = conn.cursor()
#
# createSql = "create table movies (name text primary key,years id)"
# cursor.execute(createSql)
#
# conn.commit()
#
# conn = sqlite3.connect("rasa.db")
# c = conn.cursor()
# c.execute("insert into movies(name,years) values('She:hulk', 2022)")
# c.execute("insert into movies(name,years) values('007:No time to die', 2021)")
# conn.commit()
# conn = sqlite3.connect("rasa.db")
# c = conn.cursor()
#
# movies_list = "select name from movies"
# c.execute(movies_list)
# conn.commit()
#
# result = [''.join(i) for i in c.fetchall()]
# strings = '\n'.join(result)
# print(strings)

# coon = sqlite3.connect("E:/Anaconda/envs/py38_rasa/rasa0/actions/rasa.db")
# c = coon.cursor()
#
# Movies_name = "She:hulk"
#
# movies_search = "select name from movies where name = ?"
# c.execute(movies_search, (Movies_name,))
# coon.commit()
#
# result = c.fetchone()
# # print(result[0])
#
# if result == None:
#     print(f'sorry, {Movies_name} is not on Wtachflix')
# else: