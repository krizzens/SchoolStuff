
base = "T"
size = "M"

if base == "t":
    base = 5
else:
    base = 10

if size.lower() == "s":
    size = 30
elif size.lower() == "m":
    size = 40

else:
    size = 50

print("the cost for your pizza is:")