import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#чтение данных с excel файлов:
readExcelApple=pd.read_excel("C:\pycharm\project\Apple.xlsx", sheet_name="Apple")
data_apple=[]
for i in readExcelApple["Open"]:
    data_apple.append(i)

readExcelMicrosoft=pd.read_excel("C:\pycharm\project\Microsoft.xlsx",sheet_name="Microsoft")
data_microsoft=[]
for i in readExcelMicrosoft["Open"]:
    data_microsoft.append(i)

readExcelGoogle=pd.read_excel("C:\pycharm\project\Google.xlsx",sheet_name="Google")
data_google=[]
for i in readExcelGoogle["Open"]:
    data_google.append(i)

x=np.arange(1,len(data_apple)+1) # с 1 по кол-во недель за 12 месяцев


print("изменения")
plt.figure(figsize=(15, 10))
plt.grid(alpha=0.3)
plt.xticks(np.arange(1, len(data_apple)+1, 1),color='g')#кол-во тиков на оси х
plt.yticks(np.arange(0, 500, 12),color='g')# кол-во тиков на оси y
plt.xlabel("Month",color='blue')
plt.ylabel("Open price",color='blue')


plt.plot(x,data_microsoft,color='#ffb41f',label='Microsoft')
plt.fill_between(x, data_microsoft, facecolor='yellow', alpha=0.4)

plt.plot(x,data_apple,c='blue',label='Apple')
plt.fill_between(x, data_apple, facecolor='blue', alpha=0.4) #facecolor-цвет заливки, alpha-степень прозрачности


plt.plot(x,data_google,c='purple',label='Google')
plt.fill_between(x, data_google, facecolor='purple', alpha=0.4)

plt.legend(loc=2)#построение легенды во второй четверти
plt.show()