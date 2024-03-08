# Easy Problem 1:
str = input()
dict = dict(x.split(":") for x in str.split(","))
lst_to_check=[]
while True:
    n=input()
    if n=="STOP":
        break
    lst_to_check.append(n)
values_of_dict=[]
for i in dict:
    values_of_dict.append(dict[i])
for j in range(len(lst_to_check)):
    if lst_to_check[j] in values_of_dict:
        print("True")
    else:
        print("False")
        
        
dict = {value.strip().split(': ')[0]:int(value.strip().split(': ')[1]) for value in input('Dictionnary: ').split(', ')}
i=0
while i<1:
    found=0
    num=input()
    if num=="STOP":
        break
    for j in dict:
        if dict[j]==int(num):
            found+=1
    if found==0:
        print("False")
    else :
        print("true")