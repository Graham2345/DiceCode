import random as rand
numofd = input ("How many dice do you wanna roll? ")
count =  0
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