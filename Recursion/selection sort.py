
#selection sort recursive function

def selection_sort(a,i,j):
  l=len(a)

  if i == l and j==l:
    return -1


  if i < l:
    min=i

    if j < l:

      if a[j] < a[min]:

        min = j

      selection_sort(a,i,j+1)

    if min != i:

      temp=a[i]

      a[i]=a[j]

      a[j]=temp

    selection_sort(a,i+1,j+1)

#Tester

A=[22,5,14,2,7,1]

i=0

j=i+1

selection_sort(A,i,j)

print(A)
