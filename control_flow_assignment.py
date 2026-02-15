# -----------------------------------------
# CONTROL FLOW ASSIGNMENT
# -----------------------------------------

# ---------------------------
# TASK 1: Discount Rules
# ---------------------------

print("----- TASK 1 -----")

order_input = input("Enter order amount: ")

if order_input.isdigit():
    order_amount = int(order_input)

    if order_amount >= 2000:
        discount = 15
    elif order_amount >= 1500:
        discount = 10
    elif order_amount >= 1000:
        discount = 7
    else:
        discount = 0

    discount_value = order_amount * discount / 100
    subtotal = order_amount - discount_value
    tax = subtotal * 0.05
    final_total = subtotal + tax

    print("Discount Applied:", discount, "%")
    print("Subtotal:", subtotal)
    print("Tax (5%):", tax)
    print("Final Total:", final_total)

else:
    print("Invalid input. Please enter a numeric value.")
    exit()


# ---------------------------
# TASK 2: Process Multiple Orders
# ---------------------------

print("\n----- TASK 2 -----")

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

for amount in orders:

    if amount >= 2000:
        discount = 15
    elif amount >= 1500:
        discount = 10
    elif amount >= 1000:
        discount = 7
    else:
        discount = 0

    final_amount = amount - (amount * discount / 100)

    if discount > 0:
        discounted_orders += 1

    total_revenue += final_amount

    print("Order:", amount, "Discount:", discount, "%", "Final:", final_amount)

print("Total Revenue After Discounts:", total_revenue)
print("Orders With Discount:", discounted_orders)


# ---------------------------
# TASK 3: User Menu
# ---------------------------

print("\n----- TASK 3 -----")

orders_list = []

while True:
    print("\n1 - Add Order")
    print("2 - Show Orders")
    print("q - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = input("Enter order amount: ")

        if amount.isdigit():
            orders_list.append(int(amount))
            print("Order added.")
        else:
            print("Invalid amount.")
            continue

    elif choice == "2":
        total = 0

        for amount in orders_list:

            if amount >= 2000:
                discount = 15
            elif amount >= 1500:
                discount = 10
            elif amount >= 1000:
                discount = 7
            else:
                discount = 0

            final = amount - (amount * discount / 100)
            total += final

            print("Order:", amount, "Final after discount:", final)

        print("Total:", total)

    elif choice == "q":
        print("Exiting menu...")
        break

    else:
        print("Invalid choice.")
        continue


# ---------------------------
# TASK 5: Loop Control with Conditions
# ---------------------------

print("\n----- TASK 5 -----")

daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily:

    if sale == -1:
        print("Corrupted data found. Stopping processing.")
        break

    if sale == 0:
        print("No sales today. Skipping.")
        continue

    total_sales += sale
    print("Running Total:", total_sales)

print("Final Total Sales:", total_sales)
