import sqlitelib

db_name: str = "080125db.db"
conn, cursor = sqlitelib.connect_db(db_name)

# Ex 4
select_query = "SELECT * from courses"
result_select_products = sqlitelib.read_query(cursor, select_query)
for item in result_select_products:
    print(item)

# Ex 5
course_topic = input('enter new course topic? ')
course_hours = int(input('enter new course hours? '))

select_query = "SELECT topic from courses WHERE topic = ?"
result_select_products = sqlitelib.read_query_params(cursor, select_query, (course_topic,))

# if a course does not exist, add it.
if not result_select_products:
    sqlitelib.update_query(
        cursor, conn,
        "INSERT INTO courses (topic, hours) VALUES (?, ?)",
        (course_topic, course_hours))
else:
    print("Course already exists")

conn.close()
