import math
import networkx as nx
import random
import matplotlib.pyplot as plt
from regular import _hierarchy_pos,hierarchy_pos
class Node:
    def __init__(self):
        self.info=0
        self.leftChild=None
        self.rightChild=None
    
def getHeight(node):
    if node==None:
        return 0
    else:
        return 1+ math.max(getHeight(node.leftChild),getHeight(node.rightChild))      
def kdtree(pointList, depth=0):
    if not pointList:
        return

    k = len(pointList[0]) 
    axis = depth % k
    pointList.sort(key=lambda x:x[axis])
    median = len(pointList)//2 
    node = Node()
    node.info = pointList[median]
    node.leftChild = kdtree(pointList[0:median], depth+1)
    node.rightChild = kdtree(pointList[median+1:], depth+1)
    return node

G=nx.DiGraph()
def recorrer(node):
    if node==None:
        return
    if node.leftChild!=None:
        G.add_node(node.leftChild.info)
        G.add_edge(node.info,node.leftChild.info)
    if node.rightChild!=None:
        G.add_node(node.rightChild.info)
        G.add_edge(node.info,node.rightChild.info)
    recorrer(node.leftChild)
    recorrer(node.rightChild)

pointList = [(2,3),(5,4),(9,1),(4,7),(8,1),(4,2),(7,2),(10,1)]
tree = kdtree(pointList)
recorrer(tree)
edge_labels = nx.get_edge_attributes(G, 'weight')
pos = hierarchy_pos(G,tree.info)    
nx.draw(G, pos=pos, node_size=1400,with_labels=True)
plt.show()





