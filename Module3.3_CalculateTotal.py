
# ---------- Module 3.3 ----------


# ----- Activity 1 -----




""" Create a script called CalculateTotal.py. The script should continuously ask a user to enter an integer value. 
This should continue until the user has entered the value -1. Once the loop has ended, print the total of all 
the values entered by the user (excluding -1).
"""


total = 0
q1 = 0 

while q1 != "q":
    try: 
        q1 = input("Write a number here or q to quit: ")
        
        total += int(q1)

    except: 
        if q1 != "q":

            print("Wrong input, try again ")

    

print ("Here is the total of all the values entered" ,total)    
    
  

# Glenn sitt svar
    
# total = 0
# q1 = 0
# while q1 != -1:
#     try:
#         q1 = int(input('Input a q1 (-1 if you are done): '))
#         if q1 >= 0:
#             total += q1
#     except:
#         print('you have to enter a q1')
#         q1 = int(input('Input a q1 (-1 if you are done): '))
#    
# 
# print(f"The total value is {q1}")
