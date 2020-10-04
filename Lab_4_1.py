import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

fgi_product = pd.read_excel(io="C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 2\\Lab_2-2_Slainte_Dataset.xlsx")
sales_subset = pd.read_excel(io="C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 2\\Lab_2-2_Slainte_Dataset.xlsx", sheet_name= 1)
customer = pd.read_excel(io="C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 2\\Lab_2-2_Slainte_Dataset.xlsx", sheet_name= 2)
fgi_product = fgi_product.set_index('Product_Code')
output = pd.DataFrame
pd.set_option('display.max_columns', None)


m = []
for i, row in sales_subset.iterrows():
    val = sales_subset.iloc[i, 1]
    year = val.year
    month = val.month
    m.append(month)
    sales_subset.at[i,'Sales_Order_Date'] = year

sales_subset.insert(2,"Month",m)
prod_name = []
for i, row in sales_subset.iterrows():
    lookup = sales_subset.iloc[i,5]
    val = fgi_product.loc[lookup, 'Product_Description']
    prod_name.append(val)

sales_subset.insert(5, "Product_Name", prod_name)

output = sales_subset[['Sales_Order_Date','Month', 'Product_Name', 'Sales_Order_Quantity_Sold']]
output = output.loc[output['Sales_Order_Date'] >= 2020]
output = output.set_index(['Sales_Order_Date', 'Month', 'Product_Name'])
output = output.groupby(level=[1,2]).sum()
output.plot(kind='barh')
plt.show()


