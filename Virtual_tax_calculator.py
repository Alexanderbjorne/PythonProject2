salary = input("Enter your salary: ")
try:
    salary = int(salary)
    if salary < 1000:
        print(salary * 0.1)
except ValueError:
    print("Please enter a valid number.")

