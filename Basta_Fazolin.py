########################
#
# Basta Fazoolin'
# Author : Rok Kepa aka AudiTTRSi
# example from https://www.codecademy.com/
# Version 1.0
#
########################

class Menu:
    def __init__ (self,name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            if item in self.items:
                total_price += self.items[item]
        return(total_price)

    def __repr__(self):
        return("{a} menu available from {b} to {c}".format(a = self.name, b = self.start_time, c = self.end_time))

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return("The restaurant is in {a}".format(a = self.address))

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time < menu.end_time:
        available_menu.append(menu)
    return(available_menu)

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises



brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
early_bird_items ={'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
dinner_items ={ 'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
kids_items = {  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

brunch = Menu("Brunch", brunch_items,11,16)
early_bird = Menu("Early Bird", early_bird_items, 15,18)
dinner = Menu("Diner", dinner_items,17,23)
kids = Menu("Kids menu", kids_items,11,21)
arepas_menu = Menu("franchise", franchise_items, 1000, 2000)

#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

flagship_store = Franchise("1232 West End Road",[brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Muberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
#print(flagship_store.available_menus(1200))
#print(flagship_store.available_menus(1700))
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepa = Business("Take a' Arepa", [arepas_place])
print(arepa)

print(brunch)
