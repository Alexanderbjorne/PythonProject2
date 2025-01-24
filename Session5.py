name = input("What is your name? ")
capse = name.capitalize()
print("Hello", capse)
#
# ### Year you were born
# age = input("How old are you "+capse+"? ")
# print(capse+" based on my advanced calculations, you were born in "+str(2024-int(age))+".")
#
### Simpler Way
age2 = input(f"How old are you {capse}? ")
try:
    age2 = int(age2) #Here there can be a problem
    print(f"{capse} based on my advanced calculations, you were born in {2024-age2}.")
except ValueError:
    print("Please enter a valid value for age.")
    age2 = input(f"How old are you {capse}? ")
    age2 = int(age2)
    print(f"{capse} based on my advanced calculations, you were born in {2024-age2}.")
except:
    print("This is another type of error.")