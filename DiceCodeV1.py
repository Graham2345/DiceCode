import random as rand
def start():
    numofd = input ("How many dice do you wanna roll? ")
    count = 0
    values = []
    tot = 0
    for count in range (0, numofd):
        roll = (rand.randint(1,6))
        values.append(roll)
    print values
    for tot in range (roll):
        vallist = values
        tot = sum(vallist)
    print tot

def help():
    print ("Start the program and type start() into the terminal, the program will then ask you how many dice you want to roll. The program will then output a string of numbers and total them when after the string. To roll more dice, type start() again.")
