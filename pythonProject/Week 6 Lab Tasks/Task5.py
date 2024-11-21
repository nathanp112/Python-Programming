owner_inventory = {
    "fruits": ["apple", "banana"],
    "vegetables": ["carrot", "lettuce"],
    "dairy": ["milk", "cheese"]
}

vendor_inventory = {
    "fruits": ["apple", "grapes"],
    "vegetables": ["carrot", "tomato"],
    "dairy": ["milk", "yogurt"]
}

owner_only = []
for category, items in owner_inventory.items():
    for item in items:
        if item not in vendor_inventory.get(category, []):
            owner_only.append(item)
            print("Owner Only Items Are: ", owner_only)

common_items =[]
for category, items in owner_inventory.items():
    common_items.append(set(items).intersection(set(vendor_inventory.get(category, []))))
    print("Common Items Are: ", common_items)

user_item = input("Enter the item: ", )
is_in_stock = False
for items in owner_inventory.values():
    if user_item in items:
        is_in_stock = True
        break
if is_in_stock:
    print("Item is in stock!")
else:
    print("Item is not in stock")

user_item = input("Enter the item: ", )
is_in_stock = False
for items in vendor_inventory.values():
    if user_item in items:
        is_in_stock = True
        break
if is_in_stock:
    print("Item is in stock!")
else:
    print("Item is not in stock")