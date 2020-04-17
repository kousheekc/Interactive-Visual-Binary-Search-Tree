class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def createNode(d):
    temp = Node(d)
    return temp

def insert(subRoot, d):
    if subRoot == None:
        return createNode(d)
    
    elif d < subRoot.data:
        subRoot.left = insert(subRoot.left, d)

    else:
        subRoot.right = insert(subRoot.right, d)

    return subRoot

def inorder(subRoot): 
    if subRoot: 
        inorder(subRoot.left) 
        print(subRoot.data, end=" ") 
        inorder(subRoot.right) 

def countNodes(subRoot):
    count = 1
    if subRoot == None:
        return 0

    if subRoot.left != None:
        count += countNodes(subRoot.left)

    if subRoot.right != None:
        count += countNodes(subRoot.right)

    return count

def minValueSubTree(subRoot):
    current = subRoot

    while (current and current.left != None):
        current = current.left

    return current

def maxValueSubTree(subRoot):
    current = subRoot

    while (current and current.right != None):
        current = current.right

    return current

def prevInOrder(subRoot):
    current = subRoot
    current = current.left

    while (current and current.right != None):
        current = current.right

    return current

def nextInOrder(subRoot):
    current = subRoot
    current = current.right

    while (current and current.left != None):
        current = current.left

    return current

def deleteEntry(subRoot, d):
    if (subRoot == None):
        return None
    
    elif (d > subRoot.data): 
        subRoot.right = deleteEntry(subRoot.right, d)
    
    elif (d < subRoot.data): 
        subRoot.left = deleteEntry(subRoot.left, d)
    
    else: 
        if (subRoot.left == None and subRoot.right == None):
            subRoot = None
            return subRoot
        
        elif (subRoot.left == None): 
            temp = subRoot.right
            subRoot = None
            return temp
        
        elif (subRoot.right == None): 
            temp = subRoot.left
            subRoot = None
            return temp
        
        else: 
            temp = minValueSubTree(subRoot.right)
            subRoot.data = temp.data
            subRoot.right = deleteEntry(subRoot.right, temp.data)

    return subRoot

def leftRotate(subRoot):
    global root
    prevNode = prevInOrder(subRoot)
    nextNode = nextInOrder(subRoot)

    if (nextNode == None): 
        print("cant left rotate")
        return None

    if (prevNode == None):
        newNode = createNode(subRoot.data)
        subRoot.left = newNode
        nextData = nextNode.data

        root = deleteEntry(root, nextNode.data)
        subRoot.data = nextData
    
    else: 
        newNode = createNode(subRoot.data)
        prevNode.right = newNode
        nextData = nextNode.data

        root = deleteEntry(root, nextNode.data)
        subRoot.data = nextData

def rightRotate(subRoot):
    global root
    prevNode = prevInOrder(subRoot)
    nextNode = nextInOrder(subRoot)

    if (prevNode == None): 
        print("cant right rotate")
        return None

    if (nextNode == None):
        newNode = createNode(subRoot.data)
        subRoot.right = newNode
        prevData = prevNode.data

        root = deleteEntry(root, prevNode.data)
        subRoot.data = prevData
    
    else: 
        newNode = createNode(subRoot.data)
        nextNode.left = newNode
        prevData = prevNode.data

        root = deleteEntry(root, prevNode.data)
        subRoot.data = prevData

def balance(subRoot):
    while True:
        if (subRoot == None):
            break

        numOfLeftNodes = countNodes(subRoot.left)
        numOfRightNodes = countNodes(subRoot.right)

        if (abs(numOfLeftNodes - numOfRightNodes) <= 1):
            balance(subRoot.left)
            balance(subRoot.right)
            break

        elif (numOfLeftNodes > numOfRightNodes):
            rightRotate(subRoot)
        
        elif (numOfLeftNodes < numOfRightNodes):
            leftRotate(subRoot)
        
    

n = [650,400,80,906,100,70,275,676,377,178,779,874,73,2,51]

root = None

for i in n:
    root = insert(root, i)

inorder(root)
root = deleteEntry(root, 80)
balance(root)
print()
inorder(root)
