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

"""
5)
return Key with max value
"""
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

"""
6)
Write a function named word_length_dictionary that takes a list of strings named words as a parameter.
The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
"""
def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

"""
7)
Write a function named frequency_dictionary that takes a list of elements named words as a parameter.
The function should return a dictionary containing the frequency of each element in words.
"""

def frequency_dictionary(words):
  freq_words = {}
  for word in words:
    if word not in freq_words:
      freq_words[word] = 0
    freq_words[word] += 1

  return freq_words
"""
8)
unique values in dictionary
"""
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

"""
9)
Create a function named count_first_letter that takes a dictionary named names as a parameter.
names should be a dictionary where the key is a last name and the value is a list of first names.
For example, the dictionary might look like this:

names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
The function should return a new dictionary where each key is the first letter of a last name,
and the value is the number of people whose last name begins with that letter.

So in example above, the function would return:

{"S" : 4, "L": 3}
  """
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
