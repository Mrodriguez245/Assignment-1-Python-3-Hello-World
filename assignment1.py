def stringCount(vars):
    #change string of characters to string
    vars = vars.split()
    #counts how many times the word occurs (word, count)
    contain = {}
    for x in vars:
        contain[x] = contain.get(x, 0) + 1
    
    #sort by value (occurences of the string)
    new_var = []
    for key, value in contain.items():
        new_var.append((value, key))
    new_var.sort(reverse = False)
    print(new_var)

    #temp = Counter(var)  ONLY USE THIS
    #for words, values in temp.items()
    #   print (words, " " ,values)
    

def isFloat(value):
    import re
    #definition of float in regular expressions
    result = re.search("([-+]?\d+\.\d*)|([-+]?\d*\.\d+)", value)
    if (result):
        print("True") 
    else:
        print("False") 

#class Node and LinkedList
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def getData(self):
        return self.data
    def getNext(self):
       return self.next
    def setData(self,val):
        self.data = val
    def setNext(self,val):
       self.next = val   
            
class LinkedList:
    def __init__(self,head = None):
       self.head = head
       self.size = 0
#return size of list (amount of nodes)
    def size():
        return self.size
#insert node at the tail of the list
    def insert(self,data):
       newNode = Node(data,self.head)
       self.head = newNode
       self.size+=1
       return True
#prints all nodes
    def printLL(self):
       cur = self.head
       while cur:
           print(cur.data)
           cur = cur.getNext()   
#deletes nodes of value val
    def delete(self,val):
        print_node = self.head
        cur = self.head
        prev = None
        #while not the end of the list keeo goijg
        while cur:
            #if val is the value passed in then set prev pointer to next node
            if cur.getData() == val:
                if prev:
                    prev.setNext(cur.getNext())
                else:
                    self.head = cur.getNext()
                size-=1
                printLL(print_node)
                return True
            prev = cur
            cur = cur.getNext()
        return False
    
    def search(self, val):
        cur = self.head
        while cur:
            if cur.getData == val:
                print ("Value " + val + " found")
        print ("Value " + val + " not found")
            
