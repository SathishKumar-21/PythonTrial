employee = {
    "Id": "2128841",
    "First_name": "Sathish kumar",
    "Last_name": "B",
    "DOB": "21/09/2000",
    "Character": "Good",
}

employee["phone"] = "7397178824"
employee["E-mali"] = "bs.sathishkumar.24@gmail.com"

# Id = employee["Id"]
# print(Id)
#
# name = employee["First_name"]
# print(name)
#
# school = employee.get("school")
# print(school)

# for key in employee:
#     print(key, employee[key], sep=": ")
# del employee["Id"]
delete_ID = employee.popitem()
print(delete_ID)
print()
for key, value in employee.items():
    print(key, value, sep=": ")


