# ID: 2083568
# Name: Ugwueze Eze

import csv
from FinalProjectInventoryItem import InventoryItem
from datetime import datetime

# This is the file manager class
class FileManager:
    @staticmethod
    def read_csv_files():
        inventory = {}
        item_types = {}

        # open and read the Manufacturer.csv file and store inventory in the dictionary
        with open('ManufacturerList.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id = row[0]
                manufacturer = row[1]
                item_type = row[2]
                damaged = True if len(row) > 3 and row[3].lower() == 'damaged' else False

                inventory[item_id] = InventoryItem(item_id, manufacturer, item_type, None, None, damaged)

                if item_type not in item_types:
                    item_types[item_type] = []
                item_types[item_type].append(item_id)

        # open and read the PriceList.csv file and store inventory in the dictionary
        with open('PriceList.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id = row[0]
                price = row[1]

                if item_id in inventory:
                    inventory[item_id].price = float(price)

        # open and read the ServiceDatesList.csv file and store inventory in the dictionary
        with open('ServiceDatesList.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id = row[0]
                service_date_str = row[1]

                if item_id in inventory:
                    try:
                        service_date = datetime.strptime(service_date_str, '%m/%d/%Y')
                        inventory[item_id].service_date = service_date
                    except ValueError:
                        inventory[item_id].service_date = None

        # return the inventory and item types dictionaries
        return inventory, item_types
