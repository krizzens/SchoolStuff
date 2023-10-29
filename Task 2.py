"""You are working on a project that requires you to read and manipulate data from a text file. The text file contains a list of emails, one email per line. Your task is to create a Python script that does the following:

Reads the data from a text file named "emails.txt"

Removes any duplicates emails in the file and sorts them alphabetically.

Writes the cleaned and sorted list of emails back to the text file, overwriting the original data.

Prints the number of unique emails to the console.

Document your code, use docstrings where appropriate.

Paste your Python code as your answer. It is recommended to upload your .py file as an attachment. The .py file should only include code relating to the current assignment"""




""" I created a new text document named email.txt and typed in some random email adresses"""

# "r" is used to read the content of the file
text_file = open("email.txt","r")

print("Here is the original email list in the text document:", text_file.read())

all_emails = [
"stinson@hotmail.com",
"arnold@me.com",
"jespley@mac.com",
"psharpe@optonline.net",
"laird@aol.com",
"campbell@icloud.com",
"tubesteak@yahoo.com",
"moxfulder@mac.com",
"mwilson@icloud.com",
"pfitza@msn.com",
"dleconte@hotmail.com",
"andrei@yahoo.ca",
"stinson@hotmail.com",]

# The "sort" function is used to sort the stings in my list.
all_emails.sort()
print("Here is the sorted list of all emails: ", all_emails)


# To remove any dublicates i made the list to a dictionary using "list(dict.fromkeys". A dictionary cant have dublicate keys.

"""The only duplicate in my list is stinson@hotmail.com, and it will b"""
all_emails = list(dict.fromkeys(all_emails))
print("Here is the list without duplicates: ", all_emails)



# Here i created a function that counts the number of unique email adresses. The "len" function returns the number of items in the "all_emails" list.
unique_emails= set(all_emails)             
number_of_emails = len(unique_emails)

print(number_of_emails)

# "w" is used to create a new file and delete the file if it already exist.
# ".write" overwrite the content of the original file
# ".close" is used to close the file that i have opened
new_file = open("email.txt" , "w")
new_file.write(str(all_emails))
new_file.close()


