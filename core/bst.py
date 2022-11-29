class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

class BST:
    def __init__(self):
        self.root = None

    def create_node(self, d):
        return Node(d)

    def insert(self, sub_root, d):
        if sub_root == None:
            return self.create_node(d)
        
        elif d < sub_root.data:
            sub_root.left = self.insert(sub_root.left, d)

        else:
            sub_root.right = self.insert(sub_root.right, d)

        return sub_root


    def inorder(self, sub_root): 
        if sub_root: 
            self.inorder(sub_root.left) 
            print(sub_root.data, end=" ") 
            self.inorder(sub_root.right) 

    def count_nodes(self, sub_root):
        count = 1
        if sub_root == None:
            return 0

        if sub_root.left != None:
            count += self.count_nodes(sub_root.left)

        if sub_root.right != None:
            count += self.count_nodes(sub_root.right)

        return count

    def get_minval(self, sub_root):
        current = sub_root

        while (current and current.left != None):
            current = current.left

        return current

    def max_val(self, sub_root):
        current = sub_root

        while (current and current.right != None):
            current = current.right

        return current

    def prev_inorder(self, sub_root):
        current = sub_root
        current = current.left

        while (current and current.right != None):
            current = current.right

        return current

    def next_inorder(self, sub_root):
        current = sub_root
        current = current.right

        while (current and current.left != None):
            current = current.left

        return current

    def delete_entry(self, sub_root, d):
        if (sub_root == None):
            return None
        
        elif (d > sub_root.data): 
            sub_root.right = self.delete_entry(sub_root.right, d)
        
        elif (d < sub_root.data): 
            sub_root.left = self.delete_entry(sub_root.left, d)
        
        else: 
            if (sub_root.left == None and sub_root.right == None):
                sub_root = None
                return sub_root
            
            elif (sub_root.left == None): 
                temp = sub_root.right
                sub_root = None
                return temp
            
            elif (sub_root.right == None): 
                temp = sub_root.left
                sub_root = None
                return temp
            
            else: 
                temp = self.get_minval(sub_root.right)
                sub_root.data = temp.data
                sub_root.right = self.delete_entry(sub_root.right, temp.data)

        return sub_root

    def left_rotate(self, sub_root):
        prev_node = self.prev_inorder(sub_root)
        next_node = self.next_inorder(sub_root)

        if (next_node == None): 
            print("cant left rotate")
            return None

        if (prev_node == None):
            newNode = self.create_node(sub_root.data)
            sub_root.left = newNode
            nextData = next_node.data

            self.root = self.delete_entry(self.root, next_node.data)
            sub_root.data = nextData
        
        else: 
            newNode = self.create_node(sub_root.data)
            prev_node.right = newNode
            nextData = next_node.data

            self.root = self.delete_entry(self.root, next_node.data)
            sub_root.data = nextData

    def right_rotate(self, sub_root):
        prev_node = self.prev_inorder(sub_root)
        next_node = self.next_inorder(sub_root)

        if (prev_node == None): 
            print("cant right rotate")
            return None

        if (next_node == None):
            newNode = self.create_node(sub_root.data)
            sub_root.right = newNode
            prevData = prev_node.data

            self.root = self.delete_entry(self.root, prev_node.data)
            sub_root.data = prevData
        
        else: 
            newNode = self.create_node(sub_root.data)
            next_node.left = newNode
            prevData = prev_node.data

            self.root = self.delete_entry(self.root, prev_node.data)
            sub_root.data = prevData

    def balance(self, sub_root):
        while True:
            if (sub_root == None):
                break

            num_left_nodes = self.count_nodes(sub_root.left)
            num_right_nodes = self.count_nodes(sub_root.right)

            if (abs(num_left_nodes - num_right_nodes) <= 1):
                self.balance(sub_root.left)
                self.balance(sub_root.right)
                break

            elif (num_left_nodes > num_right_nodes):
                self.right_rotate(sub_root)
            
            elif (num_left_nodes < num_right_nodes):
                self.left_rotate(sub_root)



