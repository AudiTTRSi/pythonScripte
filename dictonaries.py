children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}
#empty dictionary
my_empty_dictionary = {}

#adding items to empty dictonary
animals_in_zoo = {}

animals_in_zoo["zebras"]= 8
animals_in_zoo["monkeys"]= 12
animals_in_zoo["dinosaurs"]= 0
print(animals_in_zoo)

#adding items to dictonary

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen":85739})
print(user_ids)

# List Comprehensions to Dictionaries 
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = list(zip(drinks,caffeine))
print(zipped_drinks)
drinks_to_caffeine = dict(zipped_drinks)
