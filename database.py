import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    # `with` commits the query after execution
    with connection:
        connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date))

def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor