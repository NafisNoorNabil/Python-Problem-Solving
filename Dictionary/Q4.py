#Medium Problem 1:
str_dict1 = input()
str_dict2 = input()
dict1 = dict( x.split(":") for x in str_dict1.split(","))
dict2 = dict( x.split(":") for x in str_dict2.split(","))
for key, value in dict1.items():
    dict1[key] = int(value)
for key, value in dict2.items():
    dict2[key] = int(value)
for key, value in dict2.items():
    if dict1.get(key) == None:
        dict1[key] = value
    else:
        dict1[key] += value
print(dict1)
list_of_values=[]
unique_values_list = []
for key in dict1.keys():
    list_of_values.append(dict1[key])
for i in list_of_values:
    if i not in unique_values_list:
        unique_values_list.append(i)
unique_values_tuple = tuple(unique_values_list)
print("Values: ", unique_values_tuple)