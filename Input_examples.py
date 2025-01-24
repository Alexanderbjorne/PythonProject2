name = input("What is your name? ")
capitalized_name = name.capitalize()
print("Hello", capitalized_name)
#
# ### Year you were born
# age = input("How old are you "+capse+"? ")
# print(capse+" based on my advanced calculations, you were born in "+str(2024-int(age))+".")
#
### Simpler Way
age2 = input(f"How old are you {capitalized_name}? ")
try:
    age2 = int(age2) #Here there can be a problem
    print(f"{capitalized_name} based on my advanced calculations, you were born in {2024 - age2}.")
except ValueError:
    print("Please enter a valid value for age.")
    age2 = input(f"How old are you {capitalized_name}? ")
    age2 = int(age2)
    print(f"{capitalized_name} based on my advanced calculations, you were born in {2024 - age2}.")
except:
    print("This is another type of error.")
else: # This is for no exception
    print("Thank you for playing as expected.")
finally: # This will be executed no matter what, at the very end
    print("Thank you for playing the game.")