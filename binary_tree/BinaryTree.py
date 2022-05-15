class Node:
    def __init__(self, value) -> None:     
        self.data = value
        self.left = None
        self.right = None

    def root_value(self) -> str:
        return self.data

    def print_inorder(self) -> None:
        '''
        Inorder traversal:
        - visit left node
        - visit root node
        - visit right node
        '''
        if not self.data:
            return

        if self.left:
            self.left.print_inorder()

        print(self.data, end=' ')

        if self.right:
            self.right.print_inorder()

    def print_preorder(self) -> None:
        '''
        Preorder traversal:
        - visit root
        - visit left node
        - visit right node
        '''

        if not self.data:
            return

        print(self.data, end=' ')

        if self.left:
            self.left.print_preorder()

        if self.right:
            self.right.print_preorder()
    
    def print_postorder(self) -> None:
        '''
        Preorder traversal:
        - visit left node
        - visit right node
        - visit root
        '''
        if not self.data:
            return

        if self.left:
            self.left.print_postorder()

        if self.right:
            self.right.print_postorder()
        
        print(self.data, end=' ')

    def print_breadth(self) -> None:
        queue = []
        queue.append(self)

        while len(queue):
            aux = queue.pop(0)

            print(aux.data, end= ' ')

            if aux.left:
                queue.append(aux.left)
            if aux.right:
                queue.append(aux.right)
 
    def print_zigzag_breadth(self) -> None:
        queue = [self]
        queue_height = [self.height()]
        
        while len(queue):
            aux = queue.pop(0)
            aux_height = queue_height.pop(0)

            print(aux.data, end= ' ')


            if not aux_height % 2:
                if aux.left:
                    queue.append(aux.left)
                    queue_height.append(aux.left.height())

                if aux.right:
                    queue.append(aux.right)
                    queue_height.append(aux.right.height())

            else:
                if aux.right:
                    queue.append(aux.right)
                    queue_height.append(aux.right.height())
                if aux.left:
                    queue.append(aux.left)
                    queue_height.append(aux.left.height())
    
    def height(self) -> int:
        if not self.data:
            return 0
        elif not self.right or not self.left:
            return 1
        
        if self.left:
            left_height = self.left.height() + 1
        else:
            left_height = 0
        
        if self.right:
            right_height = self.right.height() + 1
        else:
            right_height = 0

        if left_height > right_height:
            return left_height
        return right_height



if __name__ == '__main__':
    '''
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
    '''
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print('Printing tree inorder...')
    root.print_inorder()

    print('\nPrinting tree preorder...')
    root.print_preorder()

    print('\nPrinting tree postorder...')
    root.print_postorder()

    print('\nPrinting tree breadth first order...')
    root.print_breadth()

    print('\nPrinting tree zigzag breadth first order...')
    root.print_zigzag_breadth()

    print('\nHeight:', root.height())