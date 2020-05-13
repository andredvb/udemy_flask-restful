import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = """CREATE TABLE users (
    id int,
    username text,
    password text
)"""
cursor.execute(create_table)

user = (1, 'jose', 'adsf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'andre', 'iasj'),
    (3, 'ppl', 'asdf')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
select = cursor.execute(select_query)
[print(x) for x in select]

connection.commit()

connection.close()