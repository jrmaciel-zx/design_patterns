from abc import ABCMeta, abstractmethod

class Order(metaclass = ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()

class StockTrade():
    def buy(self):
        print("Você está comprando ações")

    def sell(self):
        print("Você está vendendo ações")

class Agent():
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

if __name__ == '__main__':
    #Cliente
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    #Chamador
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
