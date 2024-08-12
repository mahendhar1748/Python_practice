# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:10:45 2024

@author: BairaM
"""
#*****************************************************************************
#------------------------- Regular_Expressions --------------------------------
#****************************************************************************  

# Regular Expressions(Regex) are mainly useful for retrieving particular text
# among thousands of statements

'''
* --> It matches Zero(or) more occureneces of preceeding character
+ --> It matches with one (or) more occureneces
? --> It matches with zero (or) one occurences
. --> It matches with single character
[] --> It matches with single character inthe given list
[-] --> It matches with single character in the given range
[^] --> It matches with starting char of the given words
[a-z] --> It matches with any single char of lower case alphabets
[A-Z] --> It matches with any single char of upper case alphabets 
[0-9] --> It matches with any single Numeric Digit
[a-zA-Z0-9] --> It matches with any alphanumeric
\w --> It matches with any alphanumeric
\W --> It matches with any non-alpha numeric
\s --> It matches with white Spaces
\S --> It matches with non-white Spaces
{m} --> It matches m times exact occureneces of preceeding Char
^ --> Start of the line
$ --> End of the line
\d --> any single digit
\D --> any single Non-digit
'''
# Regex Functions

'''
findall --> Returns a list containing all matches
split ----> Returns a list where string has been split at each match
finditer -> Returns a iterator object
sub ------> Replaces one or more matches with a string

'''
# Eg :- "jan 15,march 13,april 10" --> [\w]+' '[\d]+

#-------------------------------------------------------------------------------------
str1="python supports dynamic data types"
str2 = "kohli scored 103 runs in 95 balls"
str3 = "104.45,102,30,5,57.35"

import re

#find lower case letters b/w a-m

x=re.findall('[a-m]',str1)
print(x,type(x))

#find dynamic in the string

x=re.findall('d.+c',str1)
print(x)

# find digital characters from str2
y=re.findall('[\d]+',str2)
print(y)

# Extract all decimal values from str3

z=re.findall('\d+[.]\d+',str3)
print(z)

#----------------------------------------------------------------------------

str4="hello world"

# check whether the string starting with hello

a=re.findall('^hello',str4)
print(a)
if a:
    print('yes the string is starting with hello')
else:
    print("no match")
    
# Check whether the string ending with world
b=re.findall('world$',str4)
print(b)
if b:
    print('yes the string is ending with world')
else:
    print("no match")           

#-------------------------------------------------------------------------

str = "The trains in spain falls mainly in plains"

# finding ai followed characters

c=re.findall('ai*',str)
print(c)

# Extracting the words containing ai characters

d=re.findall('[\w]+ai[\w]+',str)
print(d)

#************************************************************************************
#---------------------  Real Time Scenario                                -----------
#************************************************************************************
import re

random_text = '''
My name is Mr. Neo. My phone number is 123-456-7890. My email is ChosenOne@gmail.com
My name is Mr. Morphius. My phone number is 413-234-2568. My email is CoolGuy@yahoo.com. 
My name is Mrs. Trinity. My phone number is 285-036-8215. My email is ChosenOnesGirl1@apple.com.
'''

print(random_text)

# Extracting Phone numbers
e=re.findall('\d{3}-\d{3}-\d{4}',random_text)
#e=re.findall('\d+-\d+-\d+',random_text)
print(e)

#Extracting only ending-mails(eg:- @gmail.com)

f=re.findall('@.+',random_text)
print(f)

#Extracting ending mails with out @  (eg:- gmail.com,yahoo.com)
g=re.findall('@([a-z]+)',random_text)
print(g)

# Extracting Entire mails
h=re.findall('[a-zA-Z]+@[a-z]+',random_text)  #It is extracting only unique mails
print(h)

# Extracting Entire mails

i=re.findall('[\w]+@[\w]+',random_text) # Now it is extracting entire mails
print(i)

#----------------------------











 