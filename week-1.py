
import yfinance as df
df.download("QAN.AX", '2020-01-01', None).to_csv('qan_stk_prc.csv')
print(df)
#variables not start at number
#print(type[]) #check the type
#division ==>float 4/2=2.0

