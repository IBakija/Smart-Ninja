import random

while True:
    random_num = random.randint(1, 10)
    broj_pokusaja = 3
    while True:
        for i in range(broj_pokusaja):
            print "Pokusaj " + str(i + 1) + "/" + str(broj_pokusaja)
            pokusaj = int(raw_input("Guess the secret number: "))
            if pokusaj == random_num:
                print "Bravo!"
                break
            elif pokusaj > random_num:
                print "Try a smaller number."
            else:
                print "Try a bigger number."
            jos = ""
        if pokusaj != random_num:
            print "You have failed! The secret number is: %s" %random_num
        if jos != "y" or pokusaj == random_num:
            break
    josigra = raw_input("Jos jedna igra? (y/n): ")
    if josigra != "y":
        break
