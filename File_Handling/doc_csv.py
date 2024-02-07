'''
f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/Test_Plan.docx",mode="r")
print(f.read())
print("file readed successfully")
f.close()
'''
#python is unable to read docx files
#we need to import a separate module for reading docx files
#same we need to install separate module for xlxs files to read.

#creating .csv file and writing it into it

f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/Test_Plan.csv",mode="w")
data='''
1,miller,8000,12,hyd
2,blake,3000,23,pune
3,sony,4000,24,hyd
4,harsha,5000,67,chennai'''

f.write(data)
f.close()
print("data written and file closed successfully")
f1=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/Test_Plan.csv")
print(f1.read())
print("\n")
f1.close()
print("files closed successfully")

