# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
data = {"telugu":[12,23,24,24,21,24,25],
        "Hindi":[21,23,23,23,21,23,12],
        "English":[22,23,24,14,21,24,19],
        "Maths":[8,23,14,24,11,24,25],
        "Science":[12,13,24,24,21,14,25],
        "Social":[12,13,24,14,21,14,25]}
#print(data,type(data),id(data))
df = pd.DataFrame(data,index=['std1','std2','std3','std4','std5','std6','std7'])
print(df)
print(df.shape)
df.hist()
df['telugu'].hist()
df['telugu'].plot(kind='bar',title="Bar plot for Telugu Subject")
print(df.loc[['std3','std4']])
print(df.iloc[0:4,0:4])
print(df.loc['std2'].mean())
print(df.value_counts())
print(df)
#printing a column entire records
print(df['telugu'].value_counts().sum())
#prints entire information of data frame-->Any-nulls,data types
df.info()
#printing null values of all columns (True or False) 
print(df.isnull().any())
#printing sum of null values of all columns (True or False) 
print(df.isnull().sum())
#printing individual total types in perticular column
print(df['telugu'].value_counts())
#printing a perticular column entire sum
print(df['telugu'].sum())
#printing entire dataframe sum--> gives each column sum
print(df.sum())
#describing entire data frame
print(df.describe())
#------------------------------------------------------------------------
#         SORTING &  FILTERING OEPRATIONS                          ------
#------------------------------------------------------------------------

#FILTERING THE RECORDS PERTICULAR STUDENT
#  ----> Here for string indexes we use .loc
print(df.loc['std1'])
print(df.loc[['std2','std3']])

#FILTERING BASED ON VALUES
#   ---> Filtering based on marks 
print(df['telugu'] > 20)  # it just gives true or false on condition
print(df[df['telugu'] > 20]) # it will print the entire dataset.Having Students who achieved 
# more than 20 marks in Telugu

#-----------------------------------------------------------------
#                      Assigning a Rank column                  --
#-----------------------------------------------------------------

#df['Total'] = df.sum(axis=1)
print(df)
df['Rank'] = df['Total'].rank(ascending=False).astype(int)
print(df)
# making the students ordering in Rank wise
print(df.sort_values(by='Rank',ascending=True))

#--------------------------------------------------------------------------
#               Grouping and Agrregations                              ----
#--------------------------------------------------------------------------
# we will take another dataset 

data2 = {"Name":["Arun","Varuni","Tarun","Ravali","Pavani"],
        "Age":[21,23,25,23,21],
        "Gender":['M','F','M','F','F'],
        "Salary":[22000,28000,35000,25000,23000],
        "Dno":[12,13,11,12,10],
        "City":["Hyd","Bglr","Pune","Hyd","Pune"]}
#print(data,type(data),id(data))
df2 = pd.DataFrame(data2,index=[1,2,3,4,5])
print(df2)

# Single grouping single Agrregation
print(df2.groupby('Gender')['Salary'].sum())
#Multi Grouping Single Agrregation
print(df2.groupby(['Dno','Gender'])['Salary'].sum())
#Single Grouping and Multi Agrregation
print(df2.groupby('Gender').agg({'Salary':['sum','mean','max']}))
#Multi Grouping and Multi Aggregation
print(df2.groupby(['Dno','Gender']).agg({'Salary':['sum','mean','max']}))
df2['Salary'].plot(kind='bar')
df2.plot(kind='bar',stacked=True)

#------------------------------------------------
#   Indexing (single & Multi)                 ---
#------------------------------------------------

print(df2)
df3=df2.copy()
print(df3)

# Resetting index if any
df3.reset_index(inplace=True)
print(df3)
#df3.set_index('index',inplace=True)
#print(df3)
# Setting Multiple indexes
df3.set_index(['index','Dno'],inplace=True)
print(df3)
#-- Here Inde and Dno becomes multiple indexes

df3=df3.sort_index(ascending=False)
df3=df3.sort_index(ascending=[False,True])
print(df3)

#Retreving values of Multiple indexing

print(df3.loc[5,10])
#here 5 ---> First Index and 10 ---> Second Index
print(df3.iloc[2,13])

#Note * here for multi indexing if we want to retreive the records use 'loc'
# iloc for multi indexing is wont work

#-----------------------------------------------------------------------------
#--------    Merging , Joining and Concatinating           ------------------
#----------------------------------------------------------------------------

# Merging and Joining Do the same operations but merging is some what more easy
# compared to Join. In merging work with column names(id,name...)
# But in Joins we have to provide index. By that Joins perform

df3=df3.sort_index(ascending=[True,True])
print(df3)

data3 = {"Name":["Arun","Varuni","Baskar","Ravali","Pavan"],
        "Age":[21,23,29,23,30],
        "Gender":['M','F','M','F','M'],
        "Salary":[22000,45000,32000,25000,50000],
        "Dno":[12,11,11,12,10],
        "City":["Hyd","Bglr","Pune","Hyd","Pune"]}
print(data3,type(data3),id(data3))
df4=pd.DataFrame(data3,index=[1,2,3,4,5])
df4.set_index('index',inplace=True)
print(df4)
print(df3)

#--------------------------
#      Merge           ----
#--------------------------


#---------- Inner merge --------------------------------
# if we dont provide the merging on, it will defaultly do inner merge and based on similar cols
inner_merge=df3.merge(df4)
print(inner_merge)

# -- Type 2 of inner merge 
inner_merge2=df3.merge(df4,how='inner',on='Gender')
print(inner_merge2)

inner_merge3=df3.merge(df4,how='inner',on=['Dno','Gender'])
print(inner_merge3)

# ----------------------- outer merge ------------------------------------
outer_merge=df3.merge(df4,how='outer')
print(outer_merge)

outer_merge2=df3.merge(df4,how='outer',on='Name')
print(outer_merge2)

# ------------------------- Left Outer Merge --------------------------------
Left_merge=df3.merge(df4,how='left',on='Name')
print(Left_merge)

# ------------------------- Right Outer Merge --------------------------------
Right_merge=df3.merge(df4,how='right',on='Name')
print(Right_merge)

# -------------------------- Cross merge -------------------------------

Cross_join = df3.merge(df4,how='cross')
print(Cross_join)

#-------------------
#  Joins       -----
#-------------------

# Joins are better useful when we are working with Indexes

Join_sample = df3.join(df4,how='inner',on='index',lsuffix='_Left',rsuffix='_Right')
print(Join_sample)

#Joining by Setting Index Dno
Join_sample2 = df3.set_index('Dno').join(df4.set_index('Dno'),how='inner',lsuffix='_Left',rsuffix='_Right')
print(Join_sample2)

# Joining by Dno (Outer Join)
Join_sample3 = df3.set_index('Dno').join(df4.set_index('Dno'),how='outer',lsuffix='_Left',rsuffix='_Right')
print(Join_sample3)

# Joining By Dno (Left Join)
Join_sample4 = df3.set_index('Dno').join(df4.set_index('Dno'),how='left',lsuffix='_Left',rsuffix='_Right')
print(Join_sample4)

# Joining By Dno (Right Join)
Join_sample5 = df3.set_index('Dno').join(df4.set_index('Dno'),how='right',lsuffix='_Left',rsuffix='_Right')
print(Join_sample5)

#------------------------
#   Concatinating     ---
#------------------------

# Concatinating is nothing but putting up one Data Frame over another

print(df3)
print("\n")
print(df4)
conc = pd.concat([df3,df4])
print(conc)

# Concatinating on inner --> it will concatinate only similar cols intwo Dataframes

inner_conc = pd.concat([df3,df4],join='inner')
print(inner_conc)

# Concatinating with just like Side by Side(Merge and Joins)

inner_conc1 = pd.concat([df3,df4],join='inner',axis=1)
print(inner_conc1)

# Appending ---> It is the old method in python

appd = df3.append(df4)
print(appd)















