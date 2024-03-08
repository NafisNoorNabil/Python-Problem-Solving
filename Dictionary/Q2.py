
#Easy Problem 2:
str_dict=input()
dict=dict(x.split(":") for x in str_dict.split(","))
for key,value in dict.items():
    dict[key]=int(value)
maxDictKey = max(dict, key=dict.get)
minDictKey = min(dict, key=dict.get)
print("Maximum: ", maxDictKey)
print("Minimum: ", minDictKey)
