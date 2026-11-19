class Node:
    def __init__(self, data):
        self.data = data
        self.leftNode=None
        self.rightNode=None

def largest(t):
    if t==None:
        return float('-inf')
    leftMax=largest(t.leftNode)
    rightMax=largest(t.rightNode)

    return max(t.data,leftMax,rightMax)

treesRoot=Node(2189494812934)
root=treesRoot
for i in range(1,67):
    root.leftNode=Node(1)
    root=root.leftNode
    root.rightNode=Node(1928349238192123412312321313132)

print(largest(treesRoot))