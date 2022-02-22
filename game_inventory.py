
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


def main():
    inventory = {}
    import_inventory(inventory, 'test_inventory.csv')


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    pass


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    pass


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
