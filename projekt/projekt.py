
# Projektna naloga GEN-I
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read excel file
headers = ['Price', 'Profit']
df = pd.read_csv(r'C:\Users\aanja\OneDrive\Dokumenti\fmf\magisterski študij\matematika z računalnikom\Nelinearne-transakcije\projekt\podatki.csv', sep=';', names=headers)
print(df)

# Plot
# plt.scatter(df['Price'], df['Profit']) 
# plt.show()

df.plot(kind='scatter', figsize=(10,10), x='Price',y='Profit' )
plt.axis("off")
plt.show()

#or 
# df.plot(kind='scatter', x='Price', y='Profit', color='blue')
# plt.show()

