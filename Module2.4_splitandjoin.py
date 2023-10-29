
# ---------- Module 2.4 ----------

# ----- Activity 1 -----

# Prompt the user to enter a string of text.
# user_input = input("Enter a text here: ")
user_input = "Hello what's going on"
# print(user_input)


# Ask the user for a character on which to split their text.
user_input1 = input("Type a character here: ")
#user_input1 = "o"

# Use this character to split their initial string.
result_one = user_input.split(user_input1)

print(result_one)

# Request text from the user to use in order to re-combine the string.
result_two = input("Type in the missing letter here: ")
#result_two = "o"

# Display the re-combined string to the user.

print(user_input1.join(result_one))