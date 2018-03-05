import random

def randomize(quantity):
    list = []
    while True:
        if len(list) == quantity:
            break
        newNumber = random.randint(1, 100)
        if newNumber not in list:
            list.append(newNumber)
    return list


def main():
    print "Welcome to the Lottery numbers generator."
    howManyNumbers = raw_input("Please enter how many random numbers would you like to have: ")
    howManyNumbers = int(howManyNumbers)
    print randomize(howManyNumbers)

if __name__== "__main__":
    main()