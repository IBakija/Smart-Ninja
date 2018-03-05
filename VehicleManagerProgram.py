class Vehicle(object):
    def __init__(self, brand, model, kilometersDoneSoFar, generalServiceDate):
        self.brand = brand
        self.model = model
        self.kilometersDoneSoFar = kilometersDoneSoFar
        self.generalServiceDate = generalServiceDate

    def getInfo(self):
        return self.brand + " " + self.model

    def getAll(self):
        return self.brand + "; " + self.model + "; " + self.kilometersDoneSoFar + "; " + self.generalServiceDate

def listAllVehicles(vehicles):
    for index, vehicle in enumerate(vehicles):
        print "ID: " + str(index)  # index is an order number of the vehicle object in the vehicles list
        print vehicle.getInfo()
        print vehicle.kilometersDoneSoFar + " km"
        print vehicle.generalServiceDate
        print "" # empty line

def addNewVehicles(vehicles):
    brand = raw_input("Please enter brand: ")
    model = raw_input("Please enter model: ")
    kilometersDoneSoFar = raw_input("Please enter kilometers done so far: ")
    generalServiceDate = raw_input("Please enter general service date: ")

    new = Vehicle(brand, model, kilometersDoneSoFar, generalServiceDate)
    vehicles.append(new)

    print ""  # empty line
    print new.getInfo() + " was successfully added to your vehicles list."

def editVehicles(vehicles):
    print "Select the number of the vehicle you'd like to edit: "

    for index, vehicle in enumerate(vehicles):
        print str(index) + ") " + vehicle.getInfo()

    print ""  # empty line
    selectedId = raw_input("Which vehicle would you like to edit? (enter ID number): ")
    selectedVehicle = vehicles[int(selectedId)]

    newKilometersDoneSoFar = raw_input("Please enter new value for kilometers done so far for %s: " % selectedVehicle.getInfo())
    selectedVehicle.kilometersDoneSoFar = newKilometersDoneSoFar

    newGeneralServiceDate = raw_input(
        "Please enter new date for general service date for %s: " % selectedVehicle.getInfo())
    selectedVehicle.generalServiceDate = newGeneralServiceDate

    print ""  # empty line
    print "Info updated."

def deleteVehicles(vehicles):
    for index, vehicle in enumerate(vehicles):
        print str(index) + ") " + vehicle.getInfo()
    print ""  # empty line
    selectedId = raw_input("What vhicle would you like to delete? (enter ID number): ")
    selectedVehicle = vehicles[int(selectedId)]
    vehicles.remove(selectedVehicle)
    print ""  # empty line
    print "Vehicle was successfully removed from your list."

def saveToDisk(vehicles):
    file = open("vehicles.txt", "w+")
    for vehicle in vehicles:
        file.write("%s, %s, %s, %s\n" % (vehicle.brand, vehicle.model, vehicle.kilometersDoneSoFar, vehicle.generalServiceDate))

def importInfo(vehicles):
    file = open("vehicles.txt", "r")
    for line in file:
        content = line.split(", ")
        print content
        if len(content) == 4:
            new = Vehicle(content[0], content[1], content[2], content[3])
            vehicles.append(new)

def main():
    print "Welcome to your Vehicle List"

    """toyota = Vehicle (brand = "Toyota", model = "Yaris", kilometersDoneSoFar = "256749", generalServiceDate ="21.3.2019.")
    hyundai = Vehicle(brand = "Hyundai", model = "Elantra", kilometersDoneSoFar = "654891", generalServiceDate = "14.1.2019.")"""
    vehicles = []

    while True:
        print ""  # empty line
        print "Please choose one of these options:"
        print "a) See all your vehicles"
        print "b) Add a new vehicle"
        print "c) Edit a vehicle"
        print "d) Delete a vehicle"
        print "e) Import list from file"
        print "f) Quit the program."
        print ""  # empty line

        selection = raw_input("Enter your selection (a, b, c, d, e or f): ")
        print ""  # empty line

        if selection.lower() == "a":
            listAllVehicles(vehicles)
        elif selection.lower() == "b":
            addNewVehicles(vehicles)
        elif selection.lower() == "c":
            editVehicles(vehicles)
        elif selection.lower() == "d":
            deleteVehicles(vehicles)
        elif selection.lower() == "e":
            importInfo(vehicles)
        elif selection.lower() == "f":
            saveToDisk(vehicles)
            print "Thank you for using Vehicle Manager Program. Goodbye!"
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue

if __name__ == "__main__":
    main()