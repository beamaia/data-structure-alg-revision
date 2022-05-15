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

    def show_all(self) -> None:
        if not self.head:
            return

        aux = self.head
        for i in range(self.size):
            print(f"Item: {aux.val}")

            aux = aux.next

    def peek(self) -> None:
        print(self.head.val)

if __name__ == "__main__":
    stack = BasicListStack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.show_all()
    print('Last item peeked:', end=' ')
    stack.peek()

    print('Last item popped:', stack.pop())
        