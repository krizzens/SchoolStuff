


"""Create a function named sum_of_five:

The function needs to receive 5 integer parameters and return the sum of the 5 values. 

Each of the five parameters should have default values assigned. The first parameter should have a default value of 1, the second parameter a default value of 2, the third a default value of 3, the fourth a default value of 4 and the fifth a default value of 5."""


 
# Here i create a function named sum_of_five that will add all the defalut values together and print out the total sum.
def sum_of_five(a,b,c,d,e):
    sum = a + b + c + d + e
    return sum
# Here is a new variabel that stores the defalut values. First i write the name of the function(sum_of_five) and then adds the correct numbers. I could write any numbers inside the sum_of_five(x,x,x,x,x) and than receive the total sum of all the numbers. 
total_values = sum_of_five(1,2,3,4,5)

# Here is the print statement that will show the total sum. 
print(total_values)



"""Create a function named comparison: 

The function needs to receive two integer parameters and test whether the first parameter is smaller than, greater than or equal to the second parameter. 

The function should return a string of "smaller than", "greater than" or "equal to"."""

# Here i create two variables containing two different values. These values is going to be compared. The value of the variables can be changed to any number.
value1 = 5
value2 = 10

# Using the "less than" operator i can see if value1 is less than value2. If value1 is less than value2 a string will be printed.
# If value1 is not less than value2 the function will go to the next step using "elif".
if value1 < value2:
   print("smaller than")

# Using the "greater than" operator i can see if value1 is less than value2. If value1 is greater than value2 a string will be printed.
# If value1 is not less than or greater than value2 the function will go to the next step using "else".
elif value1 > value2:
   print("grater than")

# Using the equality operator i can see if value1 is equal to value2. If value1 is equal to value2 a string will be printed.
else:
    value1 == value2
    print("equal to")



# Its also possible to make a user type in the numbers that you want to compare using "input" followed by a string.
q1 = input("Enter the first number here: ")
q2 = input("Enter the second number here: ")
value1 = q1
value2 = q2

if value1 < value2:
   print("smaller than")

elif value1 > value2:
   print("grater than")

else:
    value1 == value2
    print("equal to")