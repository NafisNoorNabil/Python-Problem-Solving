# Easy Problem 3 

dict = {}
i=0
while i<10:
    value=input()
    key=i
    if value not in dict.values():
        dict[i] = value
    else:
        print("enter a different number.")
        i=i-1
    i+=1
print(dict)