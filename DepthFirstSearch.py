# Description: Depth First Search Implementation using a Stack
# Author: Kenyon Geetings & Sam Scholz
# Class: COSC-330 Algorithms

class Vertex:
    def __init__(self, key):
        self.key = key
        self.color = "WHITE"
        self.pi = None
        self.d = 0
        self.f = 0

class Graph:
    def __init__(self):
        self.vertices = {}
        self.adjacency_lists = {}

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)
        self.adjacency_lists[key] = []

    def add_edge(self, from_key, to_key):
        self.adjacency_lists[from_key].append(to_key)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

time = 0

def DFS(G):
    global time
    for u in G.vertices.values():
        if u.color == "WHITE":
            DFS_VISIT(G, u)

def DFS_VISIT(G, u):
    global time
    stack = Stack()
    time += 1
    u.d = time
    u.color = "GRAY"
    
    stack.push((u, G.adjacency_lists[u.key]))
    
    while not stack.is_empty():
        u, adj_list = stack.pop()
        while adj_list == []:
            u.color = "BLACK"
            time += 1
            u.f = time
            if stack.is_empty():
                return
            else:
                u, adj_list = stack.pop()
        stack.push((u, adj_list[1:]))
        v = G.vertices[adj_list[0]]
        if v.color == "WHITE":
            v.pi = u
            time += 1
            v.d = time
            v.color = "GRAY"
            stack.push((v, G.adjacency_lists[v.key]))

if __name__ == "__main__":
    G = Graph()
    G.add_vertex(1)
    G.add_vertex(2)
    G.add_vertex(3)
    G.add_vertex(4)
    G.add_vertex(5)
    G.add_vertex(6)

    G.add_edge(1,2)
    G.add_edge(2,1)
    G.add_edge(2,4)
    G.add_edge(4,2)
    G.add_edge(1,3)
    G.add_edge(3,1)
    G.add_edge(3,4)
    G.add_edge(4,3)
    G.add_edge(3,5)
    G.add_edge(5,3)
    G.add_edge(5,6)
    G.add_edge(6,5)

    DFS(G)

    for u in G.vertices.values():
        print(f"Vertex {u.key}: Discovery (d) = {u.d}, Finish (f) = {u.f}, Predecessor (pi) = {u.pi.key if u.pi else 'None'}")