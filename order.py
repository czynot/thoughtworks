from cost import Cost
from gst import GST
from charge import Charge


from inventory import Inventory

class Order:
    def calculateBill(items):
        """
        :param items: list of strings in the order
        """
        orderList = Inventory.parseItems(items)


        cost = Cost.getCost(orderList)
        gst = GST.getGST(cost)
        charges = Charge.getCharge(1, 0, 1)

        amount = cost + gst + charges
        print(cost, gst, charges)
        print(amount)

inputList = ["pizza", "burger"]

Order.calculateBill(inputList)