pizza_menu = {
    "Margherita": {
        "price": 10.99,
        "size": "Medium",
        "cheese": "Mozzarella"
    },
    "Pepperoni": {
        "price": 13.99,
        "size": "Large",
        "cheese": "Cheddar"
    },
    "Veggie": {
        "price": 11.99,
        "size": "Medium",
        "cheese": "Mozzarella"
    }
}

print("Original Pizza Menu:")
print(pizza_menu)

print("\nPrice of Margherita Pizza:")
print("$", pizza_menu["Margherita"]["price"])

print("\nCheese used in Pepperoni Pizza:")
print(pizza_menu["Pepperoni"]["cheese"])

pizza_menu["Veggie"]["price"] = 12.49
print("\nUpdated price of Veggie Pizza:")
print("$", pizza_menu["Veggie"]["price"])

pizza_menu["BBQ Chicken"] = {
    "price": 15.99,
    "size": "Large",
    "cheese": "Smoked Gouda"
}

print("\nBBQ Chicken Pizza added.")

removed_pizza = pizza_menu.pop("Pepperoni")
print("Pepperoni Pizza removed.")
y
print("\n========== PIZZA MENU ==========")

for pizza_name, pizza_details in pizza_menu.items():
    print("\nPizza:", pizza_name)

    for detail, value in pizza_details.items():
        if detail == "price":
            print("  Price: $" + str(value))
        else:
            print(" ", detail.capitalize() + ":", value)

print("\n================================")