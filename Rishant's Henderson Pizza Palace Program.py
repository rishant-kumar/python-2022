from collections import namedtuple
from pickle import FALSE
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
  print("\nOur selection of pizzas")
  for entry in pizza_options:
      index = str(getattr(entry,'index')).ljust(5)
      pizza = getattr(entry,'pizza').ljust(25)
      price = getattr(entry,'price').ljust(7)
      print('{}{}{}'.format(index, pizza, price))

# Prints and formats the topping menu
def topping_menu():
  print("\nOur selection of toppings")
  for entry in topping_options:
    index = str(getattr(entry,'index')).ljust(5)
    topping = getattr(entry,'topping').ljust(25)
    price = getattr(entry,'price').ljust(7)
    print('{}{}{}'.format(index, topping, price))

# Menu function prints out the instructions for the user so they can use a mode option for the Henderson Pizza Palace service.
def main_menu():
  """Prints out the instructions for the user so they can use an action option to use the Henderson Pizza Palace service."""
  print("\nType: \n")
  print("'1' to view pizza menu\n")
  print("'2' to order pizza\n")
  print("'3' to cancel ordering\n")

# Menu function prints out the instructions for the user so they can use a service option for the Henderson Pizza Palace service.
def servicing_menu(order_cost):
  """Prints out the instructions for the user so they can use a service option for the Henderson Pizza Palace service."""
  print("\nHow would you like to receive your pizza?\n")
  print("'1' Delivery ($3 Delivery charge)\n")
  print("'2' Pick-up\n")
  print("'3' Go back to main menu\n")

  service_repeat = True
  while service_repeat:
      service_option = input("\nInput number here: ").strip()
      # Asks the user to input address and phone number
      # Will ask if contact information is correct
      # Will remove contact information and repeat if user inputs "no"
      if service_option == "1":
        print("\nService Option: Delivery\n")
        time.sleep(1)
        # adds $3 to user order cost as delivery has $3 charge
        order_cost += 3

        contact_repeat = True
        while contact_repeat:
          # error prevention
          try:
            phone_number = int(input("Please state your phone number: ").strip())
          except ValueError:
            # tells user to enter an appropriate integer and goes back to phone number input
            print("\nPlease input integers only!\n")
            continue
          # adds user phone number to user_info dictionary
          user_info['Phone number'] = phone_number
          
        
          address = input("\nPlease enter your delivery address: ").strip()
          user_info['Address'] = address.title()
            
          name = input("\nPlease enter your name: ").strip()
          user_info['Name'] = name.title()

          if len(name) <= 0 and len(address) <= 0:
            print("\nYou have entered no name or address, please enter your contact information!\n")
            continue

          else:
            print("\nYour Contact Information:")
            # prints user info dictionary
            for key, value in user_info.items():
              print(key, ':', value)
            
          print("\nIs the contact information shown above correct?")
          correct_information = input("Answer ('yes' or 'no'):  ").strip().lower()

          if correct_information == "no" or correct_information == 'n':
            print("\nPlease resubmit your contact information")
            time.sleep(1)
            contact_repeat = True
                
          # when the user enters 'yes'
          elif correct_information == "yes" or correct_information == 'y':
            # calls pizza and topping menu functions
            time.sleep(1)
            pizza_menu()
            time.sleep(1)
            topping_menu()
            # exit loops
            break

          # if user does not say either 'yes' or 'no'
          else:
            print("\nPlease enter a valid response ('yes' or 'no')!")

      elif service_option == "2":
        print("\nService Option: Pick-up\n")
        time.sleep(1)

        while True:
          name = input("\nPlease enter your name: ").strip()
          # adds users name to dictionary
          user_info['Name'] = name.title()
          # prints user info
          for key, value in user_info.items():
            print(key, ':', value)

          print("\nIs the contact information shown above correct?")
          correct_information = input("Answer ('yes' or 'no'):  ").strip().lower()

          if correct_information == "no" or correct_information == 'n':
            print("\nPlease resubmit your name for contacting purposes!")
            time.sleep(1)
            continue

          elif correct_information == "yes" or correct_information == 'y':
            time.sleep(1)
            pizza_menu()
            time.sleep(1)
            topping_menu()
            # exit all loops
            break
            

      elif service_option == "3":
        main_menu()

      else:
        print("\nPlease input a valid number ('1', '2' or '3'))\n")
      
      service_repeat = False
  time.sleep(10)
