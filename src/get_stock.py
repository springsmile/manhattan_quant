import baostock as bs
import pandas as pd
import config as cfg

class GetStock:

    def __init__(self, cfg):
        self.cfg = cfg
        self.stock_code = cfg.stock_code
        self.start_date = cfg.start_date
        self.end_date = cfg.end_date
        self.frequency = "d"
        self.csv_path = cfg.csv_path

    def login_bs(self):
        #### 登陆系统 ####
        lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:'+lg.error_code)
        print('login respond  error_msg:'+lg.error_msg)
        return bs

    def request_data(self, _bs, stock_code,
                     var_names = "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                     start_date = '2020-07-01',
                     end_date = '2020-07-30',
                     frequency = "d"):
        #### 获取沪深A股历史K线数据 ####
        # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。
        # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
        """
        rs = _bs.query_history_k_data_plus("sh.600000",
            "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
            start_date='2017-07-01', end_date='2017-12-31',
            frequency="d", adjustflag="3")
        """
        rs = _bs.query_history_k_data_plus(stock_code,
                                           var_names,
                                           start_date=start_date, end_date=end_date,
                                           frequency=frequency, adjustflag="3")
        print('query_history_k_data_plus respond error_code:'+rs.error_code)
        print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)



        return rs

    def format_data(self, rs):
        #### 打印结果集 ####
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        return data_list

    def save_data_file(self, data, columns):
        #### 结果集输出到csv文件 ####
        result = pd.DataFrame(data, columns=columns)
        result.to_csv("../data/history_A_stock_k_data.csv", index=False)
        print(result)

    def logout_bs(self, _bs):
        #### 登出系统 ####
        _bs.logout()

    def get_data(self):
        _bs = self.login_bs()
        _rs = self.request_data(_bs, stock_code= self.cfg.stock_code)
        data = self.format_data(_rs)
        print(data)
        # self.save_data_file(data, columns=_rs.fields)
        self.logout_bs(_bs)


if __name__ == '__main__':
    GS = GetStock(cfg)
    GS.get_data()
