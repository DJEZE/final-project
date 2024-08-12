# ID: 2083568
# Name: Ugwueze Eze

# This is the class used as the blue-print for inventory item
class InventoryItem:
    def __init__(self, item_id, manufacturer, item_type, price, service_date, damaged):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.damaged = damaged

    def __repr__(self):
        return (f"{self.item_id}, {self.manufacturer}, {self.item_type}, {self.price}, "
                f"{self.service_date.strftime('%m/%d/%Y')}, {self.damaged}")
