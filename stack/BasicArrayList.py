class BasicArrayStack:
    def __init__(self) -> None:
        self.array = []
        self.size = 0

    def push(self, value) -> None:
        self.array.append(value)
        self.size += 1

    def pop(self) -> object:
        if not self.size:
            return None

        aux = self.array.pop()
        self.size -= 1

        return aux
    
    def peek(self) -> None:
        for i in range(self.size - 1, -1, -1):
            print('Item:', self.array[i])
    
if __name__ == "__main__":
    stack = BasicArrayStack()

    stack.push(123)
    stack.push(23)
    stack.push(12)

    stack.peek()

    print("Item removed:", stack.pop())
    stack.peek()

