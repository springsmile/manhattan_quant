class Stock:
    def __init__(self, stock_code, stock_price, stock_num):
        self.stock_code = stock_code
        self.stock_price = stock_price
        self.stock_num = stock_num

    def stock_value(self):
        self.stock_value = self.stock_price * self.stock_num
        return self.stock_value


class Account:
    # 假设只持有一支股票
    def __init__(self, cash_amount, stocks, account_id = 'tkq'):
        self.cash_amount = cash_amount
        self.stocks = stocks
        self.account_id = account_id

    def all_stock_value(self):
        self.all_stock_value = 0
        for stock in self.stocks:
            stock.stock_value()
            self.all_stock_value += stock.stock_value
        return self.all_stock_value

    def account_assets(self):
        self.all_stock_value()
        self.account_assets = self.all_stock_value + self.cash_amount
        return self.account_assets


def stock_test():
    S = Stock(stock_code='1', stock_price=6.0, stock_num=1000)
    A = Account(cash_amount=10000, stocks = [S])
    print(A.cash_amount)
    A.account_assets()
    print(A.account_assets)

if __name__ == '__main__':
    stock_test()
