class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Linked:

    def __init__(self):
        self.head = None


if __name__ == '__main__':

    linked_list = Linked()

    linked_list.head = Node(4)
    second = Node(5)
    third = Node(6)

    linked_list.head.next = second
    second.next = third

    #
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next
