
# --------- Module 3.3 ----------

# ----- Activity 3 ------


postcodes = {1331 : "FORNEBU", 1411 : "KOLBOTN"}

while True:
    pcentered = int(input("Enter a postcode: "))

    if pcentered == -1:
        break

    if pcentered in postcodes.keys():
       print("Postcode: ", pcentered, "-", postcodes[pcentered], "\n")
       break     
    else:
        print(pcentered, "is not in out system") 