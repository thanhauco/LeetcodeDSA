class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty stack

    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Method to push an element onto the stack
    def push(self, element):
        self.stack.append(element)
        print(f"Pushed {element} onto the stack")

    # Method to pop an element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    # Method to peek at the top element of the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    # Method to display the stack contents
    def display(self):
        print(f"Stack contents: {self.stack}")

# Create a stack instance
my_stack = Stack()

# Push elements onto the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Display the stack contents
my_stack.display()

# Pop an element from the stack
print(f"Popped element: {my_stack.pop()}")

# Peek at the top element
print(f"Top element after popping: {my_stack.peek()}")

# Display the stack again
my_stack.display()
