#sum of digits

def sum_of_digits(num,sum):

  if num == 0:

    return sum

  return sum_of_digits(int(num/10), sum+(num%10))