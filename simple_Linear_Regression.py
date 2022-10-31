import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv('Salary_Data.csv')
X = data['YearsExperience']
print(X)
Y = data['Salary']
print(data.head())
ax = plt.plot(X,Y,'o')

plt.show


m = 0
c = 0
l = 0.00001
epochs = 10000
n = float(len(X))
for i in range(epochs):
    Y_pred = m *X + c
    delta_m = -2/n  * sum (X*(Y-Y_pred))
    delta_c = -2/n *sum(Y-Y_pred)
    m = m - l *delta_m
    c = c - l *delta_c

print(m,c)
Y_predicted = m *X + c
ax = plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')
plt.savefig('a.png')
plt.show()
