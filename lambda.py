people=[
    {"name":"Harry", "house":"Gyaffindor"},
    {"name":"Cho", "house":"Ravenclaw"},
    {"name":"Draco", "house":"Slytherin"}
]

##def f(person):
##    return person["name"]

##people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)

