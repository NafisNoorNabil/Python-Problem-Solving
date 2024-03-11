
#length_of_linkedlist recursive function

def length(self,node):    

    if node is None:

      return 0

    else:

      return 1+ self.length(node.next)