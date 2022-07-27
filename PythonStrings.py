#####################
#
# Codecademy projects for python 3 cours
#
#####################
"""
Write a function named count_char_x 
that takes a string named word and a single character named x as parameters. 
The function should return the number of times x appears in word.
"""
def count_char_x(word, x):
  count = 0
  for char in word:
    if char == x:
      count +=1
  return count 

"""
Write a function called unique_english_letters that takes the string word as a parameter. 
The function should return the total number of unique letters in the string. 
Uppercase and lowercase letters should be counted as different letters.
We’ve given you a list of every uppercase and lower case letter in the English alphabet. 
It will be helpful to include that list in your function.
"""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques +=1
  return uniques

"""
Write a function named count_multi_char_x that takes a string named word and a string named x. 
This function should do the same thing as the count_char_x function you just wrote - 
it should return the number of times x appears in word. 
However, this time, make sure your function works when x is multiple characters long.

For example, count_multi_char_x("Mississippi", "iss") should return 2
"""
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

"""
Write a function named substring_between_letters that takes a string named word, 
a single character named start, and another character named end. 
This function should return the substring between the first occurrence of start and end in word. 
If start or end are not in word, the function should return word.

For example, substring_between_letters("apple", "p", "e") should return "pl".

"""
