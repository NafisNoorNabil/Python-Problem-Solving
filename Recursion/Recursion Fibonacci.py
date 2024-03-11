

store={}

def fibonacci(num):
    if num in store:
        return store[num]
    if num == 0:
        return 1

    elif num == 1:
        return 1
    
    else:
        x=(fibonacci(num-1)+fibonacci(num-2))
    store[num]=x
    return x
x=fibonacci(101)
for num in range(0,101):
    print(fibonacci(num))