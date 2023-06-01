#BFS
class Graph:
    def __init__(self):
        self.graph = {}

    def bfs(self, start_node):
        visited = set()
        queue = []

        queue.append(start_node)

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                neighbors = self.graph.get(node, [])
                queue.extend(neighbors)

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)


graph = Graph()

num_nodes = int(input("Enter the number of nodes: "))
for i in range(num_nodes):
    node = input(f"Enter node {i+1}: ")
    has_children = input(f"Does node {node} have any children? (y/n): ")

    if has_children.lower() == 'y':
        children = []
        while True:
            print(f"Menu for {node}:")
            print("1. Add child")
            print("2. Finish adding children")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                child = input(f"Enter child for node {node}: ")
                children.append(child)
            elif choice == 2:
                break
            else:
                print("Invalid choice! Try again.")

        graph.graph[node] = children

start_node = input("Enter the start node: ")
print("BFS Traversal:")
graph.bfs(start_node)