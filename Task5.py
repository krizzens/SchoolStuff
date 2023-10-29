

""" data = [[1, 2, 3, 4, 5, 6],

        [7, 8, 9, 10, 11, 12],

        [13, 14, 15, 16, 17, 18]]

Create a Python script that will check if a file the_file.csv exists.  If it does, then the entries in the list should be appended to the file.  If the file does not exist, it should be created and the data added to the file.  

Each of the 3 entries in the list should be added as a single line and the entries in the line should be separated by commas.  Your text file should contain no square brackets.  You can test whether your .csv file works by opening it in Excel or a similar spreadsheet manipulation package.  

The only import (except for any basic Python packages) you are allowed to make is for os.  Ensure that if any errors occur, an error message will be printed to the console window and that the file will always be closed; even if an error occurs, i.e. the file should always be closed after processing, no matter what happens. """





import os.path

from os import path


data = [

[1, 2, 3, 4, 5, 6],

[7, 8, 9, 10, 11, 12],

[13, 14, 15, 16, 17, 18],

 ]

datalist = ""

for a in data:
     for data in a:
         datalist += f"{data},\n"
        




def file_checker():
    while True:
        if os.path.isfile("the_file.csv"):
            print("The file already exist")

            q1 = input("Do you want to append new text to the file or write new text that will discards its previous contents? a for append and w for write: ")
    
            if q1.lower == "a":
                my_file = open("the_file.csv" , "a")
                my_file.write(str(datalist))
                my_file.close() 
                break

            elif q1 == "w":
                my_file = open("the_file.csv" , "w")
                my_file.write(str(datalist))
                my_file.close()
                break



        else: 
            print("The file does not exist")
            q2 = input("Do you want do create the file? y for yes or n for no: ")
            my_file = open("the_file.csv" , "w")

      
file_checker()

