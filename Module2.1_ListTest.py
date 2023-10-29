
# ---------- Module task 2.1 ----------
# Activity 1

# Define a lsit
nameList = []
nameList = ["Per", "Jonas", "Tom", "Adrian", "Ole", "Mons", "Kari", "Åse", "Olav", "Odin"]
print(nameList)

# Sort the list
nameList.sort()
print(nameList)

# Reverse the list
nameList.reverse()
print(nameList)

# Ask the user for one more name
nameValue = input("What name do you want to add to the list?")

# Append the name to the end of the original list
nameList.append(nameValue)
print(nameList)

# Display the content of the original list

nameList.pop()
print(nameList)