         graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
visited=[]
queue=[]
def bfs (visited,graph,node):
  visited.append(node)
  queue.append(node)
  while queue:
    m=queue.pop(0)

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited,graph,'A')
print(visited)
