class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.is_empty():
            self.tail = new_node

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:  # Update tail if the list was initially empty
            self.tail = new_node

    def delete_node(self, key):
        if self.is_empty():
            return

        current_node = self.head
        if current_node.data == key:
            self.head = current_node.next
            if self.head is None:  # Update tail if the list becomes empty
                self.tail = None
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        if prev_node.next is None:  # Update tail if the last node is deleted
            self.tail = prev_node
        current_node = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print("None")

    def append_after(self, data, pos):

        if pos is None:
            print("Position cannot be None")
            return

        if self.is_empty() or pos == self.get_last_index():
            self.append(data)
            return
        new_node = Node(data)

        n = self.head

        if n is None:
            print(pos, "Not found")
            return

        new_node.next = n.next
        n.next = new_node

    def get_last_index(self):
        index = 0
        current_node = self.head
        while current_node and current_node.next:
            current_node = current_node.next
            index += 1
        return index

    def append_before(self, data, pos):
        if pos is None:
            raise ValueError("Position cannot be None")

        if self.is_empty() or pos == 0:
            self.add_head(data)
            return

        new_node = Node(data)
        current_node = self.head
        prev_node = None
        index = 0

        while current_node and index < pos:
            prev_node = current_node
            current_node = current_node.next
            index += 1

        if current_node is None and index < pos:
            # Position is greater than the last index, so append at the end
            self.append(data)
            return

        prev_node.next = new_node
        new_node.next = current_node

    def removeFromLast(self, head , n):
        dummy = ListNode(0,head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        # print(left.val)

        left.next = left.next.next
        # print(left.next.val)
        # print(dummy.next.next.next.next.val)
        return dummy.next

    def rotatebyK(self,head,k):
        if not head or k == 0:
            return head

        len, tail = 1, head
        while tail.next:
            tail = tail.next
            len += 1
        k %= len
        if k == 0:
            return head  # No rotation needed

        # Step 3: Traverse to find the new tail node
        cnt = head
        for _ in range(len - k - 1):
            cnt = cnt.next

        # Step 4: Rotate the linked list
        new_head = cnt.next
        cnt.next = None
        tail.next = head
        return new_head





    # # Definition for singly-linked list.
    # # class ListNode:
    # #     def __init__(self, val=0, next=None):
    # #         self.val = val
    # #         self.next = next
    # class Solution:
    #     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #         nodes = []
    #         node = head
    #         count = 0
    #         while node != None:
    #             nodes.append(node)
    #             node = node.next
    #             count += 1
    #
    #         if count == 1 and n == 1:
    #             return None
    #         elif n == count:
    #             return nodes[1]
    #         else:
    #             idx = count - n
    #             rem = nodes[idx]
    #             prv = nodes[idx - 1]
    #             prv.next = rem.next
    #             rem.next = None
    #             return head

def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Convert a linked list to a list
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst



# # Example usage:
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.add_head(0)
# print("LL is:")
# linked_list.print_list()
#
# print("After deletion:")
# linked_list.delete_node(2)
# linked_list.print_list()
#
# print("Adding node after a given position:")
# linked_list.append_after(200, 2)
# linked_list.print_list()
#
# print("Number of elements in Linkedlist")
# print(linked_list.get_last_index() + 1)
#
# print("Adding node before a given position:")
# linked_list.append_before(500, 3)
# linked_list.print_list()
#
#
# print("New Linked List:")
# linked_list2 = LinkedList()
# head = list_to_linked_list([1, 2, 3, 4, 5])
# print(linked_list_to_list(head))
# print("Given the head of a linked list, remove the nth node from the end of the list and return its head:")
# new_head = linked_list2.removeFromLast(head, 2)
# print(linked_list_to_list(new_head))


print("New Linked List:")
linked_list3 = LinkedList()
head = list_to_linked_list([1 , 2 , 3 , 4 , 5])
print(linked_list_to_list(head))
print("Given the head of a linked list, rotate the list to the right by k places.")
new_head = linked_list3.rotatebyK(head , 2)
print(linked_list_to_list(new_head))