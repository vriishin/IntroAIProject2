import networkx as nx
import matplotlib.pyplot as plt
import random
import pickle

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class CircularLinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            while len(nodes) != 0:
                node.next = Node(value=nodes.pop(0))
                node = node.next
            node.next = self.head

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            if node == self.head:
                break

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.val == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

def create_graph(N_NODES, N_EDGES):
    G = nx.cycle_graph(N_NODES)
    while nx.number_of_edges(G) < N_NODES + N_EDGES:
        n1, n2 = random.sample(range(N_NODES), 2)
        if G.degree[n1] < 3 and G.degree[n2] < 3 and not G.has_edge(n1, n2):
            G.add_edge(n1, n2)
    return G

def convert_to_dict(G):
    graph_dict = nx.to_dict_of_lists(G)
    return graph_dict

def build_linked_list(graph_dict):
    circular_linked_lists = {}
    for node, edges in graph_dict.items():
        circular_linked_lists[node] = CircularLinkedList(edges)
    return circular_linked_lists

def draw_graph(G):
    nx.draw_circular(G, with_labels=True)
    plt.show()

def print_graph_dict(graph_dict):
    print("Graph as a dictionary:")
    for node, edges in graph_dict.items():
        print(f"Node {node} connected to: {edges}")

def print_linked_list(circular_linked_lists):
    print("\nGraph as a circular linked list:")
    for node, linked_list in circular_linked_lists.items():
        print(f"Node {node} connected to: ", end="")
        for connected_node in linked_list:
            print(connected_node.val, end=" ")
        print()

if __name__ == "__main__":
    # Generate 50 graphs and save them using pickle.
    graphs = [create_graph(40, 10) for _ in range(50)]
    with open('graphs.pkl', 'wb') as f:
        pickle.dump(graphs, f)

    # Load the 7th graph (index 6) from the pickle file.
    with open('graphs.pkl', 'rb') as f:
        loaded_graphs = pickle.load(f)
    G = loaded_graphs[6]
    
    # Use the loaded graph
    graph_dict = convert_to_dict(G)
    circular_linked_lists = build_linked_list(graph_dict)
    draw_graph(G)
