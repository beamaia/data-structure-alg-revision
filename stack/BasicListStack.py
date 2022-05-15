from Node import Node

class BasicListStack:
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

    def pop(self) -> object:
        if not self.size:
            return None

        aux = self.head
        
        self.head = self.head.next
        self.size -= 1

        return aux

    def peek(self) -> None:
        if not self.head:
            return

        aux = self.head
        for i in range(self.size):
            print(f"Item: {aux.val}")

            aux = aux.next

if __name__ == "__main__":
    stack = BasicListStack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.peek()
    print('Last item:', stack.pop())
        