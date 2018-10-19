#CS2302
#Aaron Brown
#Diego Aguirre
#Anindita Nath
#10/18/18
#Find duplicate IDs in a linked list
import random
import time
import matplotlib.pyplot as plt

def main():
    mergedIDs = mergeIDs()
    mergedIDs2 = copyList(mergedIDs)
    mergedIDs3 = copyList(mergedIDs)
    mergedIDs4 = copyList(mergedIDs)
    mergedIDs5 = copyList(mergedIDs)
    ##solutions on original merged text file
    solution1List = solution1(mergedIDs2)
    print('Solution1 number of duplicates' , end =':')
    print(listLength(solution1List))

    solution2List = solution2(mergedIDs3)
    print('Solution2 number of duplicates' , end =':')
    print(listLength(solution2List))

    solution3List = solution3(mergedIDs4)
    print('Solution3 number of duplicates', end =':')
    print(listLength(solution3List))

    maxID = getLargestID(mergedIDs)
    solution4List = solution4(mergedIDs5 , maxID)
    print('Solution4 number of duplicates', end =':')
    print(listLength(solution4List))
    ##run times for solutions on other lists
    displayRunTimes()
    
def displayRunTimes():#displays solution run times on a graph
    plt.figure(1 , figsize = (15,15))
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 =[]
    for i in range(0, 10000, 1000):        
        idList1 = createIDList(i , i) #largest id , size of list
        idList2 = copyList(idList1)
        idList3 = copyList(idList1)
        idList4 = copyList(idList1)
        idList5 = copyList(idList1)       
        x.append(i)
        startTime = time.clock() 
        solution1(idList1)
        endTime = time.clock()
        y1.append((endTime - startTime))        
        startTime = time.clock() 
        solution2(idList2)
        endTime = time.clock()
        y2.append((endTime - startTime))
        startTime = time.clock() 
        solution3(idList3 )
        endTime = time.clock()
        y3.append((endTime - startTime))     
        startTime = time.clock() 
        solution4(idList4 , getLargestID(idList4))
        endTime = time.clock()
        y4.append((endTime - startTime))
    plt.plot(x,y1 , label = 'Solution1 - Nested Loops')
    plt.plot(x,y2 , label = 'Solution2 - BubbleSort')
    plt.plot(x,y3 , label = 'Solution3 - MergeSort')  
    plt.plot(x,y4, label = 'Solution4 - seen array')
    plt.xlabel('List Size')
    plt.ylabel('Running Time')
    plt.title("Solution Running Times")
    plt.legend()
    plt.show()
    
def mergeIDs(): #returns linked list of original provided files merged
    node = Node(-1,None)
    cur = node
    activisionIds = open('activision.txt')    
    for employeeID in activisionIds:
       cur.next = Node(int(employeeID),None)
       cur = cur.next       
    activisionIds.close()
    vivendiIds = open('vivendi.txt')    
    for employeeID in vivendiIds:
       cur.next = Node(int(employeeID),None)
       cur = cur.next
    return node.next
 
def solution1(node):            #compares every id with every other id using nested loops
    if node == None or node.next == None:
        return None    
    cur = node
    cur2 = node.next
    cur3 = node    
    duplicates = Node(-1,None)
    cur4 = duplicates    
    while cur.next != None:
        hasDuplicates = False
        while cur2 != None:
            if cur.item == cur2.item:
                cur4.next = Node(cur.item,None)
                cur4 = cur4.next
                hasDuplicates = True
                cur3.next = cur2.next
            else:
                cur3 = cur3.next
            cur2 = cur2.next
        cur3 = cur.next
        if hasDuplicates == True:
            cur4.next = Node(cur.item,None)
            cur4 = cur4.next
        if cur.next != None:
            cur = cur.next
        if cur != None:
            cur2 = cur.next
    return duplicates.next

def solution2(node): #bubblesorts list then checks sorted list for duplicates
    sortedList = bubbleSort(node)
    return sortedListCheck(sortedList)

def solution3(node):  #mergesorts list then checks sorted list for duplicates
    sortedList = mergeSort(node)
    return sortedListCheck(sortedList)

def solution4(node,m):  #checks elements in a loop and compares if the have been seen or not
    seen = []
    for i in range(m+1):
        seen.append(0)
    cur = node
    duplicates = Node(-1,None)
    while cur != None:
        seen[int(cur.item)] += 1
        cur = cur.next        
    cur2 = duplicates
    for i in range(len(seen)):
        if seen[i] > 1:
            for j in range(seen[i]):
                cur2.next = Node(i,None)
                cur2 = cur2.next                
    return duplicates.next

def bubbleSort(node):            #bubblesort list
    if node == None:
        return None
    if node.next == None:
        return node
    start = Node(-1,node)
    list_Length = listLength(node)
    for i in range(1,list_Length):
        prev = Node(-1,start.next)
        cur = start.next
        cur2 = cur.next
        for j in range(list_Length - i):
            if cur.item > cur2.item:
                cur.next = cur2.next
                cur2.next = cur
                prev.next = cur2
                temp = cur2
                cur2 = cur
                cur = temp
            if start.next == cur2:
                start.next = cur
            cur = cur.next
            cur2 = cur2.next
            prev = prev.next
                
    return start.next

def sortedListCheck(node): #checks sorted list for duplicates by comparing neighboring elements
    if node == None or node.next == None:
        return None   
    cur = None
    cur2 = node
    duplicatesList = Node(-1,None)
    cur3 = duplicatesList
    while cur2 != None:
        duplicates = 0
        cur = cur2
        cur2 = cur2.next
        while cur2 != None and cur.item == cur2.item:
                duplicates += 1
                cur2 = cur2.next
        if duplicates > 0:
            for i in range(duplicates+1):
                cur3.next = Node(cur.item , None)
                cur3 = cur3.next          
    if duplicatesList.next != None:
        return duplicatesList.next
    else:
        return None
  
def mergeSort(node):        #mergesort
    cur = node
    if node != None and node.next != None:
        list1 , list2 = splitList(node)
        list3 = mergeSort(list1)
        list4 = mergeSort(list2)
        return merge(list3 , list4)
    return cur

def splitList(node):    #separates list into two separate lists
    if node.next != None:
        cur = node
        cur2 = node
        while  cur2.next.next != None and cur2.next.next.next != None:
            cur = cur.next
            cur2 = cur2.next.next
        cur3 = cur.next
        cur.next = None
        return node , cur3
    else:
        return node , None

def merge(list1 , list2):   #combines two lists into one
    list3 = Node(-1,None)
    cur = list1
    cur2 = list2
    cur3 = list3
    while cur!=None and cur2 != None:
        if cur.item < cur2.item:
            cur3.next = Node(cur.item, None)
            cur3 = cur3.next
            cur = cur.next
        else:
            cur3.next = Node(cur2.item,None)
            cur3 = cur3.next
            cur2 = cur2.next           
    while cur != None:
        cur3.next = Node(cur.item,None)
        cur3 = cur3.next
        cur = cur.next
    while cur2 != None:
        cur3.next = Node(cur2.item , None)
        cur3 = cur3.next
        cur2 = cur2.next
    return list3.next

def createIDList(largestID , size): #creates a text file with random IDs
    node = Node(-1,None)
    cur = node
    for i in range(size):
        cur.next = Node(int(random.random()* largestID) , None)
        cur = cur.next
    return node.next
    
def listLength(node):   #length of list
    counter = 0
    while node != None:
        node = node.next
        counter += 1
    return counter

def getLargestID(node): #returns largest ID in list
    cur = node
    maxID = -1
    while cur != None:
        if int(cur.item) > maxID:
            maxID = int(cur.item)
        cur = cur.next
    return maxID
    
def printList(node):    #prints linked list
    if node == None:
        return
    print(node.item)
    while node.next != None:
        node = node.next
        print(node.item)

def copyList(node): #returns a copy of linked list
    cur = node
    node2 = Node(-1,None)
    cur2 = node2
    while cur != None:
        node2.next = Node(cur.item,None)
        cur = cur.next
        node2 = node2.next
    return cur2.next

class Node(object):
    item = -1
    next = None

    def __init__(self, item , next):
        self.item = item
        self.next = next

main()
