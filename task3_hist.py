from idlelib.iomenu import encoding

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('divans.csv', encoding='utf-16')
data = data['Цена']
data.plot.hist(bins=10)
plt.title("Распределение цен диванов и кресел")
plt.xlabel("Цена")
plt.ylabel("Количество")
plt.show()