from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('seaborn')

#plt.rcParams["figure.figsize"] = [15.00, 7.50]
#plt.rcParams["figure.autolayout"]=True
#columns = ["Frequency", "dB"]
df = pd.read_csv("trace01.csv", sep=';')
df2= pd.read_csv("trace02.csv", sep=';')
df3= pd.read_csv("trace03.csv", sep=';')
df4= pd.read_csv("trace04.csv", sep=';')
freq=df['Frequency']
dB=df['dB']
freq2=df2['Frequency']
dB2=df2['dB']
freq3=df3['Frequency']
dB3=df3['dB']
freq4=df4['Frequency']
dB4=df4['dB']
#print("Contents in csv file:\n", df)
plt.plot(freq, dB, linewidth=1, color='red')
plt.plot(freq2, dB2, linewidth=1, color='blue')
plt.plot(freq3, dB3, linewidth=1, color='green')
plt.plot(freq4, dB4, linewidth=1, color='yellow')
plt
plt.title('NBIAs Resonant Frequencies')
plt.xlabel('Frequency')
plt.ylabel('dB')
plt.show()
    