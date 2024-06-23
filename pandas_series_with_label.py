import pandas as pd # importing pandas library as pd

students = ["Daniel", "Zadva", "Kefas", "Comfort", "Mary"]

students_data = pd.Series(students)

print(students_data) #this prints with default label 0 - end using index

print(students_data[4]) # this prints students_data at index 4


#creating labels for series
students_data = pd.Series(students, index = ["A", "B", "C", "D", "E"])
print(students_data)

#you can also access series by labels
print(students_data["D"]) # will print Comfort