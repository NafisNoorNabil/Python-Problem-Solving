

def houseofcards(h):
    if h == 0:
        return 0
    elif h==1:
        return 8
    else:
        m=houseofcards(h-1)
        return m+5
print(houseofcards(5))

  