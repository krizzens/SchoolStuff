
# ---------- Module 3.2 ----------


menu = input("""

*********************
Menu System
*********************

---------------------
Guess the number        (1)

Calculate time          (2)    

Print something         (3)

Change a print option   (4)
----------------------

What option would you like?
 
""")


print(menu)


if menu == "1":
    print ("Guess the number!")
    q1 = int(input("Enter a number: "))

    while True:
        if q1 == 543:
            print ("You guessed the number! It is 543")
            break
            
        elif q1 < 543:
            print ("The number you entered is too low")  
            q1 = int(input("Enter a number: "))
        elif q1 > 543:
            print ("The number you entered is too high")
            q1 = int(input("Enter a number: "))

elif menu == "2" :
    print ("Calculate time!")
    
    
    while True:
        time = int(input("Enter time (format hh): "))

        # time can only be between 00 and 23
        if 00 <= time <= 23:
            
            if 8 <= time < 17:          
                print("Inside working hours")
                break
            else:
                print("Private time")
                break
        else:
            print("Wrong input")
            
            

elif menu == "3" :
    print("Print something!")
    message = {0:"Coding is fun", 1:"Python is not code, but a way of life", 2:"We learn Python the fun way", 3:"We code, because we can"}
    
    
    while True:
        enter_number = int(input("Enter 0, 1, 2 or 3 here to print a message: "))

        if enter_number+1 in message.keys() :
            print (message[enter_number])
            user_input = input("Do you want to print another message? y for yes or n for no: ")
            if user_input == "y":
              enter_number 
            else:
                break

            
        else:
             print("The number is wrong")
    
elif menu == "4" :
    print("Change a print option")
    message =["Coding is fun", "Python is not code, but a way of life", "We learn Python the fun way", "We code, because we can"]
    name = int(input("Write a number 0, 1, 2 or 3: "))
    message[name] = input("Write the new text here: ")
    print(message)



