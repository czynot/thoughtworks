class Cost():

    def getCost(items): 

        """
        :param items: array of Item type objects
        :returns: total cost of the order
        """
        cost = 0
        for item in items: 
            cost += item.getPrice()
        return cost
        