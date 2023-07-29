import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random
import pickle
from abc import ABC, abstractmethod

class Agent(ABC):

    def djikstra(self, graph_dict, start, end):
        # djikstra's algorithm.
        heap = [(0, start)]
        predecessors = {start: None}
        distances = {start: 0}

        while heap:
            (distance, current) = heapq.heappop(heap)
            if current == end:
                return self.path(predecessors, end)
            for neighbor in graph_dict[current]:
                old_distance = distances.get(neighbor, float('inf'))
                new_distance = distances[current] + 1
                if new_distance < old_distance:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current
                    heapq.heappush(heap, (new_distance, neighbor))

    @staticmethod
    def path(predecessors, end):
        cursor = end
        path = []
        while cursor is not None:
            path.append(cursor)
            cursor = predecessors[cursor]
        return list(reversed(path))
    

    def update_probabilistic_kb(self, examined_node, graph_dict, target):
        target_found = True if examined_node == target else False
        if target_found:
            self.probabilistic_kb[examined_node] = 1
        else:
            self.probabilistic_kb[examined_node] = 0


        for node in graph_dict:
            if self.num_neighbors[node] > 0:
                k = self.num_neighbors[node]
                p_move_to_neighbor = 1 / k
                for neighbor in graph_dict[node]:
                    self.probabilistic_kb[neighbor] += p_move_to_neighbor
                self.probabilistic_kb[node] -= 1

        # Normalize the probabilities to maintain the sum equal to 1.
        total_probability = sum(self.probabilistic_kb.values())
        for node in self.probabilistic_kb:
            self.probabilistic_kb[node] /= total_probability
    

    

class Agent_0(Agent):
    def __init__(self):
        self.location = random.randint(0, 39)
    
    def move_agent(self, graph_dict, target):
        # print(f"AGENT 0 LOC: {self.location},\n TARGET LOCATION: {target}")
        return self.location
        
    

class Agent_1(Agent):
    def __init__(self):
        self.location = random.randint(0, 39)
        # self.location = 0
 
    def move_agent(self, graph_dict, target):
        shortest_path = self.djikstra(graph_dict, self.location, target)
        if not shortest_path:
            print("You have made a grave error...")
            return

        self.location = shortest_path[1] if len(shortest_path) > 1 else shortest_path[0]
        # print(f"AGENT 1 LOC: {self.location},\n TARGET LOCATION: {target}")

class Agent_2(Agent):
    def __init__(self):
        self.location = random.randint(0, 39)
        # self.location = 0

    def move_agent(self, graph_dict, target):
        if target in graph_dict[self.location]:
            return self.location
        potential_target_locations = graph_dict[target]
        potential_target_locations.append(target)
        all_paths = []
        for i in range(0, len(potential_target_locations)):
            path = self.djikstra(graph_dict, self.location, potential_target_locations[i])
            if path is not None:
                all_paths.append(path)

        sorted_paths = sorted(all_paths, key=len)
        if sorted_paths is None:
            print("You have made a grave error...")
            return
        selected_path = sorted_paths[0]
        self.location = selected_path[1] if len(selected_path) > 1 else selected_path[0]
        # print(f"AGENT 2 LOC: {self.location},\n TARGET LOCATION: {target}")
        return

class Agent_3(Agent):
    def __init__(self):
        self.location = random.randint(0, 39)

    def move_agent(self, graph_dict, target):
        # print(f"AGENT 3 LOC: {self.location},\n TARGET LOCATION: {target}")
        return self.location
    
class Agent_4(Agent):
    def __init__(self, graph_dict):
        total_nodes = 40
        self.location = random.randint(0, 39)
        # self.location = 0   
        self.probabilistic_kb = {node: 1/total_nodes for node in range(total_nodes)}
        self.num_neighbors = {node: len(neighbors) for node, neighbors in graph_dict.items()}

    def move_agent(self, graph_dict, target):

        highest_prob_nodes = [node for node, prob in self.probabilistic_kb.items() if prob == max(self.probabilistic_kb.values())]

        next_location = random.choice(highest_prob_nodes)
        self.update_probabilistic_kb(next_location, graph_dict, target)
        self.location = next_location
        # print(f"AGENT 4 LOC: {self.location},\n TARGET LOCATION: {target}")
        #print("Knowledge Base:")
        #for node, prob in self.probabilistic_kb.items():
            #print(f"Node {node}: {prob}")

class Agent_5(Agent):
    def __init__(self, graph_dict):
        total_nodes = 40
        self.location = random.randint(0, 39)
        # self.location = 0   
        self.probabilistic_kb = {node: 1/total_nodes for node in range(total_nodes)}
        self.num_neighbors = {node: len(neighbors) for node, neighbors in graph_dict.items()}
    
    def modified_probabilistic_kb(self, examined_node, graph_dict, target):
        target_found = True if examined_node == target else False
        if target_found:
            self.probabilistic_kb[examined_node] = 1
        else:
            self.probabilistic_kb[examined_node] = 0

        for node in graph_dict:
            if self.num_neighbors[node] > 0:
                k = self.num_neighbors[node]
                p_move_to_neighbor = 1 / k
                for neighbor in graph_dict[node]:
                    self.probabilistic_kb[neighbor] += p_move_to_neighbor
                    if self.num_neighbors[neighbor] > 0:
                        k_neighbor = self.num_neighbors[neighbor]
                        p_move_to_next_neighbor = p_move_to_neighbor / k_neighbor
                        for neighbor_neighbor in graph_dict[neighbor]:
                            self.probabilistic_kb[neighbor_neighbor] += p_move_to_next_neighbor
                    self.probabilistic_kb[node] -= 1

        total_probability = sum(self.probabilistic_kb.values())
        for node in self.probabilistic_kb:
            self.probabilistic_kb[node] /= total_probability

    def move_agent(self, graph_dict, target):
        pass
        highest_prob_nodes = [node for node, prob in self.probabilistic_kb.items() if prob == max(self.probabilistic_kb.values())]
        next_location = random.choice(highest_prob_nodes)
        self.modified_probabilistic_kb(next_location, graph_dict, target)
        self.location = next_location
        # print(f"AGENT 5 LOC: {self.location},\n TARGET LOCATION: {target}")
        # print("Knowledge Base:")
        # for node, prob in self.probabilistic_kb.items():
        #     print(f"Node {node}: {prob}")


class Agent_6(Agent):
    def __init__(self, graph_dict):
        self.location = random.randint(0, 39)
        total_nodes = 40
        # self.location = 0        
        self.probabilistic_kb = {node: 1/total_nodes for node in range(total_nodes)}
        self.num_neighbors = {node: len(neighbors) for node, neighbors in graph_dict.items()}
    def move_agent(self, graph_dict, target):

        highest_prob_nodes = [node for node, prob in self.probabilistic_kb.items() if prob == max(self.probabilistic_kb.values())]

        next_location = random.choice(highest_prob_nodes)
        self.update_probabilistic_kb(next_location, graph_dict, target)
        shortest_path = self.djikstra(graph_dict, self.location, next_location)
        if not shortest_path:
            print("You have made a grave error...")
            return

        self.location = shortest_path[1] if len(shortest_path) > 1 else shortest_path[0]
        # print(f"AGENT 6 LOC: {self.location},\n TARGET LOCATION: {target}")
        #print("Knowledge Base:")
        #for node, prob in self.probabilistic_kb.items():
            #print(f"Node {node}: {prob}")

class Agent_7(Agent):
    
    def __init__(self, graph_dict):
        total_nodes = 40
        self.location = random.randint(0, 39)
        # self.location = 0
        self.probabilistic_kb = {node: 1/total_nodes for node in range(total_nodes)}
        self.num_neighbors = {node: len(neighbors) for node, neighbors in graph_dict.items()}

    def move_agent(self, graph_dict, target):
        highest_prob_nodes = [node for node, prob in self.probabilistic_kb.items() if prob == max(self.probabilistic_kb.values())]
        highest_prob_sorted = sorted(highest_prob_nodes, key=lambda x: len(self.djikstra(graph_dict, self.location, x)))
        next_location = highest_prob_sorted[0] if highest_prob_sorted is not None and len(highest_prob_sorted) > 0 else self.location
        self.update_probabilistic_kb(next_location, graph_dict, target)
        self.location = next_location
        
        shortest_path = self.djikstra(graph_dict, self.location, next_location)
        if not shortest_path:
            print("You have made a grave error...")
            return

        # print(f"AGENT 7 LOC: {self.location},\n TARGET LOCATION: {target}")
        # print("Knowledge Base:")
        # for node, prob in self.probabilistic_kb.items():
        #     print(f"Node {node}: {prob}")

class Graph:

    def __init__(self, N_NODES, N_EDGES):
        self.G = nx.cycle_graph(N_NODES)
        while nx.number_of_edges(self.G) < N_NODES + N_EDGES:
            n1, n2 = random.sample(range(N_NODES), 2)
            if self.G.degree[n1] < 3 and self.G.degree[n2] < 3 and not self.G.has_edge(n1, n2):
                self.G.add_edge(n1, n2)
        self.time_step = 0
        self.convert_to_dict()
        self.set_target_location()
        self.initialize_agents()
    
    def run_agents(self):
        while not all (not element for element in self.agents_active):
            self.turn()
            self.move_target()
            # print(self.time_step)
        # print(self.agent_performance)

    def turn(self):
        self.time_step += 1
        for i in range(0, 8):
            if self.agents_active[i]:
                self.agents[i].move_agent(self.graph_dict, self.target)
                self.agent_locations[i] = self.agents[i].location
                self.is_target_captured(self.agent_locations[i], i)
        #self.draw_graph() # draw the graph at each time step
        #plt.pause(0.1) # add a pause so you can see the graphs

    def is_target_captured(self, agent_location, agent_index):
        if(agent_location == self.target):
            self.agent_performance[agent_index] = self.time_step
            self.agents_active[agent_index] = False
            # print(f"Agent {agent_index} has captured the target")
            # print(self.agent_performance)

    def initialize_agents(self):        
        self.agents = [Agent_0(), Agent_1(), Agent_2(), Agent_3(), Agent_4(self.graph_dict), Agent_5(self.graph_dict), Agent_6(self.graph_dict), Agent_7(self.graph_dict)]
        self.agent_locations = [self.agents[i].location for i in range(0, 8)]
        self.agents_active = [True, True, True, True, True, True, True, True]
        self.agents_colors = ["magenta","green","pink","yellow","gray","white","cyan","purple"]
        self.agent_performance = [-1 for i in range(0, 8)]
        for i in range(0, 8):
            if self.agents_active[i]:
                self.is_target_captured(self.agent_locations[i], i)

    def set_target_location(self):
        location = random.randint(0, 39)
        self.target = location

    def convert_to_dict(self):   
        graph_dict = nx.to_dict_of_lists(self.G)
        self.graph_dict = graph_dict
    
    def draw_graph(self):
        colors = ["blue" for node in self.G.nodes]
        for i in range(len(self.agents)):
            if self.agents_active[i]:
                colors[self.agent_locations[i]] = self.agents_colors[i]
        colors[self.target] = "red"
        nx.draw_circular(self.G, node_color=colors, with_labels=True)
        plt.show()
    
    def print_graph_dict(self):
        print(self.graph_dict)
        print(f"TARGET LOCATION: {self.target}")
    
    def move_target(self):
        connections = self.graph_dict[self.target]
        random_choice = random.randint(0, len(connections)-1)
        self.target = connections[random_choice]
    def get_performance(self):
        return self.agent_performance
    
def calculate_averages(performance_records):
    transposed_records = list(map(list, zip(*performance_records)))
    
    averages = []
    for i, record in enumerate(transposed_records):
        avg = sum(record) / len(record)
        print(f"Agent {i} Performance: {avg}")
        averages.append(avg)
    return averages

if __name__ == "__main__":

    with open('graphs.pkl', 'rb') as f:
        graph_envs = pickle.load(f)
    # For each graph, initialize the agents and run them
    performance_records = []
    for i, graph_env in enumerate(graph_envs):
        graph_env.initialize_agents()
        graph_env.run_agents()
        performance_records.append(graph_env.get_performance())
    
    perf_avgs = calculate_averages(performance_records)

    with open('performance.pkl', 'wb') as f:
        pickle.dump(perf_avgs, f)
   