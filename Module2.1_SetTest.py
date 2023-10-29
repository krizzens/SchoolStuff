
# ---------- Module task 2.1 ----------
# Activity 2

# 1. Define a list.
food_set = {}


# 2. Populate the set with the names of your five favourite fast foods (no user input required).
food_set = {"burger", "pizza", "kebab", "taco", "sushi"}

print("My favourite fast foods:", food_set)

# 3. Define a second set and populate it with the names of a friend’s five favourite fast foods (no user input required).
Setfood_friend = {"kylling", "kjøttdeig", "fiskekake", "apekatt", "pizza"}
print("My friends favourite fast fooods:", Setfood_friend)

# 4. Add another type of fast food to your set of favourite foods.
food_set.add("fiskekake")
print("After add() of fiskekake to my list:", food_set)

# 5. Determine which favourite fast foods are shared by you and your friend and display these overlapped foods.
print("Difference of foods in my and my friends set:", food_set.difference(Setfood_friend))

print("Intersection of my food set and my friends set:", food_set.intersection(Setfood_friend)) 

