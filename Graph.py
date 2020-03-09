class Graph:

  adjacency_matrix = []
  totalV = 0

  def __init__(self, adjacency_matrix):
    self.adjacency_matrix = adjacency_matrix
    self.totalV = len(self.adjacency_matrix)

  @classmethod
  def fromFile(self, filename):
    f = open(filename, "r")
    with f as lines:
      adjacency_matrix = [[int(i) for i in line.split()] for line in lines]
    f.close()
    return Graph(adjacency_matrix)
    
  def isDistanceOne(self, vertex, newVertex):
    return self.adjacency_matrix[vertex][newVertex] == 1

  def getHamiltonian(self):
    walk = []
    walk.append(0)
    if self.tryVisiting(walk) or (self.totalV ==1):
        return walk
    return None

  def tryVisiting(self, Hamiltonian):
    vertex = Hamiltonian[-1]
    hamLen = len(Hamiltonian)
    if (vertex == 0) and (hamLen > 1):
        return (hamLen == self.totalV+1)
    else:
        for newVertex in range(0,self.totalV):
            distance = self.isDistanceOne(vertex, newVertex)
            isRepeat = newVertex in (Hamiltonian[1:]+[vertex])
            isPrevious = (newVertex == vertex)
            if (distance == 1) and (isRepeat == False) and (isPrevious == False):
                Hamiltonian.append(newVertex)
                if self.tryVisiting(Hamiltonian):
                    return True
                else:
                    Hamiltonian.pop()
        return False

test = Graph([[0, 1, 1],[1,0,1],[1,1,0]])
print(test.getHamiltonian())

test2 = Graph([[0,1,0,1],[1,0,1,1],[0,1,0,1],[1,1,1,0]])
print(test2.getHamiltonian())


test3 = Graph.fromFile("test")
print(test3.getHamiltonian())

