
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


def main():
    # inventory = {}
    # import_inventory(inventory, 'test_inventory.csv')
    # display_inventory(inventory)
    # loot = ['sword', 'ork tooth', 'fms', 'fms', 'fms']
    inventory = {'rope': 1, 'torch': 6}
    added_items = ['torch', 'torch', 'torch', 'fms', 'fms']
    add_to_inventory(inventory, added_items)


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    if inventory:
        for key, value in inventory.items():
            print(key + ':', value)
    

def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if item in inventory:
            new_value = inventory[item] + 1
            inventory.update({item : new_value})  
        inventory.setdefault(item, added_items.count(item))
    return inventory
    

def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    pass


def print_table(inventory, order=None):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """

    pass


def import_inventory(inventory, filename = 'import_inventory.csv'):
    """Import new inventory items from a CSV file."""
    try:
        with open(filename, "r") as file:
            items_list = file.readline().split(",")
        for element in items_list:
            inventory.setdefault(element, items_list.count(element))
        return inventory
    except FileNotFoundError:
        print(f"File '{filename}' not found!")


def export_inventory(inventory, filename = 'export_inventory.csv'):
    """Export the inventory into a CSV file."""
    try:
        items_list = list(inventory.keys())
        with open(filename, "w") as file:
            for item in items_list:
                if item != items_list[-1]:
                    item = ((item + '\t') * inventory[item]).replace('\t', ',')
                file.write(item)
    except OSError:
        print(f"You don't have permission creating file '{filename}'!")


if __name__ == "__main__":
    main()
