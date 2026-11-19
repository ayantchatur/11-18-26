class Node:
    def __init__(self, data):
        self.data = data
        self.leftNode=None
        self.rightNode=None


def count(t=None):
    if t==None:
        return(0)

    left=count(t.leftNode)
    right=count(t.rightNode)

    return(left+right+1)

treesRoot=Node(6)
root=treesRoot
for i in range(1,67):
    root.leftNode=Node(1)
    root=root.leftNode

print(f"Counted {count(treesRoot)} nodes")