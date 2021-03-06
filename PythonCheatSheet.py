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

#method split
spring_storm_text = \
"""The sky has given over
its bitterness.
Out of the dark change
all day long
rain falls and falls
as if it would never end.
"""

spring_storm_lines = spring_storm_text.split('\n')

#method join
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = '\n'.join(winter_trees_lines)

#method strip ()
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped=[]
for i in love_maybe_lines:
  stripped = i.strip()
  love_maybe_lines_stripped.append(stripped)

print(love_maybe_lines_stripped)
love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)

#method replace
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career,
was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman,
born into slavery in 1839 in Chatham County, North Carolina.
Jean Tomer is most well known for his first book Cane,
which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')

#method find
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown")

#method format
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

#####################
#  modules          #
#####################
from module_name import object_name as name_you_pick
from matplotlib import pyplot as plt

#####################
#  dictionaries     #
#####################
translations = {"mountain":"orod","bread":"bass","friend":"mellon","horse":"roch"}
children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] , "Corleone":["Sonny", "Fredo", "Michael"] }
#empty dic and adding key value pair
animals_in_zoo = {}
animals_in_zoo["zebras"]= 8

#adding multiple entries to dic in one line
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen":85739})

#dictionary comprehension
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks,caffeine)

drinks_to_caffeine = {key:value for key,value in zipped_drinks}

#dictonary get all items
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for name, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of "+ name + "s")

#####################
#  files            #
#####################

#opening and reading fiiles
with open('millay_sonnet.txt') as sonnet_doc:
first_line = sonnet_doc.readline()
second_line = sonnet_doc.readline()
print(second_line)

#writing to file
with open('generated_file.txt', 'w') as gen_file:
    gen_file.write("What an incredible file!")

#readign csv file
import csv

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])

#readign json file
import json

with open('message.json') as message_json:
  message = json.load(message_json)

  print(message)

  #####################
  #  obj oriented     #
  #####################

  # self contructor
class SearchEngineEntry:
    def __init__(self, url):
        self.url = url

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
print(codecademy.url)
# prints "www.codecademy.com"
print(wikipedia.url)
# prints "www.wikipedia.org"
