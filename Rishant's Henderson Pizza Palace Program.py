from collections import namedtuple
import sys
import time

# Empty lists to store the orders of user
order_list = []
topping = []

# empty variable for total cost 
order_cost = 0

# empty dictionary for Contact information for delivery
user_info = {}

# Dictionary Pizza to price, key = pizza, value = price
pizza_to_price = {'Classic Cheese': 5.00, 'Classic Veggie': 5.00, 'Pepperoni': 5.00, 'Margherita': 5.00, 'Spicy Paneer': 5.00, 'Tandoori Chicken': 8.50, 'Peri Peri Chicken': 8.50, 'BBQ Chicken': 8.50, 'Garlic Prawn': 8.50, 'Americano': 8.50, 'Supreme': 8.50, 'Spicy Lamb': 8.50,}

# Index of pizza to price
index_to_price = {'1': 5.00, '2': 5.00, '3': 5.00, '4': 5.00, '5': 5.00, '6': 8.50, '7': 8.50, '8': 8.50, '9': 8.50, '10': 8.50, '11': 8.50, '12': 8.50,}

# Index to pizza
index_to_pizza = {'1': '\n- Classic Cheese', '2': '\n- Classic Veggie', '3': '\n- Pepperoni', '4': '\n- Margherita', '5': '\n- Spicy Paneer', '6': '\n- Tandoori Chicken', '7': '\n- Peri Peri Chicken', '8': '\n- BBQ Chicken', '9': '\n- Garlic Prawn', '10': '\n- Americano', '11': '\n- Supreme', '12': '\n- Spicy Lamb'}

# defining namedtuple for pizza menu
menu_entry = namedtuple('menu_entry', ['index','pizza','price'])
pizza_options = []

# appends pizza options to named tuple
pizza_options.append(menu_entry(1, 'Classic Cheese', '$5.00'))
pizza_options.append(menu_entry(2, 'Classic Veggie', '$5.00'))
pizza_options.append(menu_entry(3, 'Pepperoni', '$5.00'))
pizza_options.append(menu_entry(4, 'Margherita', '$5.00'))
pizza_options.append(menu_entry(5, 'Spicy Paneer', '$5.00'))
pizza_options.append(menu_entry(6, 'Tandoori Chicken', '$8.50'))
pizza_options.append(menu_entry(7, 'Peri Peri Chicken', '$8.50'))
pizza_options.append(menu_entry(8, 'BBQ Chicken', '$8.50'))
pizza_options.append(menu_entry(9, 'Garlic Prawn', '$8.50'))
pizza_options.append(menu_entry(10, 'Americano', '$8.50'))
pizza_options.append(menu_entry(11, 'Supreme', '$8.50'))
pizza_options.append(menu_entry(12, 'Spicy Lamb', '$8.50\n'))

# toppings to price list
index_to_topping = {'1': ' + Extra Cheese', '2': ' + Extra Onions', '3': ' + Extra Mushroom', '4': ' + Extra Pepperoni', '5': ' + Extra Olives', '6': ' + Extra Chicken'}

# defining namedtuple for Toppings Menu
topping_entry = namedtuple('topping_entry', ['index','topping','price'])
topping_options = []

# appends topping options to named tuple
topping_options.append(topping_entry(1, 'Extra Cheese', '$0.50'))
topping_options.append(topping_entry(2, 'Extra Onion', '$0.50'))
topping_options.append(topping_entry(3, 'Extra Mushroom', '$0.50'))
topping_options.append(topping_entry(4, 'Extra Pepperoni', '$0.50'))
topping_options.append(topping_entry(5, 'Extra Olives', '$0.50'))
topping_options.append(topping_entry(6, 'Extra Chicken', '$0.50'))

# prints and formats the pizza menu
def pizza_menu():
    for entry in pizza_options:
        index = str(getattr(entry,'index')).ljust(5)
        pizza = getattr(entry,'pizza').ljust(25)
        price = getattr(entry,'price').ljust(7)
        print('{}{}{}'.format(index, pizza, price))

# Prints and formats the topping menu
def topping_menu():
    for entry in topping_options:
        index = str(getattr(entry,'index')).ljust(5)
        topping = getattr(entry,'topping').ljust(25)
        price = getattr(entry,'price').ljust(7)
        print('{}{}{}'.format(index, topping, price))

# Menu function prints out the instructions for the user so they can use a mode option for the Henderson Pizza Palace service.
def main_menu():
  """Prints out the instructions for the user so they can use an action option to use the Henderson Pizza Palace service."""
  print("\nType: \n")
  print("'1' to view action menu\n")
  print("'2' to view pizza menu\n")
  print("'3' to order pizza\n")
  print("'4' to cancel ordering\n")
