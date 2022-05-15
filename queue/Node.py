class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.val = value

    def __str__(self) -> str:
        return str(self.val)