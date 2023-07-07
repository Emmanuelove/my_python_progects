#Pizza delivery code

import os
print("Welcome to Dominos pizza delivery system")

while True:
    size = input("What size of pizza do you want?\n\nSelect:\n\n'S' for Small\n\n'M' for Medium\n\n'L' for Large\n\n")
    os.system('cls')
    if size not in ("S","M","L"):
         print("Please select a valid size!")
         continue
    if size == "S":
            price = 15
    if size == "M":
            price = 20
    if size == "L":
            price = 25
    else: 
         print("Select the appropriate size")

    break
     
        
pizza_price=int(price)

while True:
    add_perpperoni = input("\nDo you want pepperoni?\n\n")
    os.system('cls')
    if add_perpperoni not in ("Y","N"):
         print("Please select 'Y' for 'Yes' or 'N' for 'No'\n")
         continue
    if add_perpperoni == 'Y':
         if size == 'S':
           price = 2
         elif size == 'M' or 'L':
           price = 3
    elif add_perpperoni == "N":
     price = 0
    break
pepperoni_price =int(price)
while True:
    extra_cheese = input("\nDo you want extra cheese?\n\n")
    os.system('cls')
    if extra_cheese not in ("Y","N"):
          print("\nPlease select 'Y' for 'Yes' or 'N' for 'No'\n")
          continue
    if extra_cheese == "Y":
         price = 1
    elif extra_cheese == "N":
        price = 0
    break

cheese_price = int(price)


total_price = int(pizza_price + pepperoni_price + cheese_price)
print(f"\nYour total price is ${total_price}")

while True:
    double_order = input("\nWould you like to double your order?\nY or N\n\n")
    if double_order not in ("Y","N"):
         print("Please select a valid answer!\n")
         continue
    if double_order == "N":
         print("\nThank you and have a nice day")
         exit()
    elif double_order == "Y":
        while True:
                try:
                    order_no = int(input("\nHow many times would you like to place this order?\n\n"))
                    break
                except ValueError:
                     print("Please input a number!\n")
        
    break

final_price = order_no * total_price
print(f"\nYour final bill for ordering the same food {order_no} times is ${final_price}")
print("\n\nThank you and have a nice day")
        
                 
