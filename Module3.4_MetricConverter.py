

# Convert inches to centimeter and pounds to kilograms

""" def metric_converter1():
    user_input1 = int(input("Enter a number here: "))
    print ("Inches", user_input1)

    convert = user_input1 * 2.54
    print ("Inches converted to centimeter", convert )

 
metric_converter1()    """




# Løsningen til Glenn

def metric_converter(valuesInInches):
    print("Your value is:", valuesInInches, "inches")
    print("That's equalent to:", round(valuesInInches * 2.54, 2), "centrimetres")


#---------------------------------------
# Program starts here

value = float(input("Enter value be converted: "))
metric_converter(value)
print("End of program")

