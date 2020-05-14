# Create your custom sandwich program
# Done

import pyinputplus as pyip

# create custom sandwich
bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
cheese = pyip.inputYesNo('Would you like some cheese? ')
cheese_type = ''
if cheese == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
extra = pyip.inputYesNo('Would you like some mayo / mustard / lettuce / tomato? ')
extra_type = ''
if extra == 'yes':
    extra_type = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], numbered=True)
sandwich_count = pyip.inputInt('How many of these sandwiches would you like? ', min=1)

# add custom sandwich to the order list
order = [bread_type, protein_type]
if cheese_type:
    order.append(cheese_type)
if extra_type:
    order.append(extra_type)

# define store prices
prices = {'bread_type': {'wheat': 0.5, 'white': 0.5, 'sourdough': 0.5},
          'protein_type': {'chicken': 0.5, 'turkey': 0.5, 'ham': 0.5, 'tofu': 0.5},
          'cheese_type': {'cheddar': 0.5, 'Swiss': 0.5, 'mozzarella': 0.5},
          'extra_type': {'mayo': 0.5, 'mustard': 0.5, 'lettuce': 0.5, 'tomato': 0.5}}


# function to calculate the prices based on the custom order
def temp_name(food_type, food_item):
    receipt = 0
    for x, y in food_type.items():  # x is food_type, y is the food_item of the prices dictionary.
        receipt = receipt + y.get(food_item, 0)
    return receipt


print("\nReceipt:")  # print prices of the individual components of the order
sandwich_price = 0
for i in range(len(order)):
    type_of_food = {0: 'bread', 1: 'protein', 2: 'cheese', 3: 'extra'}
    print(f'{order[i].title()} {type_of_food[i]} price: {float(temp_name(prices, order[i]))}0 cents.')
    sandwich_price += (temp_name(prices, order[i]))

# print the total price for the order
if sandwich_count == 1:
    print(f'Total price for a sandwich: €{float(sandwich_price)}0.')
if sandwich_count > 1:
    print(f'Total price for {sandwich_count} sandwiches: €{float(sandwich_price * sandwich_count)}0.')
