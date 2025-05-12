def buyLotsOfFruit(orderList):
    totalCost=0.0
    fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}
    for fruit,pounds in orderList:
        if fruit in fruitPrices:
            totalCost+=fruitPrices[fruit]*pounds
        else:
            print("Error:",fruit ,"is not available!")
            return None
    return totalCost

if __name__ == '__main__':
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))

    
