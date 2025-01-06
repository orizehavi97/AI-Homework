import sqlite3
import os

if os.path.exists("hw_solution.db"):
    os.remove("hw_solution.db")

conn = sqlite3.connect("hw_solution.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

create_query = "CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER);"
cursor.execute(create_query)

insert_query = "INSERT INTO shopping VALUES (1, 'Avokado', 5);"
cursor.execute(insert_query)
insert_query = "INSERT INTO shopping VALUES (2, 'Milk', 2);"
cursor.execute(insert_query)
insert_query = "INSERT INTO shopping VALUES (3, 'Bread', 3);"
cursor.execute(insert_query)
insert_query = "INSERT INTO shopping VALUES (4, 'Chocolate', 8);"
cursor.execute(insert_query)
insert_query = "INSERT INTO shopping VALUES (5, 'Bamba', 5);"
cursor.execute(insert_query)
insert_query = "INSERT INTO shopping VALUES (6, 'Orange', 10);"
cursor.execute(insert_query)

select_query = "SELECT * FROM shopping"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
print()

select_query = "SELECT * FROM shopping WHERE amount > 5"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
print()

delete_query = "DELETE from shopping WHERE name like 'Orange';"
cursor.execute(delete_query)

update_query = "UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'"
cursor.execute(update_query)

update_query = "UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'"
cursor.execute(update_query)

select_query = "SELECT COUNT(*)from shopping"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
print()

select_query = "SELECT * FROM shopping WHERE id > 0"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
print()

conn.close()
