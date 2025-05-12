class FruitShop:

    def __init__(self, name, fruitPrices):
        """
            name: Name of the fruit shop
            fruitPrices: Dictionary with keys as fruit strings and prices for values
                         e.g. {'apples':2.00, 'oranges': 1.50, 'pears': 1.75}
        """
        self.fruitPrices = fruitPrices
        self.name = name
        print('Welcome to %s fruit shop' % (name))

    def getCostPerPound(self, fruit):
        """
            fruit: Fruit string
        Returns cost of 'fruit', assuming 'fruit' is in our inventory or None otherwise
        """
        if fruit not in self.fruitPrices:
            return None
        return self.fruitPrices[fruit]

    def getPriceOfOrder(self, orderList):
        """
            orderList: List of (fruit, numPounds) tuples
        Returns cost of orderList, only including the values of fruits that this fruit shop has.
        """
        totalCost = 0.0
        for fruit, numPounds in orderList:
            costPerPound = self.getCostPerPound(fruit)
            if costPerPound is not None:
                totalCost += numPounds * costPerPound
        return totalCost

    def getName(self):
        return self.name

    def __str__(self):
        return "<FruitShop: %s>" % self.getName()

    def __repr__(self):
        return str(self)



if __name__ == '__main__':
    # Sample fruit prices
    fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}
    
    # Create a FruitShop instance
    shop = FruitShop('Fresh Fruits', fruitPrices)
    
    # Sample order list
    orderList = [('apples', 2.0), ('pears', 3.0), ('bananas', 2.0)]  # 'bananas' not in shop
    
    # Get total price of the order
    totalCost = shop.getPriceOfOrder(orderList)
    
    print("Total cost of the order:", totalCost)
