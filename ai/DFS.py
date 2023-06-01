#DFS
class Graph():
    def __init__(self):
        self.graph={}
    
    def dfs(self, v , visited = None):
        if visited is None:
            visited = set()

        visited.add(v)
        print(v, end=" ")

        for n in self.graph.get(v, []):
            if n not in visited:
                self.dfs(n, visited)

graph = Graph()

num_node = int(input("Enter number of node : "))
for i in range(num_node):
    node= int(input(f"Enter the {i+1} node : "))
    has_children = input(f"Does the node {node} has any children y/n ? : ")
    
    if has_children.lower() == 'y':
        children = []
        
        while True:
            print(f"Menu for node {node}")
            print("1. Add children")
            print("2. Finish adding children")
            
            choice = int(input("Enter your choice : "))
            if choice == 1:
                child = int(input(f"Enter child for node {node} : "))
                children.append(child)
            elif choice == 2:
                break
            else:
                print("Invalid choice !!")
                
        graph.graph[node] = children
        
start_node = int(input("Start node : "))
print("DFS traversal : ")
graph.dfs(start_node)
