class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.val = value

class BasicLinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, value) -> None:
        """
        Inserts node into the beginning of the list
        """
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def append(self, value) -> None:
        """
        Inserts node into the end of the list
        """
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            aux = self.head

            while aux.next:
                aux = aux.next

            aux.next = node

    def insert(self, value_add, value_search) -> None:
        """
        Inserts node after a certain value in the list
        """
        node = Node(value_add)

        aux = self.head
        while aux:
            if aux.val == value_search:
                break
            aux = aux.next

        if not aux:
            print("Value not found") 
            return
        
        node.next = aux.next
        aux.next = node
    
    def insertIndex(self, value_add, index) -> None:
        """
        Inserts node into a certain index of the list
        """
        index_counter = 0
        node = Node(value_add)

        aux = self.head
        while aux:
            if index_counter == index - 1:
                break
            aux = aux.next
            index_counter += 1

        if not aux:
            print(f"There is no index {index} in linked list") 
            return
        
        node.next = aux.next
        aux.next = node

    def show_list(self) -> None:
        aux = self.head
        counter = 0

        while aux:
            print(f"Node {counter}: {aux.val}")
            aux = aux.next
            counter += 1

if __name__ == "__main__":
    linked_list = BasicLinkedList()

    linked_list.append(10)
    linked_list.append(2)
    linked_list.append(30)
    linked_list.insert(23, 2)
    linked_list.insertIndex(32, 1)

    linked_list.show_list()