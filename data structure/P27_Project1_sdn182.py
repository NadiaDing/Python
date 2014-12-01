

class List_Node():
    def __init__(self, v):
        self.Value = str(v)
        self.Next = None

    def __str__(self):       
        return str(self.Value) + ("" if self.Next == None else (" " + str(self.Next)))
## do not write any additional code in this class,
## including do not add your netID to the class name



    

class Linked_List(object):
    def __init__(self):
        self.Head = None

    def __str__(self):
        return ("" if self.Head == None else str(self.Head))
## do not write any additional code in this super-class,
## including do not add your netID to the class name




class Queue_sdn182(Linked_List):
    def __init__(self):
        super(Queue_sdn182, self).__init__()
        self.Tail = None
        self.count=0
    def isEmpty(self):
        return self.Head is None
    
    def Enqueue(self, v):
        node=List_Node(v)
        if self.isEmpty():
            self.Head=node
        else:
            self.Tail.Next=node
        self.Tail=node
        self.count+=1
    def Dequeue(self):
        v = None
        assert not self.isEmpty(), "Can't dequeue from an empty enqueue"
        node=self.Head
        if self.Head == self.Tail:
            self.Tail=None
        else:
            self.Head=self.Head.Next
            self.count-=1
        #print 'head.next', self.Head.Next
        v=node.Value
        return v





class Stack_sdn182(Linked_List):
    def __init__(self):
        super(Stack_sdn182, self).__init__()
        self.size=0
        self.Head=None
    
    
    def isEmpty(self):
        return self.Head is None
  
    
    def Push(self, v):
    ## write Push
        node=List_Node(v)
        if self.isEmpty():
            self.Head=node
        else:
            node.Next=self.Head
            self.Head=node
        
        self.size+=1
   
    def Read_Top(self):
        assert not self.isEmpty(), "Can't read from an empty stack"
        v = None
        node=self.Head
        v=node.Value
        ## write Read_Top
        return v
    
    def Pop(self):
        v=None
        assert not self.isEmpty(), "Can't pop from an empty stack"
        node = self.Head
        
        self.Head=self.Head.Next
        ## write Pop
        self.size-=1
        v=node.Value
        
        return v




class Scheme_Object(Stack_sdn182):
    def __init__(self):
        super(Scheme_Object, self).__init__()
        self.Operator = None

    def __str__(self):
        return ("(SO-start " + str(self.Operator) + " " 
    + ("" if self.Head == None else str(self.Head)) + " SO-end) ")
## change the two references to class Stack_ to be your netID

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def Get_Scheme_Object_sdn182(string):

    print "begin queue"
    queue = Queue_sdn182()
   

    ## use string operations to
    ## translate the input string into a queue of List_Nodes
    ## {one node per token}
    str3= string
    str1=['' for j in range(100)]
    m=len(str3)
    j=0
    for i in range(0,m):
        if str3[i]==' ':
            j+=1
        else:
            str1[j]+=str3[i]

    str2=str1[0:j+1]
    for i in range(j+1):
        n=str2[i]
        queue.Enqueue(n)

        ## MAKE SURE THIS NEXT PRINT COMMAND IS PRESENT AND UNCOMMENTED
        ## WHEN YOU TURN IN YOUR FINAL SUBMISSION- IT IS REQUIRED FOR GRADING
        print queue
        ## end while-loop block

                


    print "\n begin stack"
    working = Stack_sdn182()
    ## transfer the elements of the queue to a Working Stack
    ## by using the given while-loop
    w=queue.Dequeue()
    while( queue != ""):
        while (w != ")" ):
            working.Push(w)
            print  working
            if queue.isEmpty():
                break
            else:
                w=queue.Dequeue()
        if queue.isEmpty():
            break
        else:
            w=queue.Dequeue()
        if working.isEmpty():
            break
        else:
            p=working.Pop()
        scheme_object=Scheme_Object()
        while ( p != "("):
            scheme_object.Push(p)

            if working.isEmpty():
                break
            else:
                p=working.Pop()

        working.Push(scheme_object)
        
#print working
        print "\n" + str(working)
        





        ## whenever the element just added to the Working Stack is ')',
        ## this represents the end of a scheme_object;
        ## start popping the Working Stack and placing elements into a new scheme_object
        ## {which represents a stack itself via inheritance} of List_Nodes;
        ## do this until you find the beginning of the scheme_object {element is '('}
        ## fix the scheme_object with respect to Operator and Head
        ## add the scheme_object itself back to the Working Stack








        

        ## keep these next two commands at the end of your while-loop block
        ## MAKE SURE THIS NEXT PRINT COMMAND IS PRESENT AND UNCOMMENTED
        ## WHEN YOU TURN IN YOUR FINAL SUBMISSION- IT IS REQUIRED FOR GRADING

        ## set condition anew by ***Rewriting the assignment in this
        ## next line as appropriate
#   condition = (True)
        ## end while-loop block
    

    ## after exiting the while-loop, the Working Stack should
    ## consist of a single element {a scheme_object "stack"}
    ## return a pointer to this single element

    return working.Pop()




if __name__ == "__main__":

    ## test code here
    
    ## formatted_expression is what it would look like using scheme
    ## (this is a throwaway string, it is simply easier to read)
    scheme_formatted_expression = "(inc (+ 1 2 (- 12 4) (* (- 1) 7 (+ 3 (- (half 12) 1)))))"
    
    ## assume some "pre-processing" has been done to add spaces in the convenient places as:
    scheme_expression = "( inc ( + 1 2 ( - 12 4 ) ( * ( - 1 ) 7 ( + 3 ( - ( half 12 ) 1 ) ) ) ) )"
    
    scheme_object = Get_Scheme_Object_sdn182(scheme_expression)
    print "\n"
    print scheme_object

    
