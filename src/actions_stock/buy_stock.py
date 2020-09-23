import sys
sys.path.append("..")
import analys_stock
import config as cfg
import pandas as pd
import matplotlib.pyplot as plt
AST = analys_stock.AnaStock(cfg=cfg)

class BuyStock:
    def __init__(self, stock_price, before_cash_amount,
            before_stock_num, dif_price = 0):

        # 实时股价
        self.stock_price = stock_price

        # 买前现金
        self.before_cash_amount = before_cash_amount

        # 买前股数
        self.before_stock_num = before_stock_num

        # 报买差价
        self.dif_price = dif_price

    def quotes_price(self):
        # 报买价 = 实时股价 - 报买差价
        self.quotes_price = self.stock_price + self.dif_price
        return self.quotes_price

    def buy_price(self):
        # 实际买价 = 报买价
        self.buy_price = self.quotes_price

        return self.quotes_price


    def prepare_buy(self):
        # 报买
        self.quotes_price()
        self.buy_price()

        # 预计买入股数
        self.buy_stock_num = int(self.before_cash_amount / (100 * self.buy_price))*100

        # 预计买股现金
        self.buy_cash_amount = self.buy_stock_num * self.buy_price

        # 预计佣金
        # 买入: 买股现金数 * 0.0006
        self.buy_commission = self.buy_cash_amount * 0.0006

        # 账户补充
        self.account_add_cash = 0


        # 买后现金 = 买前现金 - 买股现金 - 佣金
        # 预买后现金
        self.after_cash_amount = self.before_cash_amount - self.buy_cash_amount - self.buy_commission

        # 注: 若买后现金数 < 0 ，
        # /方案1：则账户补充 =  -买后现金数， 买后现金数 = 0
        # /【未启用】方案2：无账户补充， 更新买入股数少持一手， 然后更新买股现金、 佣金、买后现金

        if self.after_cash_amount < 0:
            self.account_add_cash = - self.after_cash_amount
            self.after_cash_amount = 0

        # 买后股数
        self.after_stock_num = self.before_stock_num + self.buy_stock_num

        # 买后总资产
        self.after_assets = self.stock_price * self.after_stock_num + self.after_cash_amount


    def get_assets(self):
        # 总资产
        self.assets = self.stock_price * self.stock_num + self.cash_amount


    def strategy(self):
        #4 策略
        """
        每天close时候buy， 次日高于close的价格的 r = 0.005 时候sale
        如果这一天都没有r = 0.005的情况，就继续hold

        这里r 可以学习前6月得到,用最后2个月来测试
        """
        principal = 100000


if __name__ == '__main__':
    SS = BuyStock(stock_price=6, before_cash_amount=100000, before_stock_num=1000, dif_price=0.1)
    SS.prepare_buy()
    # SS.after_assets()
    print(SS.stock_price, SS.buy_price)
    print(SS.account_add_cash, SS.buy_commission, SS.after_cash_amount, SS.after_stock_num, SS.after_assets)