import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

happy_df=pd.read_excel("E:/PROJECTS/DATA ANALYTICS PROJECT 2/DATA.xlsx")
print(happy_df.head(10))

print(happy_df.isnull().sum())
plt.rcParams['figure.facecolor']='#FFE5B4'


#Plotting the graph for top 10 Happiest countries in 2021

plt.rcParams['figure.figsize']=(10,7)
plt.title('Top 10 Countries by Ladder score(Happiness) in 2021',size=25)
sns.scatterplot(data=happy_df.sort_values(by='Ladder score',ascending=False).iloc[:10],x='Country',y='Ladder score',s=200)
print(plt.show())

#Plotting the graph for top 10 Sad countries in 2021
plt.rcParams['figure.figsize']=(10,7)
plt.title('Top 10 Countries by Least Ladder score(Sadness) in 2021',size=25)
sns.scatterplot(data=happy_df.sort_values(by='Ladder score',ascending=True).iloc[:10],x='Country',y='Ladder score',s=200)
print(plt.show())

#Total Ladder score Graph for each Region
Ladder_df=happy_df.groupby('Regional indicator')['Ladder score'].sum()
print(Ladder_df.head(10))
Ladder_df.plot.pie(autopct='%1.2f%%')
plt.title('Total Ladder score by Region',size=25)
plt.ylabel('')
plt.legend()
print(plt.show())

#Plotting the graph for top 10 countries with Highest GDP
plt.rcParams['figure.figsize']=(10,7)
plt.title('Top 10 Countries with Higest GDP in 2021',size=25)
sns.lineplot(data=happy_df.sort_values(by='Logged GDP per capita',ascending=False).iloc[:10],x='Country',y='Logged GDP per capita',linewidth=5)
print(plt.show())

#Plotting the graph for top 10 countries with Lowest GDP
plt.rcParams['figure.figsize']=(10,7)
plt.title('Top 10 Countries with Lowest GDP in 2021',size=25)
sns.lineplot(data=happy_df.sort_values(by='Logged GDP per capita',ascending=True).iloc[:10],x='Country',y='Logged GDP per capita',linewidth=5)
print(plt.show())

#Total GDP contribution in 2021 from each Region
GDP_df=happy_df.groupby('Regional indicator')['Logged GDP per capita'].mean()
print(GDP_df.head(10))
GDP_df.plot.area()
plt.title('Total GDP by Region',size=25)
plt.ylabel('')
plt.legend()
print(plt.show())

#Plotting the graph For top 10 countries having Highest life expectency in 2021
plt.rcParams['figure.figsize']=(10,7)
plt.title('Top 10 Countries with Higest Life Expectency in 2021',size=25)
sns.pointplot(data=happy_df.sort_values(by='Healthy life expectancy',ascending=False).iloc[:10],x='Country',y='Healthy life expectancy',linewidth=5)
print(plt.show())

#Plotting the graph For top 10 countries having Lowest life expectency in 2021
plt.rcParams['figure.figsize']=(10,7)
plt.title('Top 10 Countries with Lowest Life Expectency in 2021',size=25)
sns.pointplot(data=happy_df.sort_values(by='Healthy life expectancy',ascending=True).iloc[:10],x='Country',y='Healthy life expectancy',linewidth=5)
print(plt.show())

#Total Life Expectency by Regions in 2021
GDP_df=happy_df.groupby('Regional indicator')['Healthy life expectancy'].mean()
print(GDP_df.head(10))
GDP_df.plot.bar()
plt.title('Total Life Expectancy by Region',size=25)
plt.ylabel('Life Span in Years')
plt.legend()
print(plt.show())

#Final corelation Map for whole excel sheet
cor1=happy_df.corr(method='pearson')
f, ax=plt.subplots(figsize=(10,7))
sns.heatmap(cor1,mask=np.zeros_like(cor1,dtype=np.bool),square=True)
plt.title('Correlation for Whole Excel Sheet')
print(plt.show())
