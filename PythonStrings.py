#####################
#
# Codecademy projects for python 3 course
#
#####################
"""
1)
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
2)
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
3)
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
4)
Write a function named substring_between_letters that takes a string named word, 
a single character named start, and another character named end. 
This function should return the substring between the first occurrence of start and end in word. 
If start or end are not in word, the function should return word.

For example, substring_between_letters("apple", "p", "e") should return "pl".

"""
def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return(word[start_ind+1:end_ind])
  return word

"""
5)
Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. 
This function should return True if every word in sentence has a length greater than or equal to x.

"""
def x_length_words(sentence,x):
  words = sentence.split()
  for word in words:
    if len(word) >= x:
      return True
    else:
      return False  

    
"""
Function to check if string name is included in string setence

"""
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()
"""
FUnction that returns every second letter of the string
"""
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

"""
reversing string 
"""

def reverse_string(word):
  new_string = ""
  for i in range(len(word)-1, -1, -1):
    new_string += word[i]
  return new_string
