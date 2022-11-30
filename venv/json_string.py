# Python program to read
# json file


import json

# JSON string
a = '{"name": "Bob", "languages": "English"}'
# deserializes into dict
# and returns dict.
y = json.loads(a)
print("JSON string = ", y)
# # JSON file
f = open('data.json', 'r')
f.close()
#Reading from file
data = json.loads(a)
data1 = json.dumps(a)
print(data)
print(data1)
print(type(data))
print(type(data1))
print("O nome é " + data["name"] + "o idioma é " + data["languages"])
for i in data.values():
    print(i)
for x, y in data.items():
    print(x,y)



