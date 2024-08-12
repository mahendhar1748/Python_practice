# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:00:11 2024

@author: BairaM
"""

#***********************************************************************************************
#                Working with jSON files                                   
#***********************************************************************************************

Data = {"people":[{"name":"Mahendhar","Age":24,"Dno":12},
                {"name":"Rahul","Age":25,"Dno":11},
                {"name":"Vineeth","Age":26,"Dno":10}]}
print(Data,type(Data),id(Data))

import json

# Json Dump ----> (Dumping raw data to Json file)

json_script_write = json.dumps(Data,indent=3)

with open ("my_data.json","w") as f:
    f.write(json_script_write)


# Json Load ----> (Loading Json file to the program)

# ---> importing json file with file handling

with open ("my_data.json","r") as f:
        json_object = json.loads(f.read())
        
print(json_object)
print(json_object['people'][0])

