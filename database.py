import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    # `with` commits the query after execution
    with connection:
        connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES ('This is some test content', '2020-01-01');")

def get_entries():
    pass