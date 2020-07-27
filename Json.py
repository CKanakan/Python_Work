#python json(all lowercase)
import json
 #used to store and exchange data
"""
x = '{"name":"John", "age":30, "city":"New York"}'

#parse x:
y = json.loads(x)

# this result is a Python dictionary
print(y["age"])
"""

# a Python object(dict):
x = {
"name": "John",
"age":30,
"city":"New York"
}

#Converts to JSON
y = json.dumps(x)

# the result is a JSON string:
print(y)

#dict, list, tuple, string, int, float, True, False, None


"""x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
# or you can do
print(json.dumps(x, indent=4))
# and you can add seperators
print(json.dumps(x, indent=4, separators=(". ", " = ")))
"""
