menu = {}
file = open("menu.txt", "w+")
while True:
    meal = raw_input("Enter todays meal: ")
    price = raw_input("Enter its price: ")
    menu[meal] = price + " kn"
    file = open("menu.txt", "a")
    file.write(meal + " " + str(menu[meal]) + "\n")
    file.close()
    more = raw_input("Would you like to enter another meal? (y/n)")
    if more.lower() != "y":
        break

print menu
