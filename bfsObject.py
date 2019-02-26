# This relates to the image of the graph on the Firefly page
# http://ws-wgsf.fireflycloud.net/computer-science/a-level--computer-science/142-data-structures/graph-traversal/breadth-first-search


class Vertex():
    def __init__(self, name):
        self.name = name    # Each node has a letter as its contents
        self.links = []     # and we start off with an empty list of links


    def makeLink(self, otherNode):
      # This method makes two-way link between the two nodes
      
      if not otherNode in self.links:   # make sure we don't repeat a link that already exists
        self.links.append(otherNode)
        otherNode.links.append(self)    # this also affects the other node

    def __str__(self):
      # This is just a custom way of printing a node
        return "Node " + str(self.name)
    
        
def BFS(StartV, EndV):
  visited = []
  queue = [StartV]
  while len(queue)>0:
    thisNode = queue.pop(0)
    visited.append(thisNode)
    print("Visiting", thisNode)
    if thisNode == EndV:
      print("Found it!")
      return True
    for neighbour in thisNode.links:
      if neighbour not in visited and neighbour not in queue:
        queue.append(neighbour)
    
    
# make the nodes
nodeA = Vertex("A")
nodeB = Vertex("B")
nodeC = Vertex("C")
nodeD = Vertex("D")
nodeE = Vertex("E")
nodeF = Vertex("F")
nodeG = Vertex("G")
nodeH = Vertex("H")



# link them
nodeA.makeLink(nodeB)
nodeA.makeLink(nodeF)
nodeB.makeLink(nodeC)
nodeB.makeLink(nodeE)
nodeC.makeLink(nodeD)
nodeD.makeLink(nodeH)
nodeE.makeLink(nodeH)
nodeF.makeLink(nodeG)



# Starting from node1, perform a depth first search for node 7
BFS(nodeA, nodeH)
