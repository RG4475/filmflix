import sqlite3 as sql

connection = sql.connect("filmflix.db")

cursor = connection.cursor()