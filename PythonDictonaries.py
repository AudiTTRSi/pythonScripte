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

"""
3)
Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
The function should add 10 to every value in my_dictionary and return my_dictionary

"""
def add_ten(my_dictionary):
   for key in my_dictionary.keys():
     my_dictionary[key] +=10
   return my_dictionary   

"""
4)
FUnction that returns values that are present in dictionary as key and as values
"""
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      value_keys.append(value)
  return value_keys
