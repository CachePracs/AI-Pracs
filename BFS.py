graph = {
  'A' : ['B','S'],'B':['A'],
  'C' : ['D', 'E','F','S'],'D':['C'],
  'E' : ['C','H'],'F':['C','G'],
  'G' : ['F','H','S'],'H':['E','G'],
  'S' : ['A','G','C']
  }

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    S = queue.pop(0) 
    print (S, end = " ") 

    for neighbour in graph[S]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print(" Breadth-First Search:")
bfs(visited, graph, 'A') 
