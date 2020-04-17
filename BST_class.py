class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

class BST:
    def __init__(self):
        self.root = None

    def createNode(self, d):
        temp = Node(d)
        return temp

    def insert(self, subRoot, d):
        if subRoot == None:
            return self.createNode(d)
        
        elif d < subRoot.data:
            subRoot.left = self.insert(subRoot.left, d)

        else:
            subRoot.right = self.insert(subRoot.right, d)

        return subRoot


    def inorder(self, subRoot): 
        if subRoot: 
            self.inorder(subRoot.left) 
            print(subRoot.data, end=" ") 
            self.inorder(subRoot.right) 

    def countNodes(self, subRoot):
        count = 1
        if subRoot == None:
            return 0

        if subRoot.left != None:
            count += self.countNodes(subRoot.left)

        if subRoot.right != None:
            count += self.countNodes(subRoot.right)

        return count

    def minValueSubTree(self, subRoot):
        current = subRoot

        while (current and current.left != None):
            current = current.left

        return current

    def maxValueSubTree(self, subRoot):
        current = subRoot

        while (current and current.right != None):
            current = current.right

        return current

    def prevInOrder(self, subRoot):
        current = subRoot
        current = current.left

        while (current and current.right != None):
            current = current.right

        return current

    def nextInOrder(self, subRoot):
        current = subRoot
        current = current.right

        while (current and current.left != None):
            current = current.left

        return current

    def deleteEntry(self, subRoot, d):
        if (subRoot == None):
            return None
        
        elif (d > subRoot.data): 
            subRoot.right = self.deleteEntry(subRoot.right, d)
        
        elif (d < subRoot.data): 
            subRoot.left = self.deleteEntry(subRoot.left, d)
        
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
                temp = self.minValueSubTree(subRoot.right)
                subRoot.data = temp.data
                subRoot.right = self.deleteEntry(subRoot.right, temp.data)

        return subRoot

    def leftRotate(self, subRoot):
        prevNode = self.prevInOrder(subRoot)
        nextNode = self.nextInOrder(subRoot)

        if (nextNode == None): 
            print("cant left rotate")
            return None

        if (prevNode == None):
            newNode = self.createNode(subRoot.data)
            subRoot.left = newNode
            nextData = nextNode.data

            self.root = self.deleteEntry(self.root, nextNode.data)
            subRoot.data = nextData
        
        else: 
            newNode = self.createNode(subRoot.data)
            prevNode.right = newNode
            nextData = nextNode.data

            self.root = self.deleteEntry(self.root, nextNode.data)
            subRoot.data = nextData

    def rightRotate(self, subRoot):
        prevNode = self.prevInOrder(subRoot)
        nextNode = self.nextInOrder(subRoot)

        if (prevNode == None): 
            print("cant right rotate")
            return None

        if (nextNode == None):
            newNode = self.createNode(subRoot.data)
            subRoot.right = newNode
            prevData = prevNode.data

            self.root = self.deleteEntry(self.root, prevNode.data)
            subRoot.data = prevData
        
        else: 
            newNode = self.createNode(subRoot.data)
            nextNode.left = newNode
            prevData = prevNode.data

            self.root = self.deleteEntry(self.root, prevNode.data)
            subRoot.data = prevData

    def balance(self, subRoot):
        while True:
            if (subRoot == None):
                break

            numOfLeftNodes = self.countNodes(subRoot.left)
            numOfRightNodes = self.countNodes(subRoot.right)

            if (abs(numOfLeftNodes - numOfRightNodes) <= 1):
                self.balance(subRoot.left)
                self.balance(subRoot.right)
                break

            elif (numOfLeftNodes > numOfRightNodes):
                self.rightRotate(subRoot)
            
            elif (numOfLeftNodes < numOfRightNodes):
                self.leftRotate(subRoot)



