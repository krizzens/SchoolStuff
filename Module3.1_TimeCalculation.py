

# ---------- Activity 3.1 ----------

# Activity 2

# A manager has requested that you write a script that allows him to enter a value 
# representing the number of minutes one of his employees has worked in a month.
# He wants the script to use the number of minutes to calculate the number of days worked in the 
# month, the number of hours left over (not adding up to a full working day) 
# and the number of minutes left over (not adding up to a full hour). 
# For the sake of this calculation, a working day consists of eight hours. 
# Once calculated, display the resulting calculation in the following format: 
# working days:hours:minutes.

#user_input = ("Enter a value representing the number of minutes worked in a month: ")

minutes = int(input("Write minutes here: "))

# minutes = 11328


hours = int(minutes / 60)

days = int(hours / 8)



minutesLeft = minutes - (hours * 60)

hoursLeft = hours - (days * 8)


print(days, hoursLeft, minutesLeft, sep=":")