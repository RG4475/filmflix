from connection import *
from readFilms import *

def addFilm():

    film = []

    title = input("Enter film name: ")
    yearReleased = int(input("Enter the year, the film was released: "))
    rating = input("Enter the suitability rating of this film: ")
    duration = int(input("Enter how long this film is in minutes: "))
    genre = input("Enter the genre of this film: ")

    if rating in ["G", "PG", "R"]:
        
        film.extend([title, yearReleased, rating, duration, genre])

        cursor.execute("INSERT INTO tblFilms(title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", film)

        connection.commit()

        print(f"{title} has been added to the films table")

        read()
    else:
        print("Please enter G, PG or R for film suitability rating")

if __name__ == "__main__":
    addFilm()