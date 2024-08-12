# ID: 2083568
# Name: Ugwueze Eze

import csv
from datetime import datetime


# This is the inventory manager class
class InventoryManager:
    def __init__(self, inventory, item_types):
        self.inventory = inventory
        self.item_types = item_types

    # generate the full inventory .csv file in the report folder
    def generate_full_inventory(self):
        sorted_items = sorted(self.inventory.values(), key=lambda x: x.manufacturer)
        with open("reports/FullInventory.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            for item in sorted_items:
                writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date.strftime('%m/%d/%Y'), 'damaged' if item.damaged else ''])

    # generate the item type inventory .csv file in the report folder
    def generate_item_type_inventory(self):
        for item_type, item_ids in self.item_types.items():
            with open(f'reports/{item_type}Inventory.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for item_id in sorted(item_ids):
                    item = self.inventory[item_id]
                    writer.writerow([item.item_id, item.manufacturer, item.price, item.service_date.strftime('%m/%d/%Y'), 'damaged' if item.damaged else ''])

    # generate the past service date inventory .csv file in the report folder
    def generate_past_service_date_inventory(self):
        current_date = datetime.now()
        past_service_items = {item_id: item for item_id, item in self.inventory.items() if item.service_date < current_date}
        sorted_items = sorted(past_service_items.values(), key=lambda x: x.service_date)

        with open('reports/PastServiceDateInventory.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for item in sorted_items:
                writer.writerow(
                        [item.item_id, item.manufacturer, item.item_type, item.price, item.service_date.strftime('%m/%d/%Y'),
                         'damaged' if item.damaged else ''])

    # generate the damaged inventory .csv file in the report folder
    def generate_damaged_inventory(self):
        damaged_items = {item_id: item for item_id, item in self.inventory.items() if item.damaged}
        sorted_items = sorted(damaged_items.values(), key=lambda x: x.price, reverse=True)

        with open('reports/DamagedInventory.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for item in sorted_items:
                writer.writerow(
                    [item.item_id, item.manufacturer, item.item_type, item.price,
                     item.service_date.strftime('%m/%d/%Y')])
