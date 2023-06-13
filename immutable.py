first_name = 'sathish'
temp = first_name
print(id(first_name))
print(id(temp))

last_name = first_name + 'kumar'
print(id(last_name))
print(id(first_name))
