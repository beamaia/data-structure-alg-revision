from Node import Node

class CircularList:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, value) -> None:
        node = Node(value)

        # List is empty
        if not self.head:
            node.next = node
        else:
            aux = self.head
            node.next = self.head
            
            while aux.next != self.head:
                aux = aux.next

            aux.next = node
            
        self.head = node 

    def show_list(self) -> None:
        if not self.head:
            return

        print(f"Node 0: {self.head.val}")

        aux = self.head.next
        counter = 1

        while aux and aux != self.head:
            print(f"Node {counter}: {aux.val}")
            aux = aux.next
            counter += 1

if __name__ == "__main__":
    circular_list = CircularList()

    circular_list.push(1)
    circular_list.push(2)
    circular_list.push(3)

    circular_list.show_list()

        
