import pandas as pd
import numpy as np
from pprint import pprint as print
import datetime as dt
import openpyxl as op
import os

pd.set_option('display.max_Columns', None)
dfE = pd.read_excel(io='C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 5\\Lab_3_1_Fuzzy.xlsx',sheet_name=0)
dfV = pd.read_excel(io='C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 5\\Lab_3_1_Fuzzy.xlsx',sheet_name=1)

dfV = dfV.loc[dfV['VendorSince'] >= pd.Timestamp(year=2019,month=1,day=1)]

with pd.ExcelWriter('C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 5\\Fuzzy-Tables-2019.xlsx') as writer:
    dfV.to_excel(writer,sheet_name='Vendors2019')
    dfE.to_excel(writer,sheet_name='Employees')
