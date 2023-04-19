import readFilms
import addFilm
import deleteFilm
from updateFilm import *
from reports import *

def menuSelect():
    option = 0

    while option not in ["1", "2", "3", "4", "5", "6"]:

        print("Films database menu. Enter \n 1. Print all films \n 2. Add a film \n 3. Update a film \n 4. Delete a film \n 5. Film Reports \n 6. Exit ")

        option = input("Enter an option from menu ")

        if option not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please select from options menu ")
    
    return option

program = True

while program:
    selected = menuSelect()

    if selected == "1":
        readFilms.read()
    elif selected == "2":
        addFilm.addFilm()
    elif selected == "3":
        updateFilm()
    elif selected == "4":
        deleteFilm.deleteFilm()
    elif selected == "5":
        runReportsFile()
    else:
        program = False

input("Press enter to quit")