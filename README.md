# Backtracking-Hamiltonian-Circuit
Backtracking Hamiltonian Circuit

## About
This was my first attemt at finding a Hamiltonian Circuit given an adjacency matrix.
Please note doubly connected points are not supported. 
Additionally, I haven't tested this code with directed graphs.

## Adjacency Matrix from List of Lists
```
test = Graph([[0, 1, 1],[1,0,1],[1,1,0]])
print(test.getHamiltonian())
```

## Import Adjacency Matrix from File

Given a path to a file, loads an adjacency_matrix space separated, one line per row 
```
test = Graph.fromFile("test")
print(test3.getHamiltonian())
```

