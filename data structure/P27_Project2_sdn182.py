

class List_Node():
    def __init__(self, v):
        self.Value = v
        self.Next = None
## do not write any additional code in this class,
## including do not add your netID to the class name



    

class Linked_List(object):
    def __init__(self):
        self.Head = None

## do not write any additional code in this super-class,
## including do not add your netID to the class name




class Queue(Linked_List):
    def __init__(self):
        super(Queue, self).__init__()
        self.Tail = None
        self.count = 0

    def Enqueue(self, v):
        ## Write Enqueue
        n = List_Node(v)
        self.count = self.count + 1
        if self.Head == None:
            self.Head = n
            self.Tail = n
        else:
            self.Tail.Next = n
            self.Tail = n

    def Dequeue(self):
        v = None
        ## write Dequeue
        if self.Head == None:
            print ("queue empty")
            return
        else:
            v = self.Head.Value
            self.Head = self.Head.Next
            self.count = self.count - 1
        return v
## do not write any additional code in this class,
## including do not add your netID to the class name


    


class Tree_Node_sdn182():
    def __init__(self, v):
        self.Value = v
        self.Parent = None
        self.LeftChild = None
        self.RightChild = None
        self.Predecessor = None
        self.Successor = None
        self.RankCounter = 1
## UPDATE the value of RankCounter within the constructor

    def Find_Subtree_Min(self):
        m = self
        while m.LeftChild != None:
            m = m.LeftChild
        return m

    def Find_Subtree_Max(self):
        m = self
        while m.RightChild != None:
            m = m.RightChild
        return m

    def Set_Successor(self):
        if self.RightChild != None:
            return self.RightChild.Find_Subtree_Min()
        else:
            a1 = self.Parent
            a2 = self
            while a1 != None:
                if a1.LeftChild != None and a1.LeftChild.Value == a2.Value:
                    return a1
                a1 = a1.Parent
                a2 = a2.Parent
        
            return None

    def Set_Predecessor(self):
        ## write Set_Predecessor
        if self.LeftChild!=None:
            return self.LeftChild.Find_Subtree_Max()
        else:
            x=self
            y=x.Parent
            while y!=None and x==y.LeftChild:
                x=y
                y=y.Parent
            return y

class Tree_sdn182():
    def __init__(self):
        self.Root = None
        self.Min = None
        self.Max = None


    def Insert(self, v):
        ## write Insert
        newNode = Tree_Node_sdn182(v)
        if self.Root==None:
            self.Root=newNode
        else:
            x=self.Root
            y=x
            while (x!=None):
                y=x
                
                if newNode.Value==x.Value:
                    return False
                elif newNode.Value<x.Value:
                    x.RankCounter+=1
                    x=x.LeftChild
                else:
                    x.RankCounter+=1
                    x=x.RightChild
        
            if y.Value>newNode.Value:
                y.LeftChild=newNode
                newNode.Parent=y
                newNode.Predecessor=y.Predecessor
                newNode.Successor=y
                y.Predecessor=newNode
            

            else:
                y.RightChild=newNode
                newNode.Parent=y
                newNode.Predecessor=y
                newNode.Successor=y.Successor
                y.Successor=newNode
    #print "root.count", self.Root.RankCounter
        self.Min=self.Root.Find_Subtree_Min()
        self.Max=self.Root.Find_Subtree_Max()

          
    def Search(self, v):
        ## write Search
        newNode=Tree_Node_sdn182(v)
        x=self.Root
        while x!=None:
            if newNode.Value==x.Value:
                return True
            elif newNode.Value>x.Value:
                x=x.RightChild
            else:
                x=x.LeftChild
        return False
                
    def BFS_Print(self):
        if self.Root == None:
            print "empty queue"
            return
        ## write BFS_Print
        r=self.Root
        Q=Queue()
        Q.Enqueue(r)
        while(Q.count!=0):
            x=Q.Dequeue()
            print x.Value
        
            if x.LeftChild!=None:
                Q.Enqueue(x.LeftChild)
            if x.RightChild!=None:
                Q.Enqueue(x.RightChild)
                    
                    
    def Find_Value_Of_Rank(self, r):
        if self.Root == None:
            return None
        if r < 1 or r > self.Node_Count():
            print "rank out of range"
            return
        x=self.Root
        i=x.LeftChild.RankCounter+1
            
        while i!=r:
            if i<r:
                x=x.RightChild
                r=r-i
                if x.LeftChild!=None:
                    i=x.LeftChild.RankCounter+1
                else:
                    i=1
            else:
                x=x.LeftChild
                if x.LeftChild!=None:
                    i=x.LeftChild.RankCounter+1
                else:
                    i=1
        return x.Value
            


    def Get_Rank_Of_Value(self, v):
        ## write Get_Rank_Of_Value
        x=self.Root
        rank=x.LeftChild.RankCounter+1
        #print "rank",rank
        while x!=None and x.Value!=v:
            if v<x.Value:
                x=x.LeftChild
                if x==None:
                    return None
                elif x.RightChild==None:
                    rank=rank-1
                else:
                    rank=rank-x.RightChild.RankCounter-1
            else:
                x=x.RightChild
                if x==None:
                    return None
                elif x.LeftChild==None:
                    rank=rank+1
                else:
                    rank=rank+x.LeftChild.RankCounter+1
    

        return rank

    


    def Node_Count(self):
        ## write Node_Count
        return self.Root.RankCounter







if __name__ == "__main__":

    ## test code here
    TREE = Tree_sdn182()

#LIST=[4,2,8,1,3,6,12,5,7,10,13,9,11]
    
    LIST = [1063,
            2121,
            9020,
            9015,
            6802,
            1613,
            8068,
            6171,
            8986,
            6799,
            7617,
            6500,
            4780,
            7159,
            1961,
            2816,
            5772,
            8020,
            7588,
            7758,
            744,
            5639,
            8609,
            8735,
            9997,
            4805,
            7759,
            8776,
            6884,
            7673,
            8611,
            5250,
            5417,
            9640,
            3504,
            3016,
            8359,
            9498,
            240,
            6833,
            4215,
            7548,
            7487,
            5884,
            2726,
            3979,
            8083,
            1442,
            6625,
            2571,
            9112,
            4458,
            4743,
            401,
            8267,
            5338,
            6599,
            6612,
            897,
            2663,
            8240,
            2612,
            6224,
            2302,
            4681,
            1634,
            6886,
            6047,
            6713,
            7813,
            4074,
            5734,
            4569,
            8117,
            6906,
            1444,
            4313,
            9990,
            3134,
            194,
            1465,
            5032,
            3306,
            349,
            7817,
            2093,
            6642,
            5578,
            4016,
            5092,
            6552,
            1805,
            5085,
            3091,
            3366,
            3336,
            2322,
            8777,
            6779]

    for el in LIST:
        TREE.Insert(el)

    finished = True
    for el in LIST:
        if not TREE.Search(el):
            finished = False
            print str(el) + " not inserted correctly"
            break
    if finished:
        print "Found all inserted values"

    finished = True
    for not_el in [1, 10, 100, 1000, 2000, 4000, 8000]:
        if TREE.Search(not_el):
            finished = False
            print str(not_el)+ "incorrectly found in list"
            break

    if finished:
        print "No bad values found"

    print "\nrun 1"
    TREE.BFS_Print()

    LIST.sort()
    print "\nMin:\n" + str(TREE.Min.Value)
    print "\nrun 2"
    for i in range(20):
        print LIST[5*i]

    print "\nrun 3"
    for i in range(20):
        print str(TREE.Find_Value_Of_Rank(5*i+1))

    print "\nrun 4"
    for i in range(500):
        if not (i < 30 or i > 470):
            continue
        x = TREE.Get_Rank_Of_Value(10*i)
        if i%2 == 0 or type(2) == type(x):
            print str(10*i) + "; " + str(x)
            
    
    print "\nrun 5"
    x = TREE.Min
    while x != None:
        print x.Value
        x = x.Set_Successor()

    print "\nrun 6"


    for i in range(1,100):
    
    
        y = TREE.Find_Value_Of_Rank(i)
    
    
        print y, TREE.Get_Rank_Of_Value(y)
