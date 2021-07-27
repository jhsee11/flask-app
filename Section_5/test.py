import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
try:
  create_table = "CREATE TABLE users (id int, username text, password text)"
  cursor.execute(create_table)
except:
  print("nth")


user = (1,'jose','asdf')
insert_query = 'INSERT INTO users VALUES (?,?,?) '
cursor.execute(insert_query,user)

users = [
    (2,'rolf','asdf'),
    (3,'anne','xyz')
]

cursor.executemany(insert_query,users)

select_query = "SELECT id,username,password FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
