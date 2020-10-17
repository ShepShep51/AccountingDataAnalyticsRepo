import pandas as pd
import numpy as np

df = pd.read_csv(filepath_or_buffer="C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 9\\Lab_5-1_PCARD_FY2018_SQL.csv")
pd.set_option('display.max_columns', None)
sum = df['Amount'].sum()
count = df['Amount'].count()

df = df.rename(columns={"TransactionDate": "Purchase_Order_Date", "BusinessUnit": "Business_Unit_Code", "MerchantName": "Supplier_Account_ID", "PostedDate": "Entered_Date",
                   "Amoutn": "Purchase_Order_Local_Currency"})
df["Purchase_Order_ID"] = ""
df["Purchase_Order_Local_Currency"] = "USD"
df["Entered_By"] = ""
df["Purchase_Order_Fiscal_Year"] = "2018"
for index, row in df.iterrows():
    df.at[index , "Entered_By"] = row["CardholderFirstInitial"] + " " + row["CardholderLastName"]

df.to_csv(path_or_buf="C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 9\\Lab_5-1_PCARD_FY2018_ADS.csv")

