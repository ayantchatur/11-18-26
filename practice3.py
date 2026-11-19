class Node:
    def __init__(self, data):
        self.data = data
        self.leftNode=None
        self.rightNode=None

def search(t,searchingFor):
    if t==None:
        return(False)

    if t.data==searchingFor:
        return(True)
    
    return search(t.leftNode,searchingFor) or search(t.rightNode,searchingFor)

treesRoot=Node(2189494812934)
root=treesRoot
for i in range(1,67):
    root.leftNode=Node(1)
    root=root.leftNode
    root.rightNode=Node(1928349238192123412312321313132)

print(search(treesRoot,1928349238192123412312321313132))