
# ---------- Module 2.4 ----------

# Activity 2

# Prompt the user to enter a string of text
string1 = input("Enter a text here: ")
#string1 = ("This is the test string")
print("String: ", string1)

# Display the length of the string.
print(len(string1))

# Ask the user for an index in the string.
index = int(input("select index: "))

# Display the string entered by the user, BUT add single quotes (“) around the word *of the index* that the user entered on the previous option.
string_list = string1.split(" ") 
string_list.insert(index, "\"")
string_list.insert(index - 1, "\"")

print(string_list)

print(" ".join(string_list))





