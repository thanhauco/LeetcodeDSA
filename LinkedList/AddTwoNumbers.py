class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy_head = ListNode(0)  # Start with a dummy node.
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry

        carry = total // 10  # Calculate carry.
        current.next = ListNode(total % 10)  # Add the sum to the result list.
        current = current.next

        # Move to the next nodes in the input lists if available.
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy_head.next  # The result starts after the dummy node.

# Testing
# Example usage of add_two_numbers function

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy_head = ListNode(0)
    current = dummy_head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next

# Helper function to print the linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


def print_linked_list_reverse(head):
    if head is None:
        return
    if head.next is not None:
        print_linked_list_reverse(head.next)  # Recursive call to go to the end of the list
        print(" -> ", end="")  # Print arrow only if not the last element
    print(head.val, end="")  # Print the current value


# Create two linked lists: 342 (represented as 2 -> 4 -> 3) and 465 (represented as 5 -> 6 -> 4)
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

# Call the add_two_numbers function
result = add_two_numbers(l1, l2)


# Print the result
print_linked_list(result)  # Output should represent 807 (7 -> 0 -> 8)

result_number = print_linked_list_reverse(result)  # Convert linked list to integer
print(result_number)  # Output should be 807

