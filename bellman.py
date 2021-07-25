class Graph:



    def __init__(self, vertices):

        self.M = vertices   # Total number of vertices in the graph

        self.graph = []     # Array of edges
        
        self.counter = 0



    # Add edges

    def add_edge(self, a, b, c):

        self.graph.append([a, b, c])



    # Print the solution

    def print_solution(self, distance):

        print("Vertex Distance from Source")

        for k in range(self.M):

            print("{0}\t\t{1}".format(k, distance[k]))



    def bellman_ford(self, src):



        distance = [float("Inf")] * self.M

        distance[src] = 0



        for _ in range(self.M - 1):

            for a, b, c in self.graph:
                if isinstance(a, str):
                    a = ord(a) % 97
                if isinstance(b, str):
                    b = ord(b) % 97
                if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c
                    print(f"{self.counter}) ({chr(a+97)}, {chr(b+97)}) | d = {distance[b]} | p = {chr(a+97)}")
                    self.counter += 1



        for a, b, c in self.graph:
            if isinstance(a, str):
                a = ord(a) % 97
            if isinstance(b, str):
                b = ord(b) % 97
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:

                print("Graph contains negative weight cycle")

                return



        self.print_solution(distance)


# amount of vertexes
g = Graph(6)
# insert edges
g.add_edge("a", "b", 1)
g.add_edge("a", "d", 5)
g.add_edge("b", "c", 1)
g.add_edge("b", "e", 5)
g.add_edge("c", "f", 5)
g.add_edge("d", "e", 2)
g.add_edge("e", "f", 2)
g.add_edge("f", "e", -3)
g.add_edge("f", "b", -7)
g.bellman_ford(0)