    def getHamiltonian(self):
        if self.isConnected():
            walk = []
            walk.append(0)
            if self.tryVisiting(0, walk) or (self.totalV == 1):
                return walk
        return None

    def tryVisiting(self, vertex, Hamiltonian):
        hamSplit = str(Hamiltonian).split()
        hamLen = len(hamSplit)
        if (vertex == 0) and (hamLen > 1):
            return (hamLen == self.totalV+1)
        else:
            for newVertex in range(0,self.totalV):
                distance = self.getEdgeCount(vertex, newVertex)
                isRepeat = str(newVertex) in (hamSplit[1:]+[vertex])
                isPrevious = (newVertex == vertex)
                if (distance == 1) and (isRepeat == False) and (isPrevious == False):
                    Hamiltonian.addVertex(newVertex)
                    if self.tryVisiting(newVertex, Hamiltonian):
                        return True
                    else:
                        Hamiltonian.removeLastVertex()
            return False
