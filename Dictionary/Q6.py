#Medium Problem 3:
str_dict = input()
dict = dict((x.split(":") for x in str_dict.split(",")))
res_dict={}
for a,b in dict.items():
    if b in res_dict:
        res_dict[b].append(a)
    else:
        res_dict[b] = [a]
print(res_dict)