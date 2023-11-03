graph = {
  '1' : ['2','3','4'],
  '2' : ['4', '6'],
  '3' : ['4', '6'],
  '4' : ['5'],
  '5' : ['8', '9'],
  '6' : ['7'],
  '7' : ['9'],
  '8' : [],
  '9' : []
}

visited = set() 
def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, '1')