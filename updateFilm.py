from connection import *
from readFilms import *

def updateFilm():

    filmID = int(input("Enter the film ID of the film you wish to update. "))
    cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {filmID}")

    foundFilm = cursor.fetchone()

    if foundFilm:
        chosenField = input(f"""What do you want to update with film \"{foundFilm[1]}\"?
        Enter 'title', 'Yearreleased', 'rating', 'duration' or 'genre' """).title()

        if chosenField in ['Title', 'Rating', 'Genre']:

            fieldValue = input(f"Enter the new value for {chosenField} to be updated to for Film ID {filmID}: ")
            cursor.execute(f"UPDATE tblFilms SET {chosenField} = \'{fieldValue}\' WHERE filmID = {filmID}")
            completeUpdate(filmID)

        elif chosenField in ['Yearreleased', 'Duration']:

            fieldValue = int(input(f"Enter the new value for {chosenField} to be updated to for Film ID {filmID}: if updating duration, please enter the duration in minutes "))
            cursor.execute(f"UPDATE tblFilms SET {chosenField} = {fieldValue} WHERE filmID = {filmID}")
            completeUpdate(filmID)

        else:
            print(f"That category does not exist. {foundFilm[1]} (Film ID: {filmID}) has not been updated")
    
    else:
        print("That Film ID does not exist, no films have been updated")

def completeUpdate(filmID):
        connection.commit()
        read()
        print(f"Film ID: {filmID} has been updated")

if __name__ == "__main__":
    updateFilm()