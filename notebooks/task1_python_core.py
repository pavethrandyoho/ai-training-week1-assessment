import csv

class InvalidSalaryError(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Name: {self.name}, "
            f"Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )

def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result

with open("data/employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

# Convert salary from string to integer
for emp in employees:
    emp["salary"] = int(emp["salary"])


print("Normal bonus:", bonus(50000))
print("Bonus with extras:", bonus(50000, 0.1, 1000, 500))
print("Bonus with cap:", bonus(50000, 0.1, 1000, cap=4000))

emp1 = Employee("Arun", 30000)
manager1 = Manager("Priya", 80000, 5)

print(emp1.get_details())
print("Annual salary:", emp1.annual_salary())
print(manager1.get_details())

try:
    emp2 = Employee("Test", -500)

except InvalidSalaryError as e:
    print("Error:", e)

finally:
    print("Transaction finished")

above_50000 = [
    emp["name"] for emp in employees
    if emp["salary"] > 50000
]

print("Above 50000:", above_50000)

raised_salaries = list(
    map(lambda emp: emp["salary"] * 1.10, employees)
)

chennai_employees = list(
    filter(lambda emp: emp["city"] == "Chennai", employees)
)

chennai_names = [emp["name"] for emp in chennai_employees]

print("Chennai:", chennai_names)

salaries = [emp["salary"] for emp in employees]

for salary in salaries:

    if salary == 0:
        continue

    if salary > 85000:
        break
