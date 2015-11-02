from collections import defaultdict

graph1 = defaultdict(set)

def add_arc(graph, node1, node2):
    '''graph is default dict of lists
    node1 and node2 are strings'''

    #add new connection
    graph[node1].add(node2)

    #add node2 if it doesn't exist
    graph[node2]

def dfs(graph, node1):
    '''uses depth first search to  try and find 
    a path all nodes connected to node1. 
    Returns the first path found or None if no
    paths exist'''

    visited = set()
    stack = [node1]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

add_arc(graph1, 'A', 'B')
add_arc(graph1, 'A', 'C')
add_arc(graph1, 'C', 'D')
add_arc(graph1, 'B', 'D')
add_arc(graph1, 'B', 'E')
add_arc(graph1, 'E', 'F')
add_arc(graph1, 'F', 'D')

print dfs(graph1, 'A')
print list(dfs_paths(graph1, 'A', 'D'))
print list(bfs_paths(graph1, 'A', 'D'))
print shortest_path(graph1, 'A', 'D')
