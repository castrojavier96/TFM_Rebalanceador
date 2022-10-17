import pandas as pd
import glob
import os
import matplotlib.pyplot as plt

path = r'C:\Users\javie\Downloads\Archives\ETFs' # use your path
all_files = glob.glob(os.path.join(path, "*.txt"))

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col='Date', header=0)
    df_close = df.loc['2010-01-01':'2015-01-01',['Close']]
    li.append(df_close)

frame = pd.concat(li, axis=1, ignore_index=True)
datos = frame.iloc[:884].dropna(axis=1)

plt.plot(datos)