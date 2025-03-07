def cancel(cart):
    """Function to modify or remove items from the cart before checkout."""
    while True:
        print("\nYour current cart:")
        for key, (name, quantity, price) in cart.items():
            print(f"{key}. {name} x{quantity} - ₹{quantity * price}")
             # Recalculate and display the updated total price
        updated_totalprice = sum(item[1] * item[2] for item in cart.values())
        print(f"\nTotal price: ₹{updated_totalprice}")

        try:
            modify = int(input("\nEnter the product number to modify or remove (0 to continue to checkout): "))
        except ValueError:
            print("Invalid input! Please enter a valid product number.")
            continue

        if modify == 0:
            break  # Exit the modification loop and continue to payment

        if cart.get(modify):
            action = input("Do you want to (R)emove or (M)odify the quantity? ").lower()
            if action == 'r':
                del cart[modify]
                print("Item removed from cart.")
            elif action == 'm':
                try:
                    new_quantity = int(input("Enter new quantity: "))
                    if new_quantity > 0:
                        cart[modify][1] = new_quantity
                        print(f"Quantity updated to {new_quantity}.")
                    else:
                        print("Invalid quantity! Removing item from cart.")
                        del cart[modify]
                except ValueError:
                    print("Invalid input! Quantity must be a number.")
        else:
            print("Item not found in cart!")

        print("\nCart after modification:", cart)

def vending_machine():
    """Main vending machine program."""
    while True:
        prod_dic = {
            1: ("Pepsi", 20),
            2: ("Limca", 18),
            3: ("Maza", 22),
            4: ("DairyMilk", 40),
            5: ("GreenLays", 20)
        }

        print("\"Products available in vending machine\"")
        for key, (name, price) in prod_dic.items():
            print(f"{key}. {name} - ₹{price}")
        print("")

        cart = {}

        while True:
            try:
                product_number = int(input("\nChoose the product number to buy (or enter \'0\' to finish selection): "))
            except ValueError:
                print("Invalid input! Please enter a valid product number.")
                continue

            if product_number == 0:
                if not cart:
                    print("\nNo products selected. Do you want to restart? (Y/N)")
                    restart = input().lower()
                    if restart == 'y':
                        print("\nRestarting program...\n")
                        return vending_machine()
                    else:
                        print("Exited. Thank you!")
                        return
                else:
                    break

            if product_number in prod_dic:
                product_name, price = prod_dic[product_number]
                try:
                    quantity = int(input(f"Enter quantity for {product_name}: "))
                    if quantity <= 0:
                        print("Invalid quantity! Please enter a number greater than 0.")
                        continue
                except ValueError:
                    print("Invalid input! Quantity must be a number.")
                    continue

                if product_number in cart:
                    cart[product_number][1] += quantity
                else:
                    cart[product_number] = [product_name, quantity, price]

                total_price = price * quantity
                print(f"Added {quantity} {product_name}(s) to cart. Price: ₹{total_price}")
            else:
                print("Invalid product number! Please try again.")

        # Display total amount before payment
        final_total = sum(item[1] * item[2] for item in cart.values())
        print(f"\nTotal amount to pay: ₹{final_total}")

        # Call the cancel() function before payment
        modify_cart = input("Do you want to modify or cancel any item before payment? (Y/N): ").lower()
        if modify_cart == 'y':
            cancel(cart)  # Call the function to modify the cart

        # Recalculate total after modifications
        final_total = sum(item[1] * item[2] for item in cart.values())
        if final_total == 0:
            print("Cart is empty after modifications. Restarting program...\n")
            return vending_machine()

        # Payment logic
        money = 0
        while money < final_total:
            try:
                amount = int(input("Enter the money-₹"))
                money += amount
            except ValueError:
                print("Invalid input! Please enter a valid amount.")
                continue

            if money < final_total:
                req_money = final_total - money
                print(f"Sorry, you need ₹{req_money} more.")
                vare = input("Enter \'Y\' if you still want to purchase the product else enter \'N\' to exit'\n").lower()
                while (vare != "y" and vare != "n"):
                    vard = input("Invalid! please enter Y/N - ")
                    vare = vard
                if vare == "1":
                    pass
                elif vare == "2":
                    print(f"Please collect the cash ₹{money}\nThank You")
                    break
                    

        # Give product and change if applicable
        if money == final_total:
            print("Take the Product")
        elif money > final_total:
            print(f"Take the product and collect your change ₹{money - final_total}")

        # Ask if user wants to continue
        nun = input("Do you want to purchase more? Press '#' to continue or '*' to exit: ")
        while nun not in ("#", "*"):
            nun = input("Invalid! Please enter '#' or '*': ")

        if nun == "#":
            print("\nRestarting program...\n")
            return vending_machine()
        elif nun == "*":
            print("Thank you for using the vending machine!")
            break

# Start the vending machine
vending_machine()
