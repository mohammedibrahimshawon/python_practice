human  = {
  "name": "Arash",
  "class": 7,
  "age": 12
}
x = human.values()

# print(x) #before the change

human["age"] = 20

print(x) #after the change


# human["eyecolor"] = "brown"
# print(human)