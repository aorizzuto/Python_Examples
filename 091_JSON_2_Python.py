# Write a Python program to convert JSON data to Python object

import json

json_obj =  '{ "Name":"Alejandro", "Class":"Ing", "Age":33, "Knowledge":{"Soft":"Python, C, C++", "Hard":"Electronics"} }'

python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"]) 
print("Knowledge: ",python_obj["Knowledge"])
print("Software: ",python_obj["Knowledge"]["Soft"])
print("Hardware: ",python_obj["Knowledge"]["Hard"])

"""
JSON data:
{'Name': 'Alejandro', 'Class': 'Ing', 'Age': 33, 'Knowledge': {'Soft': 'Python, C, C++', 'Hard': 'Electronics'}}

Name:  Alejandro
Class:  Ing
Age:  33
Knowledge:  {'Soft': 'Python, C, C++', 'Hard': 'Electronics'}
Software:  Python, C, C++
Hardware:  Electronics
"""
