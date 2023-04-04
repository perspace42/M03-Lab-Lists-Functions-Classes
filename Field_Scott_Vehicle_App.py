'''
Author: Scott Field
Version: 1.00
Date: 4/04/2023
Program Name: Vehicle_App
Program Purpose: Create a Python App that meets the following requirements
- A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
- A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
    - year
    - make
    - model
    - doors (2 or 4)
    - roof (solid or sun roof).
- Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
  The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
  The app will then output the data in an easy-to-read and understandable format, such as this:
    - Vehicle type: car
    - Year: 2022
    - Make: Toyota
    - Model: Corolla
    - Number of doors: 4
    - Type of roof: sun roof

Variable List:
user_input [string] (stores input string and string user input)
validated [boolean] (stores if user_input is valid for input loops)

vehicle_type [string] (stores the type of vehicle: car, truck, plane, boat, broomstick)
vehicle_year = [int] (stores the vehicle year of production)
vehicle_make = [string] (stores the company that made the vehicle)
vehicle_model = [string] (stores the vehicle model name)
vehicle_doors = [string] (stores the number of vehicle doors: 2 or 4)
vehicle_roof = [string] (stores whether the vehicle roof type: solid or sunroof)

the_vehicle = [Automobile] the class that stores the vehicle charecteristics entered by the user

'''

#Superclass
class Vehicle():
    def __init___(self,vehicle_type):
        self.vehicle_type = vehicle_type
    
    #setter method
    def setType(self,newType):
        self.vehicle_type = newType
    
    #getter method
    def getType(self):
        return self.vehicle_type

#Subclass
class Automobile(Vehicle):
    def __init__(self,vehicle_type,year,make,model,doors,roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

        #Get SuperClass Attribute
        Vehicle.__init__(vehicle_type)

    #Setter Methods

    def setYear(self,newYear):
        self.year = newYear

    def setMake(self,newMake):
        self.make = newMake

    def setModel(self,newModel):
        self.model = newModel
    
    def setDoors(self,newDoors):
        self.doors = newDoors

    def setRoof(self,newRoof):
        self.roof = newRoof

    #Getter Methods
    
    def getYear(self):
        return self.year

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model
    
    def getDoors(self):
        return self.doors

    def getRoof(self):
        return self.roof
    
    #Print Method
    def __str__(self):
        return ("Vehicle Type: " + self.getType() + "\n"
                "Year: " + str(self.getYear()) + "\n"
                "Make: " + self.getMake() + "\n"
                "Model: " + self.getModel() + "\n"
                "Number of Doors: " + str(self.getDoors()) + "\n"
                "Type of Roof: " + self.getRoof() + "\n")
      
#App Code
def main():
    #Variable Initialization
    user_input = ""
    validated = False

    vehicle_type = ""
    vehicle_year = 0
    vehicle_make = ""
    vehicle_model = ""
    vehicle_doors = 0
    vehicle_roof = 0

    #Class Initialization
    the_vehicle = Automobile(vehicle_type,vehicle_year,vehicle_make,vehicle_model,vehicle_doors,vehicle_roof)

    

    #Welcome Message
    print("Please enter your vehicles type, model year, maker, model name, number of doors, and roof type.\nThe program will then ouput the data you've entered.\n")

    #Get User Input Section

    #Get Vehicle Type:
    user_input = input("Please enter the vehicle type\n (car, truck, plane, boat, broomstick)\n:")
    #Lowercase input for input validation loop
    user_input = user_input.lower()

    #Input Validation Loop
    while (user_input not in ["car","truck","plane","boat","broomstick"]):

        print("Error input must be: (car, truck, plane, boat, broomstick) \n (This loop will repeat until correct input is entered) ")
        user_input = input("Please enter the vehicle type\n (car, truck, plane, boat, broomstick)\n:")
    
    #Assign Vehicle Type To Class
    vehicle_type = user_input
    the_vehicle.setType(vehicle_type)

    #Get Vehicle Year
    user_input = input("Please enter the " + vehicle_type + "s" + " model year\n:")
    
    #Input Validation Loop
    while (validated == False):
        try:
            vehicle_year = int(user_input)
        except:
            print("Error input must be an integer number \n (This loop will repeat until correct input is entered)")
            user_input = input("Please enter the " + vehicle_type + "s" + " model year\n:")
        else:
            validated = True

    #Assign Vehicle Year To Class
    the_vehicle.setYear(vehicle_year)

    #Get Vehicle Make
    user_input = input("Please enter the " + vehicle_type + "s" + " maker\n:")
    vehicle_make = user_input
    the_vehicle.setMake(vehicle_make)

    #Get Model Name
    user_input = input("Please enter the " + vehicle_type + "s" + " model name\n:")
    vehicle_model = user_input
    the_vehicle.setModel(vehicle_model)

    #Get Number Of Doors
    user_input = input("please enter the number of doors the " + str(vehicle_year) + " " + vehicle_make + " " + vehicle_model + " has\n(2 or 4)\n:")
    
    #Input Validation Loop
    validated = False
    while (validated == False):
        if (user_input == "2" or user_input == "4"):
            vehicle_doors = int(user_input)
            the_vehicle.setDoors(vehicle_doors)
            validated = True
        else:
            print("Error, the number of doors must be 2 or 4 \n (This loop will repeat until correct input is entered)")
            user_input = input("please enter the number of doors the " + str(vehicle_year) + " " + vehicle_make + " " + vehicle_model + " has\n(2 or 4)\n:")

    #Get Roof Type
    user_input = input("please enter the type of roof the " + str(vehicle_year) + " " + vehicle_make + " " + vehicle_model + " has\n(solid or sunroof):")
    #Lowercase input for input validation loop
    user_input = user_input.lower()

    #Input Validation Loop
    validated = False
    while (validated == False):
        if (user_input == "solid" or user_input == "sunroof"):
            vehicle_roof = user_input
            the_vehicle.setRoof(vehicle_roof)
            validated = True
        else:
            print("Error, a cars roof must be solid or sunroof \n(This loop will repeat until correct input is entered)")
            user_input = input("please enter the type of roof the " + str(vehicle_year) + " " + vehicle_make + " " + vehicle_model + " has\n(solid or sunroof):")
    
    #Print Header
    print("\nVehicle Data\n")
    #Print Data
    print(the_vehicle)

#Call Main Method
if (__name__ == "__main__"):
    main()