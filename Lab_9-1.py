import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_excel(io='C:\\Users\\Shepard\\Desktop\\Life\\School\\Fall_2020\\ACC575\\Week 14\\Ch_9_State_SalesTax.xlsx')
df = df.dropna()
freq_dist = [0, .019, .038, .054, .073]
num_bins = 5
print(df["taxrate"])
histogram = plt.hist(df["taxrate"], num_bins)
zero = df[df['taxrate'] == 0]
print(zero)