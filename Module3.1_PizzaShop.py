

# ---------- Activity 3.1 ----------

# Activity 3

pizza_base = {"thick":10, "thin":5}

pizza_size = {"small":30, "medium":40, "large":50}

basic_sauce = {"tomato":5, "barbecue":10}

toppings = {"cheese":5, "mushrooms": 3, "avocado":7, "pineapple": 5, "bacon":7, "chicken":7, "fish":6}


# Bruker .lower for å godta om user skriver inn store bokstaver. Uten .lower vil kun små bokstaver være godkjendt.

sum = 0

q1 = input("Choose pizza base, thick or thin: ")
while True:
    if q1.lower() in pizza_base.keys():
        print("OK!")
        sum += pizza_base[q1.lower()]  
        break
    else:
        print(f"We dont have {q1.lower()} in our menu!")
        q1 = input("Choose pizza base, thick or thin: ")

print(sum)

q2 = input("Choose pizza size, small, medium or large: ")
while True:
    if q2 in pizza_size.keys():
        print("OK!")
        sum += pizza_size[q2]  
        break
    else:
        print(f"We dont have {q2} in our menu!")
        q2 = input("Choose pizza size, small, medium or large: ")

print(sum)

q3 = input("Choose basic sauce tomato or barbecue: ")
while True:
    if q3 in basic_sauce.keys():
        print("OK!")
        sum += basic_sauce[q3]  
        break
    else:
        print(f"We dont have {q3} in our menu!")
        q3 = input("Choose basic sauce tomato or barbecue: ")

print(sum)

q4 = input("Choose toppings cheese, mushrooms, avocado, pineapple, bacon, chicken or fish: ")
while True:
    if q4 in toppings.keys():
        print("OK!")
        sum += toppings[q4]  
        break
    else:
        break
        print(f"We dont have {q4} in our menu!")
        q4 = input("Choose toppings cheese, mushrooms, avocado, pineapple, bacon, chicken or fish: ")

print(f"The total cost is {sum}Kr")
