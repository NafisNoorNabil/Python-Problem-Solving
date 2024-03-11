
def powerN(base,n):

  if (n==0):
    return 1

  else:
    m=powerN(base,n-1)
    return m*base 
 
print(powerN(3,3))