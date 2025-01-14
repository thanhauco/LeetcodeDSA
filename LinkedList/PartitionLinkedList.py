class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def partition(head, x):
    # Dummy nodes for the two partitions
    smaller_head = ListNode(0)
    greater_head = ListNode(0)

    # Pointers to the end of the two partitions
    smaller = smaller_head
    greater = greater_head

    # Traverse the original list
    while head:
        if head.value < x:
            smaller.next = head
            smaller = smaller.next
        else:
            greater.next = head
            greater = greater.next
        head = head.next

    # Combine the two partitions
    greater.next = None  # Ensure the last node of the greater partition points to None
    smaller.next = greater_head.next

    return smaller_head.next  # Return the new head of the partitioned list

# Example Usage
# Input: 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# Partition the list
partitioned_head = partition(node1, 3)

# Print the result
current = partitioned_head
while current:
    print(current.value, end=" -> ")
    current = current.next
# Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5 -> 