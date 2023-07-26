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


if __name__ == "__main__":
    circlist = CircularLinkedList()
    for i in range(1, 41):
        circlist.add_node(f"Agent-{i}", f"Target-{i}", f"Pos-{i}")
    circlist.print_list()
