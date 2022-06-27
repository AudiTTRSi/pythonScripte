###################
#
# Scrabble
# example from https://www.codecademy.com/
# author : audittrsi
##################

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = zip (letters, points)

letter_to_points_dic = {key:value for key,value in letter_to_points}
#print(letter_to_points_dic)

letter_to_points_dic[" "] = 0
print(letter_to_points_dic)

def score_word(word):
  modified = word.upper()
  point_total = 0
  for letter in modified:
    #print(letter)
    point = letter_to_points_dic.get(letter,0)
    #print(point)
    point_total += point

  return point_total
print(" ")
#print(score_word("Test"))
brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words ={"player1": ["BLUE", "TENNS", "EXIT"],
"wordNerd": ["EARTH", "EYES", "MACHINE"],
"Lexi Con": ["ERASER", "BELLY", "HUSKY"],
"Prof Reader": ["ZAP", "COMA", "PERIOD"]
}
player_to_points = {}

for player,words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)
