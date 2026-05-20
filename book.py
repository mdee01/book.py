class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True  # Available status (True = available, False = borrowed)

    # Getter para sa available status
    def is_available(self):
        return self.available

    # Setter para baguhin ang status
    def set_available(self, status):
        self.available = status
