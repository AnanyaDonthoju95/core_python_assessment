def update_menu(menu, add_item=None, remove_item=None, check_item=None):
    if add_item:
        menu.append(add_item)
    if remove_item and remove_item in menu:
        menu.remove(remove_item)
    elif remove_item:
        print(f"{remove_item} does not exist in the menu.")
    
    if check_item:
        availability = f"{check_item} is available" if check_item in menu else f"{check_item} is not available"
        return menu, availability
    return menu

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
menu, availability = update_menu(initial_menu, add_item="Tacos", remove_item="Salad", check_item="Pizza")
print(f"Updated menu: {menu}")
print(f"Availability: {availability}")
