car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["model"] = "toyota premio"

print(x) #after the change
