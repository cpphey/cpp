class Node:
    data = None
    leftptr = None
    rightptr = None

    def __init__(self,data=None):
        self.data = data

class Tree:
    root = None

    def __init__(self, root=None):
        self.root = root


def main():

    #Put some data
    r = Node(30)
    n1 = Node(20)
    n2 = Node(10)
    r.leftptr = n1
    n1.leftptr = n2

    #Form a tree
    t = Tree(r)

    #Balance the tree

main()

