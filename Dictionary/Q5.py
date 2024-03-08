#Medium Problem 2:
dict={}
while True:
    num = input()
    if dict.get(num)==None:
        dict[num] = 1
    else:
        dict[num] += 1
    if num=="STOP":
        break
dict.pop("STOP")
for x,y in dict.items():
    print(x,"-",y,"times")