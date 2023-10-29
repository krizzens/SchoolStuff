
""" Create a class called "Car" which has the variables name, speed, and mileage.

The "Car" class should include a method called info, which uses name, speed, and mileage to print the information to the user such as this: "The car is a Volvo, it has a top speed of 155km/h and the mileage is 125 000km".

Create another classed called "Volvo", which inherits all instance variables from class "Car"

The "Volvo" class should have "Volvo" as a default value for the name.

Create an instance of the "Volvo" class that only uses mileage and speed as variables.

Only an instance of the Volvo class should be created. """


"""Here is the "Car" class that is asking for a name, speed and, milage"""

class Car:

    def __init__(self, name, speed, milage):
        self.name = name
        self.speed = speed
        self.milage = milage



# I created a new variabel to store the information and wrote the information that the task asked.
car1 = Car("Volvo", "155kmt", "125 000km")

# Here is the complete print state
print("This is the first class:")
print("The car is a " + car1.name, "it has a top speed of " + car1.speed, "and the milage is " + car1.milage)


# "Volvo" is set as the default name of the new class.
# The class only needs to use milage and speed as variables.
class Volvo:

     def __init__(self, name, speed, milage):
        Car.__init__(self, name, speed, milage)
        self.name = "Volvo"
        self.speed = speed
        self.milage = milage


car2 = Volvo("", "155kmt", "125 000km")
print("This is the second class: ")
print(car2.name, car2.speed, car2.milage )
