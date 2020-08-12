from util import Queue, Stack


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('nonexistent vertex/node')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    # given sets of [(parent, child)] relationships on a graph & an input node
    # find the node that is the furthest away from the input node and output it
    # if there are more than 1 ancestors tied return the lowest number
    # if the input doesn't have a parent node return -1
    g = Graph()

    for parent, child in ancestors:
        g.add_vertex(child)
        g.add_vertex(parent)
        g.add_edge(child, parent)

    q = Queue()
    q.enqueue([starting_node])
    max_path_length = 1
    aged_one = -1

    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]

        if(len(path) >= max_path_length and current_node < aged_one) or (len(path) > max_path_length):
            aged_one = current_node
            max_path_length = len(path)

        for neighbor in g.vertices[current_node]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return aged_one


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 2))
