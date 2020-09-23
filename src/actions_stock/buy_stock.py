import analys_stock
import config as cfg
import pandas as pd
import matplotlib.pyplot as plt
AST = analys_stock.AnaStock(cfg=cfg)

class BuyStock:
    def __init__(self, cfg):
        self.cfg = cfg

    def buy(self, stock_price, before_cash_amount,
            before_stock_num, dif_price = 0):
        # 实时股价
        self.stock_price = stock_price

        # 报买价
        self.buy_price = self.stock_price - dif_price

        # 买前现金
        self.before_cash_amount = before_cash_amount

        # 买前股数
        self.before_stock_num = before_stock_num

        # 买入股数
        self.buy_stock_num = int(self.before_cash_amount / (100 * self.buy_price))*100

        # 买股现金
        self.buy_cash_amount = self.buy_stock_num * self.buy_price

        # 佣金
        # 买入: 买股现金数 * 0.0006
        self.buy_commission = self.buy_cash_amount * 0.0006

        # 账户补充
        self.account_add_cash = 0


        # 买后现金 = 买前现金 - 买股现金 - 佣金
        # 注: 若买后现金数 < 0 ，
        # /方案1：则账户补充 =  -买后现金数， 买后现金数 = 0
        # /【未启用】方案2：无账户补充， 更新买入股数少持一手， 然后更新买股现金、 佣金、买后现金

        self.after_cash_amount = self.before_cash_amount - self.buy_cash_amount - self.buy_commission
        if self.after_cash_amount < 0:
            self.account_add_cash = - self.after_cash_amount
            self.after_cash_amount = 0

        # 买后股数
        self.after_stock_num = self.before_stock_num + self.buy_stock_num


    def strategy(self):
        #4 策略
        """
        每天close时候buy， 次日高于close的价格的 r = 0.005 时候sale
        如果这一天都没有r = 0.005的情况，就继续hold

        这里r 可以学习前6月得到,用最后2个月来测试
        """
        principal = 100000




if __name__ == '__main__':
    SS = StrategicStock(cfg)
    SS.load_data()
    SS.strategy()