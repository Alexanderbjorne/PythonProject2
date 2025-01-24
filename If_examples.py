# Lets create a virtual bartender that serves you if you are of legal age

from random import choice
drinks = ["Whiskey", "Rum", "Tequila", "Gin", "Sake","Wine","Beer","Vodka","Cognac"]
mixers = ["Fanta","Fanta Limon","Red Bull","Tonic","Coca-Cola","Soda"]

# print(f"{choice(drinks)} and {choice(mixers)}")
print("I am the virtual bartender, welcome to the party")
name = input("What is your name? ").capitalize()

try:
    age = input(f"How old are you {name}? ")
    age = int(age) # this is where we can have problems
    legal = None
    country = input("Where are you from?")
    if age < 14:
        legal = False
    elif age < 16:
        if country == "Austria":
            legal = True
        else:
            legal = False
    elif age < 18:
        if country == "Austria" or country == "Luxembourg":
            legal = True
        else:
            legal = False
    elif age < 21:
        if country == "USA" or country == "UAE":
            legal = False
        else:
            legal = True
    else:
        legal = True
    if legal:
        print(f"Welcome to the party {name}! Enjoy your {choice(drinks)} and {choice(mixers)}!")
    else:
        print(f"Sorry {name}, I can only serve you {choice(mixers)}!")
except ValueError:
    print("I don't have time for your games! Get outta here!")

