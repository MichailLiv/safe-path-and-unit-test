import math
import numpy as np
class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


# Methods have been added to associate node numbers with names
# Specifically: Graph.set_node_names
# and the methods ending in "_names" which will print names instead
# of node numbers

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node, To Node)"""
        return [(e.value, e.node_from.value, e.node_to.value)
                for e in self.edges]

    def get_edge_list_names(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node Name, To Node Name)"""
        return [(edge.value,
                 self.node_names[edge.node_from.value],
                 self.node_names[edge.node_to.value])
                for edge in self.edges]

    def get_adjacency_list(self):
        """Return a list of lists.
        The indecies of the outer list represent "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_index = self.find_max_index()
        adjacency_list = [[] for _ in range(max_index)]
        for edg in self.edges:
            from_value, to_value = edg.node_from.value, edg.node_to.value
            adjacency_list[from_value].append((to_value, edg.value))
        return [a or None for a in adjacency_list]  # replace []'s with None

    def get_adjacency_list_names(self):
        """Each section in the list will store a list
        of tuples that looks like this:
        (To Node Name, Edge Value).
        Node names should come from the names set
        with set_node_names."""
        adjacency_list = self.get_adjacency_list()

        def convert_to_names(pair, graph=self):
            node_number, value = pair
            return (graph.node_names[node_number], value)

        def map_conversion(adjacency_list_for_node):
            if adjacency_list_for_node is None:
                return None
            return map(convert_to_names, adjacency_list_for_node)

        return [map_conversion(adjacency_list_for_node)
                for adjacency_list_for_node in adjacency_list]

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_index = self.find_max_index()
        adjacency_matrix = [[0] * (max_index) for _ in range(max_index)]
        for edg in self.edges:
            from_index, to_index = edg.node_from.value, edg.node_to.value
            adjacency_matrix[from_index][to_index] = edg.value
        return adjacency_matrix

    def find_max_index(self):
        """Return the highest found node number
        Or the length of the node names if set with set_node_names()."""
        if len(self.node_names) > 0:
            return len(self.node_names)
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index

    def find_node(self, node_number):
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False


    def dijkstar(self, start_node_num):
        """
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes for the safest path.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: Safest path and maximum value of risk within safest path"""
        path_Weight = {node: math.inf for node in self.nodes}
        previous_node = {node: None for node in self.nodes}

        node = self.find_node(start_node_num)
        path_Weight[node] = 0
        self._clear_visited()
        #ret_list = []
        nodes = self.nodes.copy()
        queue = [node]
        node.visited = True
        path=[node]
        def enqueue(n, q=queue):
            n.visited = True
            nodes.remove(n)
            #print(n.value)
            #print([path_Weight[node] for node in nodes])
            # min( nodes , key=lambda node:path_Weight[node])
            if nodes:
                current_node = min( nodes, key=lambda i: path_Weight[i] )
                path.append(current_node)
                q.append(current_node)

        def unvisited_outgoing_edge(n, e):
            return ((e.node_from.value == n.value) and
                    (not e.node_to.visited))

        # import pdb;pdb.set_trace()
        while queue:
            node = queue.pop(0)
            #ret_list.append(node.value)
            #min = math.inf

            for e in node.edges:
                if unvisited_outgoing_edge(node, e):
                    route = e.value# path_Weight[node] + e.value
                    if route <  path_Weight[e.node_to]:
                        path_Weight[e.node_to] = route
                        previous_node[e.node_to] = node

            enqueue(node)
        Zearth = self.nodes[-1]
        end=Zearth
        ret_list=[end]
        while previous_node[end] is not None:
            ret_list.insert(0,previous_node[end])
            end=previous_node[end]
        return ret_list,max([path_Weight[i] for i in path_Weight])

    def dijkstar_output(self, start_node_num):
        """Return the results of dijkstar with numbers converted to names."""
        path, max_distance_=self.dijkstar(start_node_num)
        return [self.node_names[p.value] for p in path], float("{0:.2f}".format(max_distance_))
