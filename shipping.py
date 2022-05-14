###################
#
# Sal's Shipping
# author : coreBlaster75491 aka Rok Kepa
##################

###
# calculate shipping cost
##
def shipping_cost(weight, type):
    shippping_price = 0
    if (type == "standard"):
        if (weight <= 2):
            shippping_price =  weight * 1.5 + 20.0
        elif (2 < weight <=6):
            shippping_price =  weight * 3.0 + 20.0
        elif (6 < weight <=10):
            shippping_price =  weight * 4.0 + 20.0
        else:
            shippping_price =  weight * 4.75 + 20.0
    elif(type == "premium"):
        shippping_price = 125.0
    elif(type == "drone"):
        if (weight <= 2):
            shippping_price =  weight * 4.5
        elif (2 < weight <=6):
            shippping_price =  weight * 9.0
        elif (6 < weight <=10):
            shippping_price =  weight * 12.0
        else:
            shippping_price =  weight * 14.25
    return shippping_price

##################
#
# determening cheapest shipping method
# for each package
#
##################
def cheapest_shipping(weight):
  standard_price = shipping_cost(weight, "standard")
  premium_price = shipping_cost(weight, "premium")
  drone_price = shipping_cost(weight, "drone")
  if (standard_price < premium_price) and (standard_price < drone_price):
        return "Chepest shipping is standard shipping for " + str(standard_price) + "$."
  elif (premium_price < standard_price) and (premium_price < drone_price):
        return "Chepest shipping is premium shipping for " + str(premium_price) + "$."
  else:
        return "Chepest shipping is drone shipping for " + str(drone_price) + "$."
    

print(shipping_cost(3, "standard"))
print(shipping_cost(4.8, "standard"))
print(shipping_cost(4.8, "premium"))
print(shipping_cost(4.8, "drone"))


print(cheapest_shipping(3))
print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))
