from connection import *
from readFilms import *

def deleteFilm():
    filmID = int(input("Enter the film ID of the film you wish to delete "))

    cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {filmID}")

    foundFilm = cursor.fetchone()

    if foundFilm:
        confirmDelete = input(f"Your chosen film to delete is \"{foundFilm[1]}\" is this correct? Enter Y for Yes or anything else for No ").upper()
        
        if confirmDelete == "Y":
            cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {filmID}")
            connection.commit()

            read()

            print(f"{foundFilm[1]} has been deleted")
    
        else:
            print("The film was not deleted")
    else:
        print("That Film ID does not exist, no films have been deleted")


if __name__ == "__main__":
    deleteFilm()