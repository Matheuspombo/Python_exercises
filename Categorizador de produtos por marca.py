import pandas as pd
import numpy as np
df1= pd.DataFrame(pd.read_csv("Marcas.csv", sep = ";", encoding="utf-8"))
df2 = pd.DataFrame(pd.read_csv("Dados.csv", sep = ";", encoding="utf-8"))

#df1= df1.set_index("Index")

pd.set_option('display.max_columns', None)
x = df2.head()
y = df1.head()

df2['Marca']=df2['Marca'].astype(object)
df1['Marca']=df1['Marca'].astype(object)
#print (x)
#print (y)

df3 = df2.merge(df1, on="Produto", how="left")


z = df3.head()
df3.to_excel('merged.xlsx')

print(z)








