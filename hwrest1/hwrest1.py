from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

# connector
db_name: str = "hwrest1.db"
conn = sqlite3.connect(db_name, check_same_thread=False)  # creates a connector
conn.row_factory = sqlite3.Row  # allow me to use column name

# cursor
cursor = conn.cursor()  # creates a cursor


def execute_modify_query(_cursor, _conn, query) -> None:
    """Execute a modify query (insert, update, delete)"""
    _cursor.execute(query)
    _conn.commit()


def execute_read_query(_cursor, query) -> list:
    """Execute a read query (select)"""
    _cursor.execute(query)
    _rows = _cursor.fetchall()
    _answer = []
    for _row in _rows:
        _answer.append(dict(_row))
    return _answer


# GET all
@app.get("/messages")
def get_messages():
    return execute_read_query(cursor, "SELECT * FROM messages;")


# GET by id
@app.get("/messages/{id}")
def get_message(id: int):
    result = execute_read_query(cursor, f"SELECT * FROM messages WHERE id = {id};")
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Message not found")


# POST (create new)
@app.post("/messages")
def create_message(text: str):
    execute_modify_query(cursor, conn, f"INSERT INTO messages (text) VALUES ('{text}');")


# PUT (replace or create)
@app.put("/messages/{id}")
def put_message(id: int, text: str):
    result = execute_read_query(cursor, f"SELECT * FROM messages WHERE id = {id};")
    if result:
        execute_modify_query(cursor, conn, f"UPDATE messages SET text = '{text}' WHERE id = {id};")
    else:
        execute_modify_query(cursor, conn, f"INSERT INTO messages (id, text) VALUES ({id}, '{text}');")


# PATCH (update only if exists)
@app.patch("/messages/{id}")
def patch_message(id: int, text: str):
    result = execute_read_query(cursor, f"SELECT * FROM messages WHERE id = {id};")
    if result:
        execute_modify_query(cursor, conn, f"UPDATE messages SET text = '{text}' WHERE id = {id};")
    else:
        raise HTTPException(status_code=404, detail="Message not found")


# DELETE
@app.delete("/messages/{id}")
def delete_message(id: int):
    result = execute_read_query(cursor, f"SELECT * FROM messages WHERE id = {id};")
    if result:
        execute_modify_query(cursor, conn, f"DELETE FROM messages WHERE id = {id};")
    else:
        raise HTTPException(status_code=404, detail="Message not found")
