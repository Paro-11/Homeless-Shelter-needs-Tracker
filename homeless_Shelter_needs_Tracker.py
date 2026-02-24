import json

try:
    with open("inventory.json", "r") as f:
        inventory = json.load(f)
except:
    inventory = {}

def save_inventory():
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

def add_donation(item, quantity):
    if quantity <= 0:
        print(" Quantity must be greater than 0")
        return

    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

    save_inventory()
    print(f"Added {quantity} {item}(s)")

def donations_out(item, quantity):
    if item not in inventory:
        inventory[item] = 0

    if quantity <= 0:
        print(" Quantity must be greater than 0")
        return

    if inventory[item] - quantity < 0:
        print(f" Cannot deduct. Available {item}: {inventory[item]}")
        return

    inventory[item] -= quantity
    save_inventory()
    print(f"{quantity} {item}(s) deducted")

def check_shortages(minimum=10):
    print("\nItems in Shortage:")
    found = False
    for item, qty in inventory.items():
        if qty < minimum:
            print(f"- {item}: {qty}")
            found = True
    if not found:
        print("No items in shortage.")
    print()

while True:
    print("\n1. Add Donation- blankets,food packets,rice,oil")
    print("2. Check Shortages")
    print("3. Donations Out")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        add_donation(item, quantity)

    elif choice == "2":
        minimum = int(input("Enter minimum stock level: "))
        check_shortages(minimum)

    elif choice == "3":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity to deduct: "))
        donations_out(item, quantity)

    elif choice == "4":
        print("Inventory saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")