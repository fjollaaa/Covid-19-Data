import requests_html
import pandas as pd
import  numpy as np
from pandas import DataFrame
df1=pd.read_csv("Data.csv")
df2=pd.read_csv("DataForHeartDisease.csv")
df3=pd.read_csv("DataForLungDisease.csv")
df4=pd.read_csv("DataForDiabetes.csv")
df5=pd.read_csv("DataForWorldPopulation.csv")
df6=pd.read_csv("CovidCases.csv")
df7=pd.read_csv("CovidDeaths.csv")
# print(df3)
# print(df2)
# print(df4)
dataframes=[df2,df3,df4,df5,df6,df7]
new=[]
for x in dataframes:
    x=x.set_index('Country')
    new.append(pd.Series(x.values.tolist(),index=x.index))
dataframe=pd.concat(new,axis=1,keys=('Heart Disease','Lung Disease','Diabetes','Population','COVID-19 Cases','COVID-19 Deaths'),sort=True)
dataframe.to_csv("Final_Data.csv")
print(dataframe)



