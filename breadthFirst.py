graph = {
  '1' : ['2','3'],
  '2' : ['1', '3'],
  '3' : ['1', '2'],
}

visited = [] 
q = []  

def bfs(visited, graph, node): 
  visited.append(node)
  q.append(node)

  while q: 
    m = q.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        q.append(neighbour)

bfs(visited, graph, '1') 
