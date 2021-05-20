import random

d = {
    "one": 1,
    "two": 2,
    "three": 3 
}

otvet = random.choice(list(d.items()))
print(otvet)