import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

df = pd.read_excel(io='C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 11\\Lab 6_4.xlsx')
dfR = pd.DataFrame(columns=["Tran_Date", "Tran_Type", "Amount"])
dfP = pd.DataFrame(columns=["Tran_Date", "Tran_Type", "Amount"])


for index, row in df.iterrows():
    if df.at[index, "Tran_Type"] == 'R':
        dfR = dfR.append(row, ignore_index=True)
    else:
        dfP = dfP.append(row, ignore_index=True)

#dfR = dfR.set_index(['Tran_Date'])
#dfP = dfP.set_index(['Tran_Date'])

dfP['Return'] = ''
dfP['Return_Amt'] = ''

for index, row in dfR.iterrows():
    ttype = dfR.at[index, 'Tran_Type']
    amt = dfR.at[index, 'Amount']
    dfP.at[index, 'Return'] = ttype
    dfP.at[index, 'Return_Amt'] = amt

dfP= dfP.astype({'Return_Amt': 'float'})

jan_df = pd.DataFrame(columns=dfP.columns)

other_df = pd.DataFrame(columns=dfP.columns)
for index, row in dfP.iterrows():
    if dfP.at[index, 'Tran_Date'].month ==1:
        jan_df = jan_df.append(row, ignore_index=True)
    else:
        other_df = other_df.append(row, ignore_index=True)

jan_df['R/P'] = ''
other_df['R/P']=''

for index, row in jan_df.iterrows():
    jan_df.at[index, 'R/P'] = jan_df.at[index, 'Return_Amt']/jan_df.at[index, "Amount"]
for index, row in other_df.iterrows():
    other_df.at[index, 'R/P'] = other_df.at[index, 'Return_Amt']/other_df.at[index, "Amount"]

#print("January \n",jan_df.head(), "\nOther Months\n", other_df.tail())


print(ttest_ind(jan_df['R/P'],other_df['R/P'],equal_var=False))