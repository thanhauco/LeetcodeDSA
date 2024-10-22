import DoublyLinkedList

class BrowserHistory:
    def __init__(self):
        self.current = None
        
    def visit(self, url):
        new_node = DoublyLinkedList.DoublyLinkedList.Node(url)
        if self.current:
            new_node.prev = self.current
            self.current.next = new_node
        self.current = new_node
        
    def back(self):
        if self.current.prev:
            self.current = self.current.prev
        return self.current.data
        
    def forward(self):
        if self.current.next:
            self.current = self.current.next
        return self.current.data

# Example usage
browser = BrowserHistory()
browser.visit("https://www.google.com")
browser.visit("https://www.facebook.com")
print(browser.back())  # Output: "https://www.google.com"
print(browser.forward())  # Output: "https://www.facebook.com"