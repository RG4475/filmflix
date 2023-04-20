from connection import *

def searchForFilm():
    searchTerm = input("Enter film name to search for: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE title LIKE \"%{searchTerm}%\" ORDER BY title")

    returnedFilms = cursor.fetchall()

    if returnedFilms:
        for film in returnedFilms:
            print(f"{film[1].upper()}: Film ID: {film[0]} Year Released: {film[2]} Rating: {film[3]} Duration: {film[4]}mins Genre: {film[5]}")
    else:
        print("That Film does not exist")

if __name__ == "__main__":
    searchForFilm()