import DoublyLinkedList

class TextEditor:
    def __init__(self):
        self.text = DoublyLinkedList.DoublyLinkedList()
        self.cursor = None

    def insert(self, char):
        new_node = DoublyLinkedList.DoublyLinkedList.Node(char)
        if not self.cursor:
            self.text.head = new_node
            self.cursor = new_node
        else:
            new_node.next = self.cursor.next
            new_node.prev = self.cursor
            if self.cursor.next:
                self.cursor.next.prev = new_node
            self.cursor.next = new_node
            self.cursor = new_node

    def delete(self):
        if self.cursor and self.cursor.next:
            self.cursor.next = self.cursor.next.next
            if self.cursor.next:
                self.cursor.next.prev = self.cursor



        # ... methods for cursor movement, etc.
        

# example usage
text_editor = TextEditor()
text_editor.insert('H')
text_editor.insert('e')
text_editor.insert('l')
text_editor.insert('l')
text_editor.insert('o')