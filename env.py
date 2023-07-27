import networkx as nx
import matplotlib.pyplot as plt
import random
import pickle

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class Graph:
    def __init__(self, N_NODES, N_EDGES):
        self.G = nx.cycle_graph(N_NODES)
        while nx.number_of_edges(self.G) < N_NODES + N_EDGES:
            n1, n2 = random.sample(range(N_NODES), 2)
            if self.G.degree[n1] < 3 and self.G.degree[n2] < 3 and not self.G.has_edge(n1, n2):
                self.G.add_edge(n1, n2)
        self.convert_to_dict()

    def convert_to_dict(self):
        graph_dict = nx.to_dict_of_lists(self.G)
        self.graph_dict = graph_dict
    
    def draw_graph(self):
        nx.draw_circular(self.G, with_labels=True)
        plt.show()
    
    def print_graph_dict(self):
        print(self.graph_dict)


if __name__ == "__main__":
    # Generate 50 graphs and save them using pickle.
    graph_envs = []
    for i in range(0, 40):
        graph_env = Graph(40, 10)
        graph_envs.append(graph_env)
    # graphs = [create_graph(40, 10) for _ in range(10)]
    with open('graphs.pkl', 'wb') as f:
        pickle.dump(graph_envs, f)

    # Load the 7th graph (index 6) from the pickle file.
    with open('graphs.pkl', 'rb') as f:
        loaded_graphs_envs = pickle.load(f)
    example = loaded_graphs_envs[6]
    example.print_graph_dict()
    example.draw_graph()
    
    
