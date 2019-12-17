# Write a Python program to convert Python object to JSON data

import json

python_obj = {
    "name": "Alejandro",
    "class":"Ing",
    "age": 33,
    "Knowledge": {"Soft":"Python, C, C++", "Hard":"Electronics"}
}

# convert into JSON:
j_data = json.dumps(python_obj)

print("\nPython data:")
print(python_obj)

print("\nJSON data:")
print(j_data)

"""
Python data:
{'name': 'Alejandro', 'class': 'Ing', 'age': 33, 'Knowledge': {'Soft': 'Python, C, C++', 'Hard': 'Electronics'}}

JSON data:
{"name": "Alejandro", "class": "Ing", "age": 33, "Knowledge": {"Soft": "Python, C, C++", "Hard": "Electronics"}}
"""
