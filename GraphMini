class Graph:
  adjacency_matrix = []
  totalV = 0
  
  def __init__(self, adjacency_matrix):
    self.adjacency_matrix = adjacency_matrix
    self.totalV = len(self.adjacency_matrix)

  #Given a path to a file, loads an adjacency_matrix space separated, one line per row
  @classmethod
  def fromFile(self, filename):
    f = open(filename, "r")
    with f as lines:
      adjacency_matrix = [[int(i) for i in line.split()] for line in lines]
    f.close()
    return Graph(adjacency_matrix)

  #Determines if vertexA is joined to vertexB
  def isDistanceOne(self, vertexA, vertexB):
    return self.adjacency_matrix[vertexA][vertexB] == 1

  #Returns a Hamiltonian Circuit, if one exists, otherwise None
  def getHamiltonian(self):
      walk = [0]
      if (self.totalV == 1) or self.tryVisiting(walk):
          return walk
      return None

  #Helper function for getHamiltonian(). Implements a backtrack approach.
  def tryVisiting(self, Hamiltonian):
    hamLen = len(Hamiltonian)
    if (Hamiltonian[-1] == 0) and (hamLen > 1):
        return (hamLen == self.totalV+1)
    else:
        for newVertex in range(self.totalV):
            isJoined = self.isDistanceOne(Hamiltonian[-1], newVertex)
            isRepeat = newVertex in (Hamiltonian[1:]+[Hamiltonian[-1]])
            isPrevious = (newVertex == Hamiltonian[-1])
            if (isJoined) and (isRepeat == False) and (isPrevious == False):
                Hamiltonian.append(newVertex)
                if self.tryVisiting(Hamiltonian):
                    return True
                else:
                    Hamiltonian.pop()
        return False
