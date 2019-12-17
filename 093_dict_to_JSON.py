# Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4

import json

dicc = {'name': 'Alejandro', 'class': 'Ing', 'age': 33, 'Knowledge': {'Soft': 'Python, C, C++', 'Hard': 'Electronics'}}

print("Original String:")
print(dicc)

print("\nJSON data:")
print(json.dumps(dicc, sort_keys=True, indent=4))
Original String:
{'name': 'Alejandro', 'class': 'Ing', 'age': 33, 'Knowledge': {'Soft': 'Python, C, C++', 'Hard': 'Electronics'}}

JSON data:
{
    "Knowledge": {
        "Hard": "Electronics",
        "Soft": "Python, C, C++"
    },
    "age": 33,
    "class": "Ing",
    "name": "Alejandro"
}
