salary = int(input("Enter Salary: "))

if salary >=0 and salary < 20000:
    increment_percent = 5
elif salary >= 20000 and salary < 50000:
    increment_percent = 10
elif salary >= 50000 and salary < 100000:
    increment_percent = 15
elif salary >= 100000 and salary < 200000:
    increment_percent = 20
else:
    increment_percent = 30

print("Increment percent = ")
print(increment_percent)
increment=(increment_percent*salary/100)

total_salary = salary + increment
print("Total Salary: ")
print(total_salary)
