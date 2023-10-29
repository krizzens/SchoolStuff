
# Lage virtual environment 
# python –m venv .venv 


""" 1.4. Lesson task - Basic programing and debugging """

# 3)
# Create a script called Output4Values.py. Ask the user to input four different string values. Your program needs to store the values in four different variables. 
# Output these values to screen using a single print statement. The print statement needs to do the following:
# Separate the values using a semi-colon.
# Automatically add the statement ". Output complete!" to the end of the print() output.
# Not move the cursor to the following line after performing the output.






# a1 = input("Enter a City: ")
# a2 = input("Enter a Country: ")
# a3 = input("Enter a fruit: ")
# a4 = input ("Enter a color: ")




# print(a1, a2, a3, a4, "Output complete!", sep=":" )


"""  2.1. Lesson task - Data containers, lists and tuples

 ACTIVITY 1 """

# Create a script called ListTest.py. The script is required to do the following:
# Define a list.
# Request 10 names of friends from the user and save them in the list.
# Sort the list.
# Reverse the list.
# Ask the user for one more name.
# Append the name to the end of the original list.
# Display the contents of the original list.


# # Define a list and ask the user for 10 names
# list = []

# for i in range(10):
#     list.append(str(input("Please Enter a Name: ")))
    
# print(list)

# #  Sort the list
# list.sort()
# print("Sorted list:", list)

# # Reverse the list
# list.reverse()
# print("Reversed list:", list)


# # Ask the user for one more name and append it to the end of the original list
# list_name =(str(input("Please Enter a Name:")))

# list.append(list_name)
# print("List with the new name:", list)

# # Display the content of the original list without the newly added name
# list.pop()

# print("Original list:", list)





"""ACTIVITY 2"""

# Create a script called SetTest.py. The script is required to do the following:
# Define a set.
# Populate the set with the names of your five favourite fast foods (no user input required).
# Define a second set and populate it with the names of a friend’s five favourite fast foods (no user input required).
# Add another type of fast food to your set of favourite foods.
# Determine which favourite fast foods are shared by you and your friend and display these overlapped foods.

# food = {"Pizza", "Taco", "Burger", "Fisk", "Kebab"}
# print("My original list:", food)

# food_friend = {"Pizza", "Fisk", "Suppe", "Kake", "Taco"}
# print("Friends original lsit", food_friend)


# food.add("Pudding")
# print("My list after adding another food", food)

# print("Shared favourite fast foods", food.intersection(food_friend))





"""ACTIVITY 3"""

# Create a script called MyPhonebook.py The script is required to do the following:
# Define a dictionary consisting of five business names and their associated phone numbers. The business name should be used as the key.
# Request the name and number of another business from the user and add it to the dictionary.
# Ask the user to type in the name of a business that is in the list. Display the result to the user.
# Display the entire dictionary (names and phone numbers).
# Display only the business names (no phone numbers).


# # Create a dictionary
# phonebook = {"Apple":1234, "Finn":5678, "Noroff":666, "Skyss":1010, "Samsung":9090}

# # Ask the user to type in a new business and number
# new_business = str(input("Enter a new business here: "))
# new_number = int(input("Enter a new number here: "))

# # Ask the user to type in the name of a business in the list and display the result
# user_input = input("Enter the name of a business her: ")
# print(phonebook[user_input])

# # Add the user input into the dictionary
# phonebook[new_business] = new_number

# # Display the entire dictionary
# print(phonebook)

# # Display only the business names
# print ("Only the keys:", phonebook.keys())





""" 2.3. Lesson task - Managing string (part 1) """


# 1)

# Given the below variable and string assignment, 
# use it in your Python script and print the indexes in the following order 16,15,4,17,6,12,11,18. 
# You must use the Python split() function to split the string.
# strMessage = "what,is,not,good,I,will,be,you,ok,Noroff,student,Python,a,awesome,pretty,knew,who,would,programmer"




# strMessage = "what,is,not,good,I,will,be,you,ok,Noroff,student,Python,a,awesome,pretty,knew,who,would,programmer"

# # Split the string at every "," to make it a list with index numbers
# newString = strMessage.split(",")


# # print the asked words using the index number
# print(newString[16], newString[15], newString[4], newString[17],newString[6], newString[12], newString[11], newString[18])




# 2)

# Create a script that will underline any length of a string. Use the below string as a start. Only 1 “-“ can be used for the print function.
# strUnderline = "This sentence must be underlined"
# If you change the string, the print function should underline the new string without you needing to change the print function. 
# The script should print the string and then print the “-“ characters underneath the string, to the same length as the original string.   



# strUnderline = "This sentence must be underlined"

# # Underlined the string
# print(strUnderline, "\n", "-"*30)





# 3)

# Use the below string, and create a Python script that will change the delimiter from a space to a 
# 1) semicolon (;) 2) a comma (,) and 3) the pipe character (|).
# “Change my delimiter”


# string_test = "Change my delimiter"


# # Use the "replace()" function to replace spaces with ";"
# print(string_test.replace(" ", ";"))

# # Use the "replace()" function to replace spaces with ","
# print(string_test.replace(" ", ","))

# # Use the "replace()" function to replace spaces with "|"
# print(string_test.replace(" ", "|"))



# 4)

# Write a Python script that will replace the word 'good' with 'great', and 'bad' with 'perfect' in a string. 
# Ask the user for input, perform the replacement and then output the modified string.



# sentence1 = "This is a good sentence"
# sentence2 = "This is a bad sentence"

# print("This is the original first sentence: ", sentence1)
# print(sentence1.replace("good", "great"))


# print("This is the original second sentence: ", sentence2)
# print(sentence1.replace("bad", "perfect"))



""" 2.4. Lesson task - Managing string (Part 2) """

"""ACTIVITY 1"""

# Create a script named splitandjoin.py.
# Prompt the user to enter a string of text.
# Ask the user for a character on which to split their text.
# Use this character to split their initial string.
# Request text from the user to use in order to re-combine the string.
# Display the re-combined string to the user.

# user_input1 = str(input("Enter a string her: "))
# user_input2 = str(input("Enter a character on wich to split: "))

# # Create a new varable wich holds the new splitted string
# new_string = user_input1.split(user_input2)
# print("This is the new string after split", new_string)

# # Ask the user to re-combine the string with a character
# user_input3 = str(input("Enter a character on wich to re-combine the string: "))
# print(user_input3.join(new_string))



"""ACTIVITY 2"""

# Create a script named editor.py. In this script, prompt the user to enter a string of text. 
# The following needs to happen:

# 1. Display the length of the string.
# 2. Ask the user for an index in the string.
# 3. Display the string entered by the user, BUT add single quotes (“) around the word *of the index* that the user entered on the previous option.

#  Example:

# String: This is the test string
# User word: is
# Result to be printed: String length: 22
# Word index: 1
# Display string: This “is” the test string


# string = "This is the string"

# # Print out the length of the original string
# print("Length of the original string: ",len(string))

# # Split the string to make the words in the string into a list
# split_string = string.split(" ")
# print(split_string)

# # print the lenght of the splitted string
# print("Length of the splitted string", len(split_string))

# # Make the user enter an index to output a word
# string_input = int(input("Enter a index here: "))

# # Print out the word from the user input
# print(split_string[string_input])



# string_list = string.split(" ") 
# string_list.insert(string_input, "\"")
# string_list.insert(string_input - 1, "\"")

# print(string_list)

# print(" ".join(string_list))





""" 3.1. Lesson task - Performing operations (part 1) """

"""1)"""

# Create a script called CalculateVolume.py. An engineer wants to calculate the volume of a rectangular tank using the formula length width height. 
# The program needs to request these three values as input from the user and store them in three different variables. 
# Using these three variables, calculate the volume of the tank and store it in a fourth variable. 
# The engineer has learned from experience that measurements and calculations are always a bit short of the volume the tank can store because the plastic tank expands when filled. 
# Therefore, he requires that the script increase the calculated volume of the tank by 1% before displaying the resulting volume to the user.


# # Float to let the user enter numbers with decimals
# length = float(input("Enter length here: "))
# width = float(input("Enter width here: "))
# height = float(input("Enter height here: "))

# # Calculate the volume and add 1%
# volume = (length*width*height) + (length*width*height*0.01)

# print("Here is the volume of the tank: ", volume)



"""3)"""

# Create a script called PizzaShop.py. A pizza shop owner has asked you to write a script that allows a customer to calculate the cost of a pizza. He has asked you to make the following options available to the customer:
# Pizza base (Customer must choose 1): Thick (Kr 10) or Thin (Kr 5).
# Pizza size (Customer must choose 1): Small (Kr 30), Medium (Kr 40), or Large (Kr 50).
# Basic sauce (Customer must choose 1): Tomato (Kr 5) or Barbecue (Kr 10).
# Toppings (Customer may choose any or none): Cheese (Kr 5), Mushrooms (Kr 3), Avocado (Kr 7), Pineapple (Kr 5), Bacon (Kr 7), Chicken (Kr 7) or Fish (Kr 6).
# If a specific item is selected, display the item and its price on the screen. At the bottom (the last line) of the display, present the customer with the purchase total.


# pizzabase = {"Thick":10, "Thin":5}
# pizzasize = {"Small":30, "Large":50}
# basicsauce = {"Tomato":5, "Barbecue":10}
# toppings = {"Cheese":5, "Bacon":7}



# sum = 0



# while True:
#     user_input1 = (input("Enter a pizzabase here: "))
#     if user_input1 == "Thick":
#         sum += (pizzabase["Thick"])
#         print(sum)
#         break
#     elif user_input1 == "Thin":
#             sum += (pizzabase["Thin"])
#             print(sum)
#             break
#     else:
#         print(f"We dont have {user_input1} in our menu")


# while True:
#     user_input2 = (input("Enter a pizzasize here: "))
#     if user_input2 == "Small":
#         sum += (pizzasize["Small"])
#         print(sum)
#         break
#     elif user_input2 == "Large":
#             sum += (pizzasize["Large"])
#             print(sum)
#             break
#     else:
#         print(f"We dont have {user_input2} in our menu")

# while True:
#     user_input3 = (input("Enter a basicsauce here: "))
#     if user_input3 == "Tomato":
#         sum += (basicsauce["Tomato"])
#         print(sum)
#         break
#     elif user_input3 == "Barbecue":
#             sum += (basicsauce["Barbecue"])
#             print(sum)
#             break
#     else:
#         print(f"We dont have {user_input3} in our menu")

# while True:
#     user_input4 = (input("Enter a toppings here: "))
#     if user_input4 == "Cheese":
#         sum += (toppings["Cheese"])
#         print(sum)
#         break
#     elif user_input4 == "Bacon":
#             sum += (toppings["Bacon"])
#             print(sum)
#             break
#     else:
#         print(f"We dont have {user_input4} in our menu")

# print("The toal cost is: ", sum)



""" 3.2. Lesson task - Performing operations (part 2) """

# Option 1: 
# The user needs to enter a number. The number needs to be assigned to a variable. If the number is equal to 543 then the application must print the words:
# “You guessed the number! It is 543” 
# If the number entered is lower than 543 then the application must print:
# “The number you entered is too low”
# If the number entered is higher than 543 then the application must print:
# “The number you entered is too high”


def guess_the_number():
    while True:
        q1 = int(input("Enter a number here: "))
        if q1 == 543:
                print("You guessed the number! It is 543")
                break
        elif q1 < 543:
                print("The number you entered is too low!")
        elif q1 > 543:
                print("The number you entered is too high!")


#guess_the_number()


# Option2: 
# The end user must enter a time value, and you need to calculate if the value is in working hours, or outside of working hours. If the time entered is outside of working hours, then the application must print: 
# “Private time” 
# If the time entered is between 08:00 and 17:00 then the application needs to print: 
# “Inside working hours”

def calculate_time():
    while True:
        q2 = int(input("Enter a time value: "))
        if (q2 < 8) or (q2 > 17):
            print("Private time!")
            break
        else:
            if (q2 > 8) or (q2 < 17):
                print("inside working hours!")
                break

#calculate_time()




# Option 3: 
# The end user must enter a number between 0 and 3. For each number the application must print a message that is associated with that number from the given data container below: 
# message = [“Coding is fun”, “Python is not code, but a way of life”,”We learn Python the fun way”,”We code, because we can”] 
# If the user enters 2, the application must print the words: 
# "We learn Python the fun way"


def print_something():
    message = ["Coding is fun", "Python is not code, but a way of life","We learn Python the fun way","We code, because we can"] 
    
    while True:
        q3 = int(input("Enter a number between 0 and 3 here: "))
        if q3 < 3:
            print(message[q3])
            break
        elif q3 > 3:
                print("Thats a too high number!")


#print_something()




# Option 4: 
# Ask the user what number of the message data container they want to change. 
# The user needs to enter a number from 0 to 3, and then the application needs to ask what the text for that index should be.
# Once the text has been changed, the application must print the data container variable message to show that the text has been changed.



def change_a_print_option():
    message = ["Coding is fun", "Python is not code, but a way of life","We learn Python the fun way","We code, because we can"] 
    
    while True:
        q4 = int(input("Enter a number between 0 and 3 here to choose the value you want to change: "))
        if q4 < 3:
            print(message[q4])
            q5 = str(input("Enter a text you want insted here: "))
            print("This is the new text", q5)
            message[q4] = [q5] 
            print("This is the entire data container with the new text: ", message)
            break
        elif q4 > 3:
                print("Thats a too high number!")    

#change_a_print_option()



# MENU SYSTEM


# while True:
#     categories = {guess_the_number:1, calculate_time:2, print_something:3, change_a_print_option:4}
#     menu = int(input("""

#         *********************
#         Menu System
#         *********************

#         ---------------------
#         Guess the number        (1)

#         Calculate time          (2)    

#         Print something         (3)

#         Change a print option   (4)
#         ----------------------

#         What option would you like?
 
#         """))

#         #print(menu)

#     if menu == 1:
#         guess_the_number()
#         user1 = input("Do you want to continue? y or n: ")
#         if user1 == "y":
#             continue
#         else:
#             if user1 == "n":
#                 break
#     elif menu == 2:
#         calculate_time()
#         user1 = input("Do you want to continue? y or n: ")
#         if user1 == "y":
#             continue
#         else:
#             if user1 == "n":
#                 break
        
#     elif menu == 3:
#         print_something()
#         user1 = input("Do you want to continue? y or n: ")
#         if user1 == "y":
#             continue
#         else:
#             if user1 == "n":
#                 break
        
#     elif menu == 4:
#         change_a_print_option()
#         user1 = input("Do you want to continue? y or n: ")
#         if user1 == "y":
#             continue
#         else:
#             if user1 == "n":
#                 break
    



""" 3.3. Lesson task - Loops """

"""1)""" 
# Create a script called CalculateTotal.py. 
# The script should continuously ask a user to enter an integer value. 
# This should continue until the user has entered the value -1. 
# Once the loop has ended, print the total of all the values entered by the user (excluding -1).

        
# sum = 0

# while True:
#     user_input = int(input("Enter a value here from -1 to 10: "))

#     if user_input != -1:
#         sum += user_input   
#     elif user_input == -1:
#             print("This is the total sum: ", sum)
#             break



"""3)"""
# Create a script called PostalCodes.py. 
# Create a data structure able to store 10 postal codes with their associated residential areas. 
# Prompt the user to enter a postal code. If the postal code exists, output the residential area linked to the postal code.

# postcodes = {5057:"Bergen", 1411:"Oslo", 4567:"Stavanger", 6847:"Vassenden"}



# while True:
#     user_input2 = int(input("Enter a postal code here: "))
#     if user_input2 in postcodes:
#         print(postcodes[user_input2])
    
#     else:
#         print(f"{user_input2} is no a postal code in my data container")




"""3.4. Lesson task - Functions (part 1)"""

"""1)"""
# Create a script called MetricConverter.py. 
# In the script, create a function called metric_converter, which receives a single numeric argument. 
# The purpose of this method is to receive a value in inches and then convert it to centimetres. 
# The function should display the number of inches that it received and the number of centimetres after conversion. 
# The function shouldn't return any values. Demonstrate the use of the function in the main section of your script.

# def inches_to_cm():
#     inches = float(input("Enter a value in inches here to convert it to cm: "))
#     convert = inches * 2.54
#     print("Here is inches in cm: ", convert)

# def cm_to_inches():
#     cm = float(input("Enter a value in cm here to convert it to inches: "))
#     convert1 = cm * 0.3937007874
#     print("Here is cm in inches: ", convert1)


# while True:
#     user_input = int(input("what do you want to convert? (1) for inches to cm and (2) for cm to inches: "))
#     if user_input == 1:
#         inches_to_cm()
#         break
#     else:
#         if user_input == 2:
#             cm_to_inches()
#             break
                

"""2)"""
# Create a script called SummingMachine.py. In the script, create a function called summing_machine. The function should receive no argument. 
# It should continuously ask the user to enter a number until they enter a value to stop, e.g. 's'. 
# The values entered must be added together, and the final result returned to the calling code. 
# Demonstrate the use of the function in the main section of your script.

         
# sum = 0

# while True:
   
#     user_input2 = input("Do you want to add numbers(y) or stop the process(n): ")
#     if user_input2 == "y":
#         user_input1 = int(input("Enter a value here: "))
#         sum += user_input1
#     else: 
#         user_input2 == "n"
#         print("Total sum: ", sum)
#         break




"""4.1. Lesson task - Functions (part 2)"""

"""1)"""
# Create a script called GenerateLetter.py. In the script, create a function called generate_letter which is to serve as a generator function. 
# The generator should return a letter in the range a to e. 
# If the generator returns the letter e, it should return the letter a the next time the generator function object is used. 
# Demonstrate the use of the generator in the main portion of your script by display the letters a to e twice.
        
# GLENN sitt svar
'''
Create a script called GenerateLetter.py. 
Create a function called generate_letter which is to serve as a generator function. 
The generator should return a letter in the range a to e. 
If the generator returns the letter e, 
it should return the letter a the next time the generator function object is used. 
Demonstrate the use of the generator in the main portion of your script 
by display the letters a to e twice.
'''

# def generate_letter():
#     while True:
#         for letter in "abcde":
#             print(letter)
#             yield

# bokstav = generate_letter()

# x = 0
# while x < 10:
#     next(bokstav)
#     x += 1



"""4.2. Lesson task - Importing modules"""

# 1)
  
# Create a Python script called mymodules.py. In this script, create the following functions:
# create_time: This function should create a time object and return it.
# output_local_time: This function should receive a time object as a parameter and display the local_time associated with it.
# calculate_difference: This function should receive two objects, subtract them from each other and return the difference.
# generate_random: This function receives a maximum number as a parameter and then returns a random number between 0 and the maximum number.


# This is a function that tells you how much money you have earned using hours worked at what the hourly wage is
def create_time(hours_worked, hourly_wage):
    return hours_worked * hourly_wage


#print(create_time(7.5, 150))


# This function diplays the current time
# Link used to get current time https://www.programiz.com/python-programming/datetime/current-time¨

def output_local_time():

    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    

#output_local_time()


# This function subtract two items
def calculate_difference(num1, num2):
    return num1 - num2

#print(calculate_difference(10, 5))


# This function generates a random number
def generate_random(num):
    import random
    return random.randint(0, num)

#print ("Here is the random number: " , generate_random(10))



# 2)

# Create a second Python script called guessinggame.py. 
# In this script, you need to access the functions created in the mymodules.py script. 
# Furthermore, this script should present the user with a guessing game. The user should be prompted to guess a number between 0 and 10. 
# The system should then randomly generate a number between 0 and 10 using a function from mymodules.py. 
# If the user guessed correctly, display a congratulatory message. Otherwise, display a message stating the actual number and wish them luck for their next attempt. 
# The user should be able to play the game as many times as they want. 
# If the user has finished playing, the system should display a message stating how many seconds they played.


# # Her importerer eg inn ein modul som heite "time". Den er brukt for å ta tida på kor lang tid det tar for user til å gjette riktig tall.
# import time
# start = time.time()

# while True:
    
# # Dette programmet henter ut funksjonen "generate_random" som er lagret i "Module4_2_mymodules"
#     from Module4_2_mymodules import generate_random as gr
# # Her har eg gjort slik at "generate_random" funksjonen kan bli "snakka" til ved å kun bruke "gr". Det er også lagt inn "10" som vil sei at programmet genererer eit random tall fra 0-10
    
#     # Her lager eg ein variabel slik at man kan velge kor "generate_random" skal generere til. Står det 10 vil programmet generere eit tall frå 0-10.
#     num = 10

#     q1 = int(input("Guess a number between 0-10: "))
#     if q1 == gr(num):
#             print ("Correct! You win")
#             break

#     else:
#         print ("Try again! Wrong number entered")
#         print (f"Here was the correct number: {gr(10)}")
    
# end = time.time()
# duration = round(end - start,2)
# print("Time used: " + str(duration) + " seconds.")


# # Linken eg brukte for å bruke "time" modulen https://www.101computing.net/time-guessing-game/




"""4.3. Lesson task - Managing files"""

"""1)"""

# Open up a spreadsheet editor and create a CSV file called mycsv.csv. 
# Populate this file with data as you choose. 
# Create a script called csvreader.py. 
# Load the data from the mycsv.cvs file and display it to the user.

# # CSVreader

# # Open up a spreadsheet editor and create a CSV file called mycsv.csv. Using "w". 
# # my_file = open("mycsv.csv", "w")

# # Load the data from the mycsv.cvs file and display it to the user. Using "r"
# my_file = open("Module_4_3_mycsv.csv", "r")

# # print for å vise det som står i fila
# print(my_file.read())



"""2)"""

# Create a script called randomnumbers.py. 
# In the script, generate 100 random numbers in the range of 0 to 500. 
# Ask the user for a file name to which the random numbers should be saved. 
# Save the file to disk.

# A linked that helped with "range" https://www.tutorialspoint.com/generating-random-number-list-in-python

# # Her brukte eg ein rnadom generator funksjon som eg hadde lagd tideligere
# from Module4_2_mymodules import generate_random

# sum = 0
# the_random_list = []
# for i in range(100):
#     the_random_list.append(generate_random(500))
    
#     sum += 1

# print(the_random_list)
# print("Total numbers: ", sum)

# # Ask the user for a file name to which the random numbers should be saved
# q1 = input("Enter a filename on wich the random numbers should be saved: ")

# # Open the new file and "a" (append) the random number content to the file
# my_file = open(f"{q1}.csv" , "a")
# my_file.write(str(the_random_list))
# my_file.close()





# # NMAP Python module

# import nmap3, json

# nmap = nmap3.Nmap()
# # Put in the IP:adddress of your pc to see wich ports that are open
# results = nmap.scan_top_ports("10.53.100.212")

# print( json.dumps( results["10.53.100.212"]["ports"], indent=2) )

# # Information about NMAP https://pypi.org/project/python3-nmap/


# # NMAP mapping
# import nmap3

# ip_addresses = "10.53.100.212/24"

# nmap = nmap3.NmapScanTechniques()

# results = nmap.nmap_ping_scan(ip_addresses)

# #print (results.keys())

# for item in results:

#     if item not in ['runtime', 'stats', 'task_results']:

#         if results [item]['macaddress']:

#             print (item, results[item]['macaddress']['addr'], results[item]['state']['state'])



# Hashing Module 5


# import hashlib
# txtMessage = "Hello World"
# txtMessage = txtMessage.encode("utf-8")

# # Forskjellige krypterings metoder
# md5hash = hashlib.md5(txtMessage).hexdigest()
# sha256 = hashlib.sha256(txtMessage).hexdigest()
# sha512 = hashlib.sha512(txtMessage).hexdigest()

# print("MD5 : " + md5hash)
# print("SHA 256 : " + sha256)
# print("SHA 512 : " + sha512)




"""PRG Exam Example"""

# devices = [["device","type","dateadded","IP Address"],
# ["computer","pc","1591259971","192.168.100.1"],
# ["android phone","phone","1591259971","192.168.100.3"],
# ["samsung phone","phone","1591259971","192.168.100.4"]]

# Create a Python script that will check if a file device.csv exists.  If it does, then the entries in the list should be appended to the file. 

# If the file does not exist, it should be created and the data added to the file.  Each of the 4 entries in the list should be added as a single line and the entries in the line should be separated by commas. 

#  Your text file should contain no square brackets.  You can test whether your .csv file works by opening it in Excel or a similar spreadsheet manipulation package. 

# The only import (except for any basic Python packages) you are allowed to make is for os.  
# Ensure that if any errors occur, an error message will be printed to the console window and that the file will always be closed; even if an error occurs, i.e. the file should always be closed after processing.

""" import os

devicelist = ""

devices = [

 ["device","type","dateadded","IP Address"],
 ["computer","pc","1591259971","192.168.100.1"],
 ["android phone","phone","1591259971","192.168.100.3"],
 ["samsung phone","phone","1591259971","192.168.100.4"]

 ]

for a in devices:
     for devices in a:
         devicelist += f"{devices},"

 # Test if the file exists
if os.path.isfile("device.csv"):
     print("File found - removing it.")

     # If it does, remove it
     os.remove("device.csv")
else:

     my_file = open("device.csv" , "a")
     my_file.write(str(devicelist))
     my_file.close()
      """


""" stinson@hotmail.com
arnold@me.com
jespley@mac.com
psharpe@optonline.net
laird@aol.com
campbell@icloud.com
tubesteak@yahoo.com
moxfulder@mac.com
mwilson@icloud.com
pfitza@msn.com
dleconte@hotmail.com
andrei@yahoo.ca
 """

""" 
while True:
    num1 = int(input("Enter the first number here: "))
    num2 = int(input("Enter the second number here: "))

    total = float(num1) / float(num2)

    if num1 and num2 == int:
        if total <= 0:
            print("The result was less than: 0")
            print(0)
            print("This is the sum after division: ", total)
        else:
            print("The result was greater than: 0")
    else:
        ValueError
        print("Wrong input!")
        print(-1) """


""" import os
from pathlib import Path
devicelist = ""
devices = [
    ["device","type","dateadded","IP Address"],
    ["computer","pc","1591259971","192.168.100.1"],
    ["android phone","phone","1591259971","192.168.100.3"],
    ["samsung phone","phone","1591259971","192.168.100.4"]
    ]


devices_file = ("devices.csv")# To check if the file exists or not
for a in devices:for device in a: devicelist += f"{device},"
if os.path.isfile(devices_file): devices_file = open ("devices.csv", "a")    devices_file.write(devicelist)    devices_file.close()


# If the file does not exist, the "else" statement will create the file and

else:
    devices_file = open ("devices.csv", "w")
    devices_file.write(devicelist)
    devices_file.close() """