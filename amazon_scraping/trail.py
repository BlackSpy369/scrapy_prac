import webbrowser
import pandas as pd
import time

df=pd.read_csv("baby_clothes.csv")

for i in range(len(df)):
    if int(df["price"][i])>=300 and int(df["price"][i])<=500:
        webbrowser.open_new_tab(df["product_link"][i])
        time.sleep(0.2)