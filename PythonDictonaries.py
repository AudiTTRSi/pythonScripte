#####################
#
# Codecademy projects for python 3 course
#
#####################

"""
1)
Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. 
The function should return the sum of the values of the dictionary
"""

def sum_values(my_dictionary):
  sum = 0
  for item in my_dictionary.values():
    sum += item
  return sum

"""
2)
Sum of even key's values
"""

def sum_even_keys(my_dictionary):
  sum = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      sum += my_dictionary[key]
  return sum   
