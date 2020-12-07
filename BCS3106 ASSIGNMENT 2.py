def processOrder(item_list, order, quantity):
    global total
    if quantity > item_list[2]:
        print("The food item is currently unavailable!")
        pass
    else:
        total += item_list[2] * quantity
        item_list[2] -= quantity

total = 300

F = ["Starter Course", float(150.50), 50], ["Main Course", float(200.00), 200]

print("Welcome to our restaurant")
print("[1]", F[1][0:2],
      "\n[2]", F[1][0:2],
      "\n[2]", F[1][0:2])

while True:
    choice, quantity = (input("\nWhat would you like to order, the starter course or the main course?\n")).upper(), str(input("\nAre you certain with your choice or would you like to cancel the order?[yes, no]\n")).upper()
    
    if F == "[1]":
        processOrder(quantity, F[0])
    elif choice == "Main Course":
        processOrder(quantity, F[0])
    elif choice == "Dessert":
        processOrder(quantity, F[0])
    else:
        print("If yes, Your Order has been successfully cancelled!\n If no, your order is being processed!")

        more_items = (input("Would you like to order something else?")).lower()
        if more_items == "YES":
            pass
        else:
            break

print("Thank you for ordering!\nYour total cost is: $" + str(total))
        
    
