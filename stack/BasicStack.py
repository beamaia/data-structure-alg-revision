from Node import Node

class BasicStack:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def push(self, value) -> None:
        node = Node(value)
        
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        
        self.size += 1

    def peek(self) -> None:
        if not self.head:
            return

        aux = self.head
        for i in range(self.size):
            print(f"Item: {aux.val}")

            aux = aux.next

if __name__ == "__main__":
    circular_list = BasicStack()

    circular_list.push(1)
    circular_list.push(2)
    circular_list.push(3)

    circular_list.peek()

        