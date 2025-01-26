### Virtual Tax Calculator

# First we'll ask about their salary

print("Welcome to the Virtual Tax Calculator!")
try:
    salary = input("What is your salary? ")
    salary = int(salary)
except ValueError:
    print("Please enter a valid value for salary.")
    salary = input("What is your salary? ")
    salary = int(salary)

# Then we'll ask about how many children they have
try:
    children = input("How many children do you have? ")
    children = int(children)
except ValueError:
    print("Please enter a valid value for children.")
    children = input("How many children do you have? ")

if children > 0:
    if salary < 2000:
        taxcut = (children * 1)/100
    else:
        taxcut = (children * 0.5)/100
else:
    taxcut = 0

print(f"Your tax cut is {taxcut}")
if salary < 1000:
    net = salary -(salary * (0.1 - taxcut))
    print(f"Your net salary is {net}")
elif salary >= 1000 and salary < 2000:
        net = salary - (salary * (0.12 - taxcut))
        print(f"Your net salary is {net}")
elif salary >= 2000 and salary < 4000:
        net = salary - (salary * (0.14 - taxcut))
        print(f"Your net salary is {net}")
elif salary >= 4000:
        net = salary - (salary * (0.18 - taxcut))
        print(f"Your net salary is {net}")

