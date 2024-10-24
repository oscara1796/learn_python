from collections import deque

class GraphAdjacencyList:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adj_list = {}
        
    def add_vertex(self, vertex):
        # Add a vertex to the adjacency list if it's not already present
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
        
    def add_edge(self, src, dest):
        # Since it's a directed graph, add an edge from src to dest
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adj_list[src].append(dest)

    def bfs(self, start_vertex):
        visited = set()          # Set to keep track of visited nodes
        queue = deque()          # Queue for BFS traversal
        traversal_order = []     # List to record the order of traversal

        # Start by visiting the start_vertex
        visited.add(start_vertex)
        queue.append(start_vertex)
        print(f"Starting BFS from vertex {start_vertex}\n")

        while queue:
            print(f"Queue: {list(queue)}")  # Debug: show current queue
            vertex = queue.popleft()        # Dequeue a vertex from queue
            print(f"Visiting vertex {vertex}")
            traversal_order.append(vertex)  # Add it to the traversal order

            # Iterate over the neighbors of the dequeued vertex
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)    # Mark neighbor as visited
                    queue.append(neighbor)   # Enqueue the neighbor
                    print(f"Discovered vertex {neighbor}, adding to queue")
            print(f"Visited nodes: {visited}\n")  # Debug: show visited nodes
        print(f"BFS traversal order: {traversal_order}\n")
        return traversal_order


if __name__ == "__main__":

    """
    Graph Representation (Directed Graph):

        [0] ------> [1]
         ^           |
         |           v
         +<------- [2] -----> [3]
                          ^     |
                          |_____|
                           (self-loop at [3])
    """

    graph = GraphAdjacencyList()
    # Adding edges as per the graph representation
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)  # Self-loop at node 3

    print("Adjacency List of the Graph:")
    for vertex in graph.adj_list:
        print(f"{vertex}: {graph.adj_list[vertex]}")
    print("\n")

    # Perform BFS starting from vertex 2
    print("BFS Traversal starting from vertex 2:")
    graph.bfs(2)

    # Perform BFS starting from vertex 1
    print("BFS Traversal starting from vertex 1:")
    graph.bfs(1)
