class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        
        # if the node is None then there is nothing to reverse. 
        if node is None:
            return

        # if the node has no next node then we are going to make this the 
        # head node...start the reversal.
        if node.next_node is None:
            self.head = node

            # update the node.next to the prev node that will be passed.
            node.next_node = prev
            return
        
        # need to save a new node for recursion...will set the next_node to the current node. 
        new_node = node.next_node

        # need to update the next_node to be the previous node. 
        node.next_node = prev

        self.reverse_list(new_node, node)


