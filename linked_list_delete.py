"""
Python program to delete a node in a linked list
at a given position
"""

class Node(object):
    """
    Node class
    """

    def __init__(self, data):
        """
        Constructor to initialize the node object
        """
        self.data = data
        self.next = None

class LinkedList(object):
    """
    Linked list class
    """

    # Constructor to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """
        Function to insert a new node at the beginning
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, position):
        """
        Given a reference to the head of a list
        and a position, delete the node at a given position
        """
 
        # If linked list is empty
        if self.head == None:
            return
 
        # Store head node
        temp = self.head
 
        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
 
        # Find previous node of the node to be deleted
        for i in range(position -1):
            temp = temp.next
            if temp is None:
                break
 
        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return
 
        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next
 
        # Unlink the node from linked list
        temp.next = None
 
        temp.next = next
 
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print " %d " %(temp.data),
            temp = temp.next

my_list = LinkedList()
my_list.push(7)
my_list.push(1)
my_list.push(3)
my_list.push(2)
my_list.push(8)
 
print "Created Linked List: "
my_list.printList()
my_list.delete_node(4)
print "\nLinked List after Deletion at position 4: "
my_list.printList()
