import time
A = list()
def F(n):
    if (n==0 or n==1):
        return 1
    else:
        return F(n-1)+F(n-2)
def FM(n):
    if(A[n] > 0):
        return A[n]
    if(n == 0 or n==1):
        return 1
    else:
        return A[n].append(FM(n-1)+FM(n-2))
def CalcFib():
    A.insert(0,1)
    A.insert(1,1)
    for i in range(2,46):
        A.insert(i,A[i-1]+A[i-2])

#-------------Tester----------------#
CalcFib()
startTime = time.time_ns()
print(FM(45))
duration = time.time_ns()-startTime
print(duration)