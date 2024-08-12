# ID: 2083568
# Name: Ugwueze Eze

from FinalProjectFileManager import FileManager
from FinalProjectInventoryManager import InventoryManager


# create main method
def main():
    inventory, item_types = FileManager.read_csv_files()
    manager = InventoryManager(inventory, item_types)

    # generate the inventory reports with .csv
    manager.generate_full_inventory()
    manager.generate_item_type_inventory()
    manager.generate_past_service_date_inventory()
    manager.generate_damaged_inventory()

    # Show the success message to the user
    print("Reports are generated successfully!")


if __name__ == '__main__':
    main()
