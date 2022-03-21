""" Implementation of a linked list in python """


from random import randint


class Node:
    """Node class"""

    def __init__(self, data):
        """Function to initialise the node object"""
        self.data = data
        self.next = None


class LinkedList:
    """Linked List class contains a Node object"""

    def __init__(self):
        """Function to initialize head"""
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def put(self, new_data):
        """Put a node in the beginning of the linked list"""
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def get_data_by_idx(self, index):
        """Returns data at given index in linked list"""
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next

        assert IndexError(f"Index {index} not found in linked list")

    def get_idx_by_val(self, val):
        """Get index inside linked list by value"""
        current = self.head
        count = 0

        while current:
            if current.data == val:
                return count
            count += 1
            current = current.next

        raise ValueError(f"Value {val} not found in the linked list")


if __name__ == "__main__":
    llist = LinkedList()
    for i in range(20):
        llist.put(randint(0, 150))
    llist.put(8)

    print("Element at index 4 is :", llist.get_data_by_idx(4))
    print("Element index by value 8:", llist.get_idx_by_val(8))
    print(llist)
