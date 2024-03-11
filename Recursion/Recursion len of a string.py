#length_of_string recursive function

def length_of_string(s):

  if s == '':

    return 0

  else:

    return 1+length_of_string(s[1:])