"""
    production code
"""


class Checkout:
    class Discount:
        def __init__(self, nbritems, price):
            self.nbritems = nbritems
            self.price = price

    def add_discount(self, item, nbritems, price):
        discount = self.Discount(nbritems, price)
        self.discounts[item] = discount

    def __init__(self):
        self.prices = {}  # item: price
        self.items = {}  # item: quantity
        self.discounts = {}  # item: discountObj

    def add_item_price(self, item, price):
        self.prices[item] = price

    def is_item_exists(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")

    def add_item(self, item):
        self.is_item_exists(item)
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def cal_total(self):
        total = 0
        for item, count in self.items.items():
            total += self.calc_item_total(item, count)
        return total

    def calc_item_total(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.nbritems:
                total += self.calc_item_discount_total(item, count, discount)
            else:
                total = self.prices[item] * count
        else:
            total += self.prices[item] * count
        return total

    def calc_item_discount_total(self, item, count, discount):
        total = 0
        nbr_of_discount = count / discount.nbritems
        total += nbr_of_discount * discount.price
        remaining = count % discount.nbritems
        total += remaining * self.prices[item]
        return total
