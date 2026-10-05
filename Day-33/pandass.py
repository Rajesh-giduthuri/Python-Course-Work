#Pandas : a powerful, open-source Python library explicitly designed for data manipulation, cleaning, and analysis

#pandas --> series : single column
import pandas as pd
data=pd.Series([23,45,68])
print(data)

data=pd.Series([23,45,68],index=['a','b','c'])
print(data)

#pandas --> dataFrame : multiple rows & columns
dt={"name":["ka","sa"],
    "age":[10,12],
    "marks":[80,75]}
df=pd.DataFrame(dt)
print(df)

df1=pd.read_csv(r"C:\Users\rajes\Downloads\students.csv")
print(df1)
print(df1.isnull())   #check null values
print(df1.isnull().sum())
df1=df1.fillna(0)  #replaces the null values
print(df1.isnull().sum())   #sum of null records
df1=df1.dropna()   #drop null records
print(df1)
df1=df1.drop(2,axis=0)  #drop the record
df1=df1.drop("Course",axis=1)  #drop the column
print(df1)
print(df1[["Name","Course"]])   #specifed columns
print(df1.iloc[0])  #individual record by index
da=pd.Series([23,45,68],index=['a','b','c'])
print(da.loc['c'])  #individual record by label specified
print(df1.loc[3])   #individual record by 
print(df1.duplicated("Course"))