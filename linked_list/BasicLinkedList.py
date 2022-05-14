from Node import Node

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
    
    def insertIndex(self, value_add, index:int) -> None:
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

    def delete(self, value) -> None:
        # If linked list is empty
        if not self.head:
            return 

        # If value is head of linked list
        if self.head.val == value:
            self.head = self.head.next

        # Searches for value in linked list
        else:
            # Searches head's next value and stores head's value
            prev = self.head
            aux = self.head.next
            
            # Searches value in list
            while aux:
                if aux.val == value:
                    break
                
                prev = aux
                aux = aux.next
            

            if not aux:
                print(f'Value {value} not found')
                return

            prev.next = aux.next

    def deleteIndex(self, index:int) -> None:
        # If linked list is empty
        if not self.head:
            return 

        # If index = 0
        if not index:
            self.head = self.head.next
            return

        aux = self.head.next
        prev = self.head
        counter = 1

        while aux:
            if counter == index:
                break
            prev = aux
            aux = aux.next
            counter += 1

        if not aux:
            print(f"Linked list doesn't have index {index}")
            return 

        prev.next = aux.next
                
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
    linked_list.deleteIndex(2)

    linked_list.show_list()