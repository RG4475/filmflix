from connection import *
from readFilms import *

def readReports():
    readoption = 0

    while readoption not in ["1", "2", "3", "4", "5"]:

        print("Film reports menu. Enter \n 1. Print all films \n 2. Print films of a particular genre \n 3. Print films released in a particular year \n 4. Print films with a particular rating \n 5. Exit")

        readoption = input("Enter an option from the menu ")

        if readoption not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please select from options menu ")
        
    return readoption

def printReports(films, noReturnMsg):

    if not films:
        print(f"No films have been returned {noReturnMsg}")
    else:
        for returned in films:
            print(returned)

readprogram = True

while readprogram:
    selected = readReports()

    if selected == "1":
        read()
    
    elif selected == "2":
        genre = input("Enter the genre of films you want to read ").title()
        cursor.execute(f"SELECT title, yearReleased, rating, duration FROM tblFilms WHERE genre = \'{genre}\'")

        filmsReturned = cursor.fetchall()
        noGenre = "that are of that particular genre"

        printReports(filmsReturned, noGenre)

    elif selected == "3":
        year = int(input("Enter the year to see all films that were released in that year "))
        cursor.execute(f"SELECT title, rating, duration, genre FROM tblFilms WHERE yearReleased = {year}")

        filmsReturned = cursor.fetchall()
        noYear = "that were released in that year"

        printReports(filmsReturned, noYear)

    elif selected == "4":
        rating = input("Enter the suitability rating to see all films that have that suitability rating ").upper()
        cursor.execute(f"SELECT title, yearReleased, duration, genre FROM tblFilms WHERE rating = \'{rating}\'")

        filmsReturned = cursor.fetchall()
        noRating = "that have that suitability rating"

        printReports(filmsReturned, noRating)
    
    else:
        readprogram = False

