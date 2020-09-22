import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import config as cfg

class AnaStock:
    def __init__(self, cfg):
        self.cfg = cfg

    def load_data(self, fpath):
        df = pd.read_csv(fpath)
        return df

    def draw(self, df):
        plt.plot(df.index, df['open'])

        plt.style.use('seaborn-whitegrid')
        plt.xticks(rotation=30)
        plt.plot(df.index, df['open'], label='open', marker='o', linestyle=':', linewidth=1, markersize=3, color='gray')
        plt.plot(df.index, df['high'], label='high', marker='o', linestyle=':', linewidth=1, markersize=3,
                 color='green')
        plt.plot(df.index, df['low'], label='low', marker='o', linestyle=':', linewidth=1, markersize=3, color='blue')
        plt.plot(df.index, df['close'], label='close', marker='o', linestyle='-', linewidth=2, markersize=6,
                 color='red')

        for x, y in zip(df.index, df['close']):
            plt.text(x, y + 0.3, '%.2f' % y, ha='center', va='bottom', color='red')

        plt.legend()
        plt.title("s' stock trend")
        plt.show(block=True)

        plt.show()

    def ana(self):
        data = self.load_data(fpath=self.cfg.csv_path)
        print(data)
        self.draw(data)

if __name__ == '__main__':
    AS = AnaStock(cfg=cfg)
    AS.ana()