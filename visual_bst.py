from tkinter import *
import random
import time
from bst import BST

class VisualBST:
    def __init__(self):
        self.outline_color = '#1e1e1e'
        self.mainscreen_color = '#e6e6e6'
        self.menubar_color = '#34495e'
        self.node_color = '#32e632'
        self.button_color = '#1abc9c'

        self.canvas_height = 600
        self.canvas_width = 1200

        self.window = Tk()
        self.window.title('Visual BST')

        self.window.geometry(f"{self.canvas_width}x{self.canvas_height}")

        self.show_steps = IntVar()
        self.avl = IntVar()
        self.color_scheme = IntVar()
        self.color_scheme.set(0)

        self.add_node_button = Button(self.window, width=10, font=('arial', 14), text='add node', borderwidth=0, command=self.add_entry)
        self.delete_node_button = Button(self.window, width=10, font=('arial', 14), text='delete node', borderwidth=0, command=self.remove_entry)    
        self.new_node_entry = Entry(self.window, font=('arial', 13), width=26, borderwidth=0, justify=CENTER)
        self.generate_random_tree_button = Button(self.window, width=20, font=('arial', 14), text='generate random tree', borderwidth=0, command=self.generate_random_tree)  
        self.num_of_random_nodes_entry = Entry(self.window, font=('arial', 13), width=25, borderwidth=0, justify=CENTER)
        self.balance_tree_button = Button(self.window, width=15, font=('arial', 14), text='balance tree', borderwidth=0, command=self.balance_tree)  
        self.show_steps_checkbox = Checkbutton(self.window, font=('arial', 12), text="show steps", variable=self.show_steps)
        self.clear_tree_button = Button(self.window, width=10, font=('arial', 14), text='clear tree', borderwidth=0, command=self.clear_tree)  
        self.canvas = Canvas(self.window, height = self.canvas_height-80, width = self.canvas_width, borderwidth=0, highlightthickness=0)
        self.avl_radiobutton = Radiobutton(self.window, text="AVL", font=('arial', 14), variable=self.avl, bg=self.menubar_color, fg=self.button_color, value=1, command=self.setcolor_scheme)
        self.bst_radiobutton = Radiobutton(self.window, text="BST", font=('arial', 14), variable=self.avl, bg=self.menubar_color, fg=self.button_color, value=0, command=self.setcolor_scheme)
        self.dark_radiobutton = Radiobutton(self.window, text="dark", font=('arial', 10, 'bold'), variable=self.color_scheme, bg=self.menubar_color, fg=self.button_color, value=1, command=self.setcolor_scheme)
        self.light_radiobutton = Radiobutton(self.window, text="light", font=('arial', 10, 'bold'), variable=self.color_scheme, bg=self.menubar_color, fg=self.button_color, value=0, command=self.setcolor_scheme)

        self.setcolor_scheme()
     
        self.add_node_button.place(x=5,y=5)
        self.delete_node_button.place(x=125,y=5)
        self.new_node_entry.place(x=5, y=48)
        self.generate_random_tree_button.place(x=300,y=5)
        self.num_of_random_nodes_entry.place(x=300, y=48)
        self.balance_tree_button.place(x=600,y=5)
        self.show_steps_checkbox.place(x=640, y=45)
        self.avl_radiobutton.place(x=850, y=5)
        self.bst_radiobutton.place(x=850, y=40)
        self.clear_tree_button.place(x=970,y=5)
        self.dark_radiobutton.place(x=1130, y=0)
        self.light_radiobutton.place(x=1130, y=20)
        self.canvas.pack(side='bottom')

        self.node_width = 30

        self.adding = False
        self.deleting = False

        self.n = 0

        self.bst = BST()

        self.user_input_and_visualize()

    def setcolor_scheme(self):
        if self.color_scheme.get() == 1:
            self.outline_color = '#e6e6e6'
            self.mainscreen_color = '#1e1e1e'
            self.menubar_color = '#252526'
            self.node_color = '#32e632'
            self.button_color = '#23a7f2'
        else:
            self.outline_color = '#1e1e1e'
            self.mainscreen_color = '#e6e6e6'
            self.menubar_color = '#34495e'
            self.node_color = '#32e632'
            self.button_color = '#1abc9c'

        self.window.configure(bg=self.menubar_color)
        self.canvas.configure(bg=self.mainscreen_color)
        self.add_node_button.configure(fg=self.mainscreen_color, bg=self.button_color, activebackground=self.button_color, activeforeground=self.mainscreen_color)
        self.delete_node_button.configure(fg=self.mainscreen_color, bg=self.button_color, activebackground=self.button_color, activeforeground=self.mainscreen_color)
        self.new_node_entry.configure(bg=self.mainscreen_color, fg=self.outline_color, insertbackground=self.outline_color)
        self.generate_random_tree_button.configure(fg=self.mainscreen_color, bg=self.button_color, activebackground=self.button_color, activeforeground=self.mainscreen_color)
        self.num_of_random_nodes_entry.configure(bg=self.mainscreen_color, fg=self.outline_color, insertbackground=self.outline_color)
        self.balance_tree_button.configure(fg=self.mainscreen_color, bg=self.button_color, activebackground=self.button_color, activeforeground=self.mainscreen_color)
        self.show_steps_checkbox.configure(bg=self.menubar_color, fg=self.button_color, activebackground=self.menubar_color, activeforeground=self.button_color)
        self.avl_radiobutton.configure(bg=self.menubar_color, fg=self.button_color, activebackground=self.menubar_color, activeforeground=self.button_color)
        self.bst_radiobutton.configure(bg=self.menubar_color, fg=self.button_color, activebackground=self.menubar_color, activeforeground=self.button_color)
        self.clear_tree_button.configure(fg=self.mainscreen_color, bg=self.button_color, activebackground=self.button_color, activeforeground=self.mainscreen_color)
        self.dark_radiobutton.configure(bg=self.menubar_color, fg=self.button_color, activebackground=self.menubar_color, activeforeground=self.button_color)
        self.light_radiobutton.configure(bg=self.menubar_color, fg=self.button_color, activebackground=self.menubar_color, activeforeground=self.button_color)
        
    def add_entry(self):
        self.adding = True
        if len(self.new_node_entry.get()) == 0:
            self.n = 0
        else:
            self.n = self.new_node_entry.get()

        self.new_node_entry.delete(first=0, last='end')

    def remove_entry(self):
        self.deleting = True
        if len(self.new_node_entry.get()) == 0:
            self.n = 0
        else:
            self.n = self.new_node_entry.get()

        self.new_node_entry.delete(first=0, last='end')

    def clear_tree(self):
        self.canvas.delete("all")
        self.bst.root = None

    def generate_random_tree(self):
        self.canvas.delete("all")
        self.bst.root = None

        random_array = random.sample(range(1000), int(self.num_of_random_nodes_entry.get()))

        for x in random_array:
            self.bst.root = self.bst.insert(self.bst.root, x)

        self.num_of_random_nodes_entry.delete(first=0, last='end')

    def balance_tree(self):
        self.canvas.delete("all")
        self.balance(self.bst.root)

    def user_input_and_visualize(self):
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
                    self.bst.root = self.bst.delete_entry(self.bst.root, int(self.n))
                    self.deleting = False

                if self.avl.get() == 1:
                    self.balance(self.bst.root)
                    
                self.n = 0
                self.inorder(self.bst.root, 30, 600, 300)

    def inorder(self, sub_root, row, col, sep): 
        if sub_root: 
            if sub_root.right != None:
                self.canvas.create_line(col, row, col + sep, row + 50, width=2, fill=self.outline_color)
            if sub_root.left != None:
                self.canvas.create_line(col, row, col - sep, row + 50, width=2, fill=self.outline_color)

            self.inorder(sub_root.left, row + 50, col - sep, sep / 2) 
            
            #print(sub_root.data, end=" ") 
            self.canvas.create_oval(col-self.node_width/2, row-self.node_width/2, col+self.node_width/2, row+self.node_width/2, fill=self.node_color, outline=self.outline_color, width=2)
            self.canvas.create_text(col, row, text=str(sub_root.data), fill='black', font = ('arial', 10, 'bold'))

            self.inorder(sub_root.right, row + 50, col + sep, sep / 2) 

    def balance(self, sub_root):
        while True:
            if (self.show_steps.get() == 1):
                self.canvas.update()
                self.canvas.delete("all")
                self.inorder(self.bst.root, 30, 600, 300)
                time.sleep(0.1)

            if (sub_root == None):
                break

            numOfLeftNodes = self.bst.count_nodes(sub_root.left)
            numOfRightNodes = self.bst.count_nodes(sub_root.right)

            if (abs(numOfLeftNodes - numOfRightNodes) <= 1):
                self.balance(sub_root.left)
                self.balance(sub_root.right)
                break

            elif (numOfLeftNodes > numOfRightNodes):
                self.bst.right_rotate(sub_root)
            
            elif (numOfLeftNodes < numOfRightNodes):
                self.bst.left_rotate(sub_root)


if __name__ == '__main__':
    VisualBST()