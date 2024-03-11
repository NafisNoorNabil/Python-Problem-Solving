
#factorial

def fact(num):

  if num == 0:

    return 0

  elif num == 1:

    return 1

  else:

    return num*fact(num-1)