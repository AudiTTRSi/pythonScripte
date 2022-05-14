combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
print(combo_meals.get(3, ["hamburger", "fries"]))
#Correct! There is no key 3 in this dictionary, so the default provided to the .get() function, ["hamburger", "fries"], will be printed.
