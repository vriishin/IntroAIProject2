import random


class Node:
    def __init__(self, agent, target, pos):
        self.agent = agent
        self.target = target
        self.prev = None
        self.next = None
        self.pos = pos


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, agent, target, pos):
        new_node = Node(agent, target, pos)
        if not self.head:
            self.head = new_node
            self.head.prev = self.head
            self.head.next = self.head
        else:
            last_node = self.head.prev
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node

    def print_list(self):
        if not self.head:
            print("Circular linked list is empty.")
            return

        current = self.head
        print("Circular linked list:")
        while True:
            print(f"Agent: {current.agent}, Target: {current.target}, Position: {current.pos}")
            current = current.next
            if current == self.head:
                break
    
    def random_edges(self, num_edges):
        if num_edges <= 0:
            return

        num_nodes = len(self.node_list)
        if num_nodes <= 1:
            return

        edges_added = 0
        while edges_added < num_edges:
            node1 = random.choice(self.node_list)
            node2 = random.choice(self.node_list)


            if node1 != node2 and not self.are_connected(node1, node2):
                node1.next = node2
                node2.prev = node1
                edges_added += 1

    def if_connected(self, n1, n2):
        cur = n1
        while True:
            if cur.next == n2:
                return True
            cur = cur.next
            if cur == n1:
                break
        return False


if __name__ == "__main__":
    circlist = CircularLinkedList()
    for i in range(1, 41):
        circlist.add_node(f"Agent-{i}", f"Target-{i}", f"Pos-{i}")
    circlist.print_list()
