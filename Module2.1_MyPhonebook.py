
# ---------- Module task 2.1 ----------
# Activity 3

# 1. Define a dictionary consisting of five business names and their associated phone numbers. The business name should be used as the key.
business = {}
business = {"Apple":12345, "IGN":2468, "Noroff":8765, "Skyss":101010, "Elkjøp":434343}
print("Dictionary:", business)
""" print(business["Apple"]) """

# 2. Request the name and number of another business from the user and add it to the dictionary.
name = input("Enter business name: ")
phone_number = input("Enter phone number of the business: ")
business[name] = phone_number


# 3. Ask the user to type in the name of a business that is in the list. Display the result to the user.
user_input = (input("Type in a name of a business thats in this list: "))
if user_input in business.keys ():
    print("This name is in this dictionary!")
else:
    print("This is not correct!")

 
# 4. Display the entire dictionary (names and phone numbers).
print(business)

# 5. Display only the business names (no phone numbers).
print("Only the keys:", business.keys())

# Displayed only the key values (no business names) 
print(business.values())