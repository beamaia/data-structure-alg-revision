class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.val = value

class BasicLinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_node(self, node:Node) -> None:
        """
        Inserts node into the beginning of the list
        """
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def show_list(self) -> None:
        aux = self.head

        while aux:
            print(f"{aux.val}")
            aux = aux.next

if __name__ == "__main__":
    node1 = Node(10)
    node2 = Node(2)
    node3 = Node(30)

    linked_list = BasicLinkedList()

    linked_list.add_node(node1)
    linked_list.add_node(node2)
    linked_list.add_node(node3)

    linked_list.show_list()