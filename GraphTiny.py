class Graph:
  adjacency_matrix = []

  def __init__(self, adjacency_matrix):
    self.adjacency_matrix = adjacency_matrix

  #Given a path to a file, loads an adjacency_matrix space separated, one line per row
  @classmethod
  def fromFile(self, filename):
    f = open(filename, "r")
    with f as lines: adjacency_matrix = [[int(i) for i in line.split()] for line in lines]
    f.close()
    return Graph(adjacency_matrix)

  #Returns a Hamiltonian Circuit, if one exists, otherwise None
  def getHamiltonian(self):
      walk = [0]
      if (len(self.adjacency_matrix) == 1) or self.tryVisiting(walk):
          return walk
      return None

  #Helper function for getHamiltonian(). Implements a backtrack approach.
  def tryVisiting(self, Walk):
    if (Walk[-1] != 0) or (len(Walk) <= 1):
      for newVertex in range(len(self.adjacency_matrix)):
          if (self.adjacency_matrix[Walk[-1]][newVertex] == 1)\
            and (newVertex not in (Walk[1:]+[Walk[-1]]))\
            and (newVertex != Walk[-1]):
              Walk.append(newVertex)
              if self.tryVisiting(Walk): return True
              else: Walk.pop()
      return False
    return (len(Walk) == len(self.adjacency_matrix)+1)
