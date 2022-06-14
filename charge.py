class Charge:
    def getCharge(specialDay, peakHour, nightOrder):
        """
        :param specialDay: 1 if it is a special day, else 0
        :param peakHour: 1 if it is peak hour order, else 0
        :param nightOrder: 1 if it is a night order, else 0
        :returns: delivery charges for the order
        """

        charges = 0
        if specialDay or peakHour or nightOrder:
            if specialDay:
                charges += 50
            if peakHour:
                charges += 30
            if nightOrder:
                charges += 20
        else:
            return 20
        return charges