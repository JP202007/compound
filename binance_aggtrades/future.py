import pandas as pd
from datetime import datetime


data = pd.read_csv('/Users/panpanfeng/PycharmProjects/defi/binancefuture/BTCUSDT-aggTrades-2021-05.csv')

csv_df = pd.DataFrame(data)
csv_df.columns=['id','price','qty','fid','lid','date','ifmker']

csv_df=csv_df.drop(columns=['id','fid','lid','ifmker'])

csv_df['date'] = [datetime.utcfromtimestamp(float(timestamp/1000)) for timestamp in csv_df['date']]
csv_df['date'] = [timestamp.strftime('%Y-%m-%d') for timestamp in csv_df['date']]

csv_df["agg"] = csv_df["price"].mul(csv_df["qty"])

csv_df=csv_df.groupby('date').sum()
csv_df.to_csv('bnft2021_05.csv')

data1 = pd.read_csv('bnft2021_05.csv')
print(data1)