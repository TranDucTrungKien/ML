import pandas as pd
from ex0410 import MyStatistic
df=pd.read_csv("dataset\SalesTransactions.csv")

print(df)
df_filtered=MyStatistic.find_orders_with_totals(df,200,500,False)
print(df_filtered)