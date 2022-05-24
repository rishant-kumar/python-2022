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
pizza_to_price = {'Classic Cheese': 8.50, 'Classic Veggie': 8.50, 'Pepperoni': 8.50, 'Margherita': 8.50, 'Spicy Paneer': 8.50, 'Tandoori Chicken': 13.50, 'Peri Peri Chicken': 13.50, 'BBQ Chicken': 13.50, 'Garlic Prawn': 13.50, 'Americano': 8.50, 'Supreme': 8.50, 'Spicy Lamb': 13.50,}

# Index of pizza to price
index_to_price = {'1': 8.50, '2': 8.50, '3': 8.50, '4': 8.50, '5': 8.50, '6': 13.50, '7': 13.50, '8': 13.50, '9': 13.50, '10': 13.50, '11': 13.50, '12': 13.50,}

# Index to pizza
index_to_pizza = {'1': '\n- Classic Cheese', '2': '\n- Classic Veggie', '3': '\n- Pepperoni', '4': '\n- Margherita', '5': '\n- Spicy Paneer', '6': '\n- Americano', '7': '\n- Supreme', '8': '\n- BBQ Chicken', '9': '\n- Garlic Prawn', '10': '\n- Tandoori Chicken', '11': '\n- Peri Peri Chicken', '12': '\n- Spicy Lamb'}

# defining namedtuple for pizza menu
menu_entry = namedtuple('menu_entry', ['index','pizza','price'])
pizza_options = []

# appends pizza options to named tuple
pizza_options.append(menu_entry(1, 'Classic Cheese', '$8.50'))
pizza_options.append(menu_entry(2, 'Classic Veggie', '$8.50'))
pizza_options.append(menu_entry(3, 'Pepperoni', '$8.50'))
pizza_options.append(menu_entry(4, 'Margherita', '$8.50'))
pizza_options.append(menu_entry(5, 'Spicy Paneer', '$8.50'))
pizza_options.append(menu_entry(6, 'Americano', '$13.50'))
pizza_options.append(menu_entry(7, 'Supreme', '$13.50'))
pizza_options.append(menu_entry(8, 'BBQ Chicken', '$13.50'))
pizza_options.append(menu_entry(9, 'Garlic Prawn', '$13.50'))
pizza_options.append(menu_entry(10, 'Tandoori Chicken', '$13.50'))
pizza_options.append(menu_entry(11, 'Peri Peri Chicken', '$13.50'))
pizza_options.append(menu_entry(12, 'Spicy Lamb', '$13.50\n'))

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
  global service_option
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
            print("\nYou have entered no name and no address! Please enter them for contacting purposes.\n")
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
            continue

          # when the user enters 'yes'
          elif correct_information == "yes" or correct_information == 'y':
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
          if len(name) <=0:
            print("You have entered no name! Please enter one for contating purposes.")
            continue

          else:
            for key, value in user_info.items():
              print(key, ':', value)

            print("\nIs the contact information shown above correct?")
            correct_information = input("Answer ('yes' or 'no'):  ").strip().lower()

            if correct_information == "no" or correct_information == 'n':
              print("\nPlease resubmit your name for contacting purposes!")
              time.sleep(1)
              continue

            elif correct_information == "yes" or correct_information == 'y':
              # exit loops
              break
            
      # heads back to main menu by exiting loop when user enters '3'
      elif service_option == "3":   
        print("Heading back to Main menu...")
        time.sleep(1)
        main_menu()
        break
        

      else:
        print("\nPlease input a valid number ('1', '2' or '3'))\n")
        continue
      
      service_repeat = False
  
  time.sleep(1)

# Function that takes in the users orders 
def order(order_cost, topping):
  ordering = True
  while ordering:
    pizza_menu()
    print("\nOrder using the number next to the name of the pizza.")
    time.sleep(0.5)
    print("To finish ordering, type 'end'.")
    time.sleep(0.5)
    print("To cancel ordering, type 'cancel'.")
    time.sleep(0.5)
    new_order = input("\nInput Pizza number here: ")

    # when user enters 'end', prints users order, cost, user info and also confirms order 
    if new_order == "end":
        print("\nContact Information:\n")
        for key, value in user_info.items():
              print(key, ':', value)
        # shows the user their order
        print("\nYour order is:\n")
        view_order()
        print("\nTotal cost of order is: ${}".format(order_cost))

        correct_order = input("\nIs your order correct? (Please input 'yes' or 'no'): ").strip().lower()
        # when the user confirms order, then 
        if correct_order == "yes" or correct_order == 'y':
            print("\nYour order will be ready soon! Thanks for ordering at Henderson Pizza Palace!\n")
            # clears order list
            order_list.clear()
            main_menu()
            break
        # if the order is incorrect, the order list will be cleared
        elif correct_order == "no" or correct_order == 'n':
            order_list.clear()
            continue
        else:
          print("Please enter 'yes' or 'no'")

    # if number in index_to_pizza dictionary, then pizza name is appended to order_list        
    elif new_order in index_to_pizza:
        order_list.append(index_to_pizza.get(new_order))
        # if the number entered by user is associate with a pizza, then price will be added and will move on to toppings
        if new_order in index_to_price:
            # adds cost of pizza to order_cost
            order_cost += index_to_price.get(new_order)
            topping_menu()
            time.sleep(1)
            print("\nAdd toppings using the number next to the name of the topping.")
            time.sleep(1)
            print("To finish adding toppings, type 'end'.")

            while True:
                topping = input("\nInput topping number here: ").strip()
                if topping in index_to_topping:
                    order_list.append(index_to_topping.get(topping))
                    order_cost += 0.5
                elif topping == "end":
                    print("\nCurrent total cost of order is: ${}".format(order_cost))
                    break
                else:
                    print("\nThat is not one of the topping options!\n")

    # when user enters 'cancel', they will be sent back to the main menu and order_list will be cleared
    elif new_order == "cancel":
        order_list.clear()
        main_menu()
        break

    else:
        print("\nSorry, that is not one of the pizza options\n")
        continue

  return order_cost

# Function that shows current orders in the order_list
def view_order():
  if len(order_list) > 0:
    for order in order_list:
      print("{}".format(order, topping))
  else:
    print("You have no orders yet!")


# Running main program loop (calling functions etc)
print("Henderson Pizza Palace\n")
print("\nHello, Welcome to Henderson Pizza Palace text-based ordering system.\nBelow is our Main menu, please enter a number associated with your required service.")

# Prints main menu
main_menu()

repeat = True
while repeat:
  # Ask user for number input
  main_menu_option = input("\nInput number Here: ").strip()

  # Checking input and calls appropriate function - this one calls the food menus
  if main_menu_option == "1":
    pizza_menu()
    time.sleep(1)
    topping_menu()
    time.sleep(1)
    main_menu()

# this one calls the food menus
  elif main_menu_option == "2":
    time.sleep(1)
    servicing_menu(order_cost)
    if service_option == '3':
      continue
    order(order_cost, topping)

  elif main_menu_option == "3":

    if len(order_list) > 0:
      print("Thanks for purchasing from Henderson Pizza Palace! \nHope to see you again!")
    else:
      print("Thanks for visiting!")
    repeat = False

  else:
    print("'{}' wasn't an option\n".format(main_menu_option))
