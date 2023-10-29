

# --------- Module 3.3 ----------

# ----- Activity 4 -----

totalsales= 0
salecounter = 0
counter = 0

while counter < 10:
    counter += 1

    #Taking in values
    valuesentered = float(input("Enter your sales number: "))

    if valuesentered < 5000:
        continue
    if 5000 < valuesentered < 10001:
        salecounter += 1
        totalsales += valuesentered
        averagesales = totalsales / salecounter

        print("This sale was: \t\t\t", valuesentered)
        print("Number of sales this mount: \t", salecounter)
        print("Your total sale this mount is: \t", totalsales)
        print("Your average sale was: \t\t", averagesales)

    elif valuesentered > 10000:
        print("A possible data entry error as occured")
        break   


    