pet1 = {
    "type": "Dog",
    "owner": "Nana"
}

pet2 = {
    "type": "Cat",
    "owner": "Kwame"
}

pet3 = {
    "type": "Bird",
    "owner": "Gyampoh"
}

pet4 = {
    "type": "Fish",
    "owner": "Tina"
}

# Store all dictionaries in a list
pets = [pet1, pet2, pet3, pet4]

# Printing all
for pet in pets:
    print("Type of Animal:", pet["type"])
    print("Owner:", pet["owner"])
    print(" ")
