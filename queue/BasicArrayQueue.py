from collections import deque

class BasicArrayQueue:
    def __init__(self) -> None:
        self.array = []
        self.size = 0

    def enqueue(self, value) -> None:
        self.array.append(value)
        self.size += 1

    def dequeue(self) -> object:
        if self.size < 1:
            return None

        aux = self.array[0]
        self.array = self.array[1:]
        self.size -= 1

        return aux

    def show_all(self) -> None:
        for item in self.array:
            print('Item:', item)

if __name__ == '__main__':
    queue = BasicArrayQueue()

    print('Enqueue:')
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    queue.show_all()

    print('\nDequeue:')
    queue.dequeue()
    queue.show_all()