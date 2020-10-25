import pandas as pd
import numpy as np
#from pprint import pprint as print
pd.set_option("Max_Columns", None)
df = pd.read_excel(io = 'C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\'
                        'ACC575\\Week 10\\Lab_6_2_SlainteAging_Sept.xlsx')
df1 = pd.read_excel(io= 'C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\'
                        'ACC575\\Week 10\\Lab_6_2_SlainteAging_Sept.xlsx', sheet_name="Cash_Received")
df1 = df1.set_index('Sales_Order_ID (FK)')
df["Receipt_Amount"] = ''

for index, row in df.iterrows():
    soid = df.at[index, "Sales_Order_ID"]
    try:
        rep_amt = df1.loc[soid, "Receipt_Amount"].sum()
        df.at[index, "Receipt_Amount"] = rep_amt
    except:
        df.at[index, "Receipt_Amount"] = 0

dfOut = df[["Sales_Order_ID", "Sales_Order_Total", "Receipt_Amount", "Sales_Order_Date"]]
dfOut = dfOut.set_index("Sales_Order_ID")

with pd.ExcelWriter('C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\'
                        'ACC575\\Week 10\\6_2_Output.xlsx') as writer:
    dfOut.to_excel(writer, sheet_name='Output')

dfOut['Difference'] = ''

for index, row in dfOut.iterrows():
    dfOut.at[index, "Difference"] = row["Sales_Order_Total"] - row["Receipt_Amount"]
dfOut = dfOut.loc[df["Difference"] > 0]



