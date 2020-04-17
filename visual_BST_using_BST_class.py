from tkinter import *
import random
import time
from BST_class import BST

class VisualBST:
    def __init__(self):
        self.outlineColor = '#1e1e1e'
        self.mainScreenColor = '#e6e6e6'
        self.menuBarColor = '#34495e'
        self.nodeColor = '#32e632'
        self.buttonColor = '#1abc9c'

        self.canvasHeight = 600
        self.canvasWidth = 1200

        self.window = Tk()
        self.window.title('Visual BST')

        self.window.geometry(f"{self.canvasWidth}x{self.canvasHeight}")

        self.showSteps = IntVar()
        self.avl = IntVar()

        self.addNodeButton = Button(self.window, width=10, font=('arial', 14), text='add node', borderwidth=0, command=self.addEntry)
        self.deleteNodeButton = Button(self.window, width=10, font=('arial', 14), text='delete node', borderwidth=0, command=self.removeEntry)    
        self.newNodeEntry = Entry(self.window, font=('arial', 13), width=26, borderwidth=0, justify=CENTER)
        self.generateRandomTreeButton = Button(self.window, width=20, font=('arial', 14), text='generate random tree', borderwidth=0, command=self.generateRandomTree)  
        self.numOfRandomNodesEntry = Entry(self.window, font=('arial', 13), width=25, borderwidth=0, justify=CENTER)
        self.balanceTreeButton = Button(self.window, width=15, font=('arial', 14), text='balance tree', borderwidth=0, command=self.balanceTree)  
        self.showStepsCheckBox = Checkbutton(self.window, font=('arial', 12), text="show steps", variable=self.showSteps)
        self.clearTreeButton = Button(self.window, width=10, font=('arial', 14), text='clear tree', borderwidth=0, command=self.clearTree)  
        self.canvas = Canvas(self.window, height = self.canvasHeight-80, width = self.canvasWidth, borderwidth=0, highlightthickness=0)
        self.avlRB = Radiobutton(self.window, text="AVL", font=('arial', 14), variable=self.avl, bg=self.menuBarColor, fg=self.buttonColor, value=1, command=self.setColorScheme)
        self.bstRB = Radiobutton(self.window, text="BST", font=('arial', 14), variable=self.avl, bg=self.menuBarColor, fg=self.buttonColor, value=0, command=self.setColorScheme)


        self.colorScheme = IntVar()
        self.colorScheme.set(0)

        self.darkRB = Radiobutton(self.window, text="dark", font=('arial', 10, 'bold'), variable=self.colorScheme, bg=self.menuBarColor, fg=self.buttonColor, value=1, command=self.setColorScheme)
        self.lightRB = Radiobutton(self.window, text="light", font=('arial', 10, 'bold'), variable=self.colorScheme, bg=self.menuBarColor, fg=self.buttonColor, value=0, command=self.setColorScheme)

        self.setColorScheme()
     
        self.addNodeButton.place(x=5,y=5)
        self.deleteNodeButton.place(x=125,y=5)
        self.newNodeEntry.place(x=5, y=48)
        self.generateRandomTreeButton.place(x=300,y=5)
        self.numOfRandomNodesEntry.place(x=300, y=48)
        self.balanceTreeButton.place(x=600,y=5)
        self.showStepsCheckBox.place(x=640, y=45)
        self.avlRB.place(x=850, y=5)
        self.bstRB.place(x=850, y=40)
        self.clearTreeButton.place(x=970,y=5)
        self.darkRB.place(x=1130, y=0)
        self.lightRB.place(x=1130, y=20)
        self.canvas.pack(side='bottom')

        self.nodeWidth = 30

        self.adding = False
        self.deleting = False

        self.n = 0

        self.bst = BST()

        self.userInputAndVisualize()

    def setColorScheme(self):
        if self.colorScheme.get() == 1:
            self.outlineColor = '#e6e6e6'
            self.mainScreenColor = '#1e1e1e'
            self.menuBarColor = '#252526'
            self.nodeColor = '#32e632'
            self.buttonColor = '#23a7f2'
        else:
            self.outlineColor = '#1e1e1e'
            self.mainScreenColor = '#e6e6e6'
            self.menuBarColor = '#34495e'
            self.nodeColor = '#32e632'
            self.buttonColor = '#1abc9c'

        self.window.configure(bg=self.menuBarColor)
        self.canvas.configure(bg=self.mainScreenColor)
        self.addNodeButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.deleteNodeButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.newNodeEntry.configure(bg=self.mainScreenColor, fg=self.outlineColor, insertbackground=self.outlineColor)
        self.generateRandomTreeButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.numOfRandomNodesEntry.configure(bg=self.mainScreenColor, fg=self.outlineColor, insertbackground=self.outlineColor)
        self.balanceTreeButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.showStepsCheckBox.configure(bg=self.menuBarColor, fg=self.buttonColor, activebackground=self.menuBarColor, activeforeground=self.buttonColor)
        self.avlRB.configure(bg=self.menuBarColor, fg=self.buttonColor, activebackground=self.menuBarColor, activeforeground=self.buttonColor)
        self.bstRB.configure(bg=self.menuBarColor, fg=self.buttonColor, activebackground=self.menuBarColor, activeforeground=self.buttonColor)
        self.clearTreeButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.darkRB.configure(bg=self.menuBarColor, fg=self.buttonColor, activebackground=self.menuBarColor, activeforeground=self.buttonColor)
        self.lightRB.configure(bg=self.menuBarColor, fg=self.buttonColor, activebackground=self.menuBarColor, activeforeground=self.buttonColor)
        
    def addEntry(self):
        self.adding = True
        if len(self.newNodeEntry.get()) == 0:
            self.n = 0
        else:
            self.n = self.newNodeEntry.get()

        self.newNodeEntry.delete(first=0, last='end')

    def removeEntry(self):
        self.deleting = True
        if len(self.newNodeEntry.get()) == 0:
            self.n = 0
        else:
            self.n = self.newNodeEntry.get()

        self.newNodeEntry.delete(first=0, last='end')

    def clearTree(self):
        self.canvas.delete("all")
        self.bst.root = None

    def generateRandomTree(self):
        self.canvas.delete("all")
        self.bst.root = None

        randomAr = random.sample(range(1000), int(self.numOfRandomNodesEntry.get()))

        for x in randomAr:
            self.bst.root = self.bst.insert(self.bst.root, x)

        self.numOfRandomNodesEntry.delete(first=0, last='end')

    def balanceTree(self):
        self.canvas.delete("all")
        self.balance(self.bst.root)

    def userInputAndVisualize(self):
        loopActive = True
        while loopActive:
            self.canvas.update()

            if self.n == 0:
                self.inorder(self.bst.root, 30, 600, 300)
                
            elif int(self.n) == -1:
                self.canvas.quit()
                loopActive = False

            else:
                if self.adding:
                    self.bst.root = self.bst.insert(self.bst.root, int(self.n))
                    self.adding = False

                elif self.deleting:
                    self.canvas.delete("all")
                    self.bst.root = self.bst.deleteEntry(self.bst.root, int(self.n))
                    self.deleting = False

                if self.avl.get() == 1:
                    self.balance(self.bst.root)
                    
                self.n = 0
                self.inorder(self.bst.root, 30, 600, 300)

    def inorder(self, subRoot, row, col, sep): 
        if subRoot: 
            if subRoot.right != None:
                self.canvas.create_line(col, row, col + sep, row + 50, width=2, fill=self.outlineColor)
            if subRoot.left != None:
                self.canvas.create_line(col, row, col - sep, row + 50, width=2, fill=self.outlineColor)

            self.inorder(subRoot.left, row + 50, col - sep, sep / 2) 
            
            #print(subRoot.data, end=" ") 
            self.canvas.create_oval(col-self.nodeWidth/2, row-self.nodeWidth/2, col+self.nodeWidth/2, row+self.nodeWidth/2, fill=self.nodeColor, outline=self.outlineColor, width=2)
            self.canvas.create_text(col, row, text=str(subRoot.data), fill='black', font = ('arial', 10, 'bold'))

            self.inorder(subRoot.right, row + 50, col + sep, sep / 2) 

    def balance(self, subRoot):
        while True:
            if (self.showSteps.get() == 1):
                self.canvas.update()
                self.canvas.delete("all")
                self.inorder(self.bst.root, 30, 600, 300)
                time.sleep(0.1)

            if (subRoot == None):
                break

            numOfLeftNodes = self.bst.countNodes(subRoot.left)
            numOfRightNodes = self.bst.countNodes(subRoot.right)

            if (abs(numOfLeftNodes - numOfRightNodes) <= 1):
                self.balance(subRoot.left)
                self.balance(subRoot.right)
                break

            elif (numOfLeftNodes > numOfRightNodes):
                self.bst.rightRotate(subRoot)
            
            elif (numOfLeftNodes < numOfRightNodes):
                self.bst.leftRotate(subRoot)

VisualBST()