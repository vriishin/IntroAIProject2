class Agent_2:
    def __init__(self):
        self.location = random.randint(0, 39)

    def move_agent(self, graph_dict, target):
    # Check if target is in agent's adjacent nodes
    if target in graph_dict[self.location]:
        self.location = target
    else:
        potential_target_locations = graph_dict[target]
        shortest_paths = [(self.dijkstra(graph_dict, self.location, potential_location), potential_location) for potential_location in potential_target_locations]
        # Filter out None paths (unreachable nodes)
        shortest_paths = [path for path in shortest_paths if path[0]]
        if not shortest_paths:
            print("No accessible paths...")
            return
        # Selects the shortest path among the potential target's next locations
        shortest_path_to_potential_location = min(shortest_paths, key=lambda x: len(x[0]))
        # Moves agent 1 step on the chosen path
        self.location = shortest_path_to_potential_location[0][1] if len(shortest_path_to_potential_location[0]) > 1 else shortest_path_to_potential_location[0][0]


    def dijkstra(self, graph_dict, start, end):
        # This method is the same as in Agent 1
        ...