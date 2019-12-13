# Write a Python function to create the HTML string with tags around the word(s)

def add_tags(tag,txt):
    return "<"+tag+">"+txt+"</"+tag+">"

print(add_tags("body","Alejandro"))
print(add_tags("h1","Omar"))
print(add_tags("h2","Rizzuto"))

"""
<body>Alejandro</body>
<h1>Omar</h1>
<h2>Rizzuto</h2>
"""
