# Lists methods 101

example_list = [1, 2, 3, 4]

# Using Append
example_list.append(5)
# print(example_list)

# Using Remove
example_list.remove(5)
# print(example_list)

# adding more items
example_list_2=example_list + [11, 22, 33]
# adding more items
broken_prices = [5, 3, 4, 5, 4] + [4]

# Accessing List Elements

#####################
#list comprehension #
#####################

#example 1
grades = [90, 88, 62, 76, 74, 89, 48, 57]
#all values her are +10 to what it is in grades list
scaled_grades = [grade+10 for grade in grades]

#example 2
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
#heights that are biggr than 161
can_ride_coaster = [height for height in heights if height > 161]

#example 3
single_digits = list(range(10))
cubes = [digit**3 for digit in single_digits]

#####################
#  functions        #
#####################


#####################
#  string           #
#####################

#splitting string
spring_storm_text = \
"""The sky has given over
its bitterness.
Out of the dark change
all day long
rain falls and falls
as if it would never end.
"""

spring_storm_lines = spring_storm_text.split('\n')

#joining string
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = '\n'.join(winter_trees_lines)
