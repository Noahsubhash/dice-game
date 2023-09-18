import random
response = input("Do you want to roll the dice?")
y = "yes"
if response==y:
    while response == y:
        no = random.randint(1,6)
print (no)