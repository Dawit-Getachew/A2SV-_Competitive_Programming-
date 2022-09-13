class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
            self.discount = discount 
            self.repeat = n
            self.temp = n

            self.price = {product:price for product, price in zip(products, prices)}

    def getBill(self, products: List[int], amount: List[int]) -> float:
        total = 0

        for product, quantity in zip(products, amount):
            total += self.price[product] * quantity

        if self.temp > 1:
            self.temp -= 1
            return float(total)
        else:
            self.temp = self.repeat
            return total - (self.discount * total)/100


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)