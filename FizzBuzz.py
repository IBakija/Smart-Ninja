number = int(raw_input("Enter a number to fizzbuzz up to it: "))

string = ""

for x in range(number):

    if ((x+1) % 3) == 0:

        string = string + "fizz"

    if ((x+1) % 5) == 0:

        string = string + "buzz"

    if (((x+1) % 3) != 0) and (((x+1) % 5) != 0):

        print x + 1

    else:

        print string

    string = ""