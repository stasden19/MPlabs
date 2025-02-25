class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.all_numbers = [data]

    def insert(self, data):
        self.all_numbers.append(data)
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        yield self.data
        if self.right:
            self.right.PrintTree()

    def ravel(self):
        return self.all_numbers


a = Node(123)
a.insert(456)
a.insert(12)
a.insert(23)
for i in a.PrintTree():
    print(i)
print(a.PrintTree())
print(a.ravel())
