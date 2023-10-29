
#----------Module 2.3----------

# ----Task 1----
# Given the below variable and string assignment, use it in your Python script and print the indexes in the following order 16,15,4,17,6,12,11,18. You must use the Python split() function to split the string.
strMessage = "what,is,not,good,I,will,be,you,ok,Noroff,student,Python,a,awesome,pretty,knew,who,would,programmer"

strList = strMessage.split(",")

print(strList[16], strList[15],strList[4], strList[17], strList[6], strList[12], strList[11], strList[18] )




# ----Task 2----
# Create a script that will underline any length of a string. Use the below string as a start. Only 1 “-“ can be used for the print function.
# If you change the string, the print function should underline the new string without you needing to change the print function. 
# The script should print the string and then print the “-“ characters underneath the string, to the same length as the original string. 

strUnderline = "This sentence must be underlined"
underlined_text = "\x1B[4m" + strUnderline + "\x1B[0m"
print(underlined_text)

strUnderline = "This sentence must be underlined"
num = len(strUnderline) - 2

print(strUnderline)
print("", num * "-")



# ----Task 3----
# Use the below string, and create a Python script that will change the delimiter from a space to a 1) semicolon (;) 2) a comma (,) and 3) the pipe character (|).

setn = "Change me delimiter"

print(setn)
print(setn.replace(" ", ";"))
print(setn.replace(" ", ","))
print(setn.replace(" ", "|"))
