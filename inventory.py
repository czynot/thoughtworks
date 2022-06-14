from gst import GST
from item import Item
from cost import Cost
from charge import Charge

class Inventory:

    dic = { "pizza" : Item("Pizza", 150),
            "burger" : Item("Burger", 100),
            "coke": Item("Coke", 50)
            }

    def parseItems(items):
        objects = []
        for item in items:
            objects.append(Inventory.dic[item])
        return objects





