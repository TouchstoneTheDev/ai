import heapq
def prim_mst(graph):
    start_node = list(graph.keys())[0]
    visited = {start_node}
    spanning_tree = []
    pq = [(w, start_node, v) for v, w in graph[start_node].items()]
    heapq.heapify(pq)
    while pq:
        w, u, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            spanning_tree.append((u, v, w))
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, v, neighbor))
    return spanning_tree
n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))
graph = {str(i): {} for i in range(1, n+1)}
for i in range(m):
    u, v, w = input("Enter edge (u, v) and weight w: ").split()
    graph[u][v] = int(w)
    graph[v][u] = int(w)
print(f"\n\nGraph: {graph}")
spanning_tree = prim_mst(graph)
print(f"\n\nMST is (u, v, w): \n{spanning_tree}\n")