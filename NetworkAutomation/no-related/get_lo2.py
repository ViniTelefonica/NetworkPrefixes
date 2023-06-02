import pandas as pd

path = 'C:/Users/40416438/OneDrive - Telefonica/Desktop/REDES/Loopbacks.xlsx'

df = pd.read_excel(path)

len_df = len(df.index)

lo2_list = []
lo2_prep = []
f = open('loopbacks.txt', 'w')

for i in range (len_df):
    lo2_prep.append(df.iloc[i]['Lo2'])

for val in lo2_prep:
    value = val.split("/")
    lo2_list.append(value[0])
    f.write(value[0]+"\n")

