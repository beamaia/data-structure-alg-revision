from Node import Node

class BasicListQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value) -> None:
        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def dequeue(self) -> object:
        if not self.size:
            return None

        aux = self.head
        self.head = self.head.next
        self.size -= 1

        return aux

    def show_all(self) -> None:
        aux = self.head
        for i in range(self.size):
            print('Item', aux.val)

            aux = aux.next

if __name__ == '__main__':
    queue = BasicListQueue()

    print('Enqueue')
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    queue.show_all()

    print('\nDequeue')
    queue.dequeue()
    queue.show_all()