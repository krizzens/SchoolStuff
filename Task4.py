

""" For this question, you are required to create the following Python function:

Create a function named divide, which has the following details:

·       It needs to receive 2 parameters.

·       The first parameter should be divided by the second one.

·       The function should return the result of the division as an integer.

·       If the result is less than 0, the function should return a value of 0.

·       If any errors occur during division, the function should return a value of -1 """


""" I have created a function named divide. Inside the function there is a while loop that allows the user to type even if what he/she types creates an an error. 

Once the function starts, the loop will "try:" to get numbers from the user and if the user write someting that would create an error "except" will handle this by printing a string and the number that the task asked for. 

The loop will then start from start again since there is not a "break" statement in the error handling.

I have created an "if" statement in inside the "try" statement to test if the divided(total) number is less than or greater than 0. If total is less than 0, som strings will be printed such as the what the number is.

I write "divide()" to call the function at the end.

"""

def divide():

    while True:
    
        try:
            num1 = (input("Enter the first number here: "))
            num2 = (input("Enter the second number here: "))

            total = float(num1) / float(num2)

            if total < 1:
                print("The result was less than: 0")
                print(0)
                print("This is the sum after division: ", total)
                break

            else:
                print("The result was greater than: 0")

        

    

        except ValueError:
            print("Wrong input!")
            print(-1)

            
divide()
    

