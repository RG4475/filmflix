from connection import *

def read():
    cursor.execute("SELECT * FROM tblFilms")

    records = cursor.fetchall()

    for record in records:
        print(record)

if __name__=="__main__":

    read()