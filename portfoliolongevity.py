# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 17:43:00 2023

@author: rahul
"""

import pandas as pd
import os
import random
os.chdir("C://Users/rahul/Downloads")
#Historic One-Year Rollling Returns Probabilities
df = pd.read_excel("Longevity.xlsx")
Longevity = []
#Historical Inflation Rates
hist_inflations=[0.07,0.05,0.07,0.04,0.04,0.03,0.05,0.05,0.07,0.10,0.09,0.09,0.12,0.11,0.08,0.06,0.06,0.04,0.04,0.04,0.04,0.04,0.04]
for x in range(10000):
    yr = 100
    #Assumed Portfolio Size
    Portfolio_Amnt = 100
    #Assumed Safe Withdrawal Rate
    Withdrawal_Amnt = 8
    for i in range(yr):
        seed = random.randint(1,5653)
        # print("Seed="+str(seed))
        for index, row in df.iterrows():
            if int(row['Min']) <= seed <= int(row['Max']):
                #Return Generator
                p_return = row["Return%"]
                #Inflation Generator
                inflation = random.choice(hist_inflations)
                break
        Portfolio_Amnt = (Portfolio_Amnt - Withdrawal_Amnt)*(1+p_return)
        Withdrawal_Amnt = Withdrawal_Amnt*(1+inflation)
        if Portfolio_Amnt <= 0:
            print("Year "+str(i+1))
            Longevity.append([Portfolio_Amnt,(i+1)])
            break
        if i == 99:
            print("Year "+str(i+2))
            Longevity.append([Portfolio_Amnt,(i+2)])
            break
df_long = pd.DataFrame(Longevity, columns = ['Portfolio Amnt', 'Year Lasted'])
df_long.to_excel("long8.xlsx", index=False)