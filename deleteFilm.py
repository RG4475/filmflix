from connection import *
from readFilms import *

def deleteFilm():
    filmID = int(input("""Enter the film ID of the film you wish to delete. 
Print all the films first if you want to find the ID of the film you wish to delete
    """))

    cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {filmID}")
    connection.commit()

    read()

    print(f"Film with ID {filmID} has been deleted")

if __name__ == "__main__":
    deleteFilm()