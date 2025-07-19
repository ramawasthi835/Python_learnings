# ENUMERATE FUNCTION

# List of animals
animals = ["dogs", "cats", "mouse", "lions", "birds", "monkeys", "zebra", "tiger", "peacock"]

# Looping through the list using enumerate to get both index (item) and value (animal)
for item, animal in enumerate(animals):
    # Print the animal if its index is 2, 4, or 6
    if item == 2 or item == 4 or item == 6:
        print(animal)
    else:
        pass  # Do nothing for other indices

        

