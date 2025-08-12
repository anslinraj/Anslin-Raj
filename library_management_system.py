import os
class Library:
    def __init__(self, name="My Library"):
        self.name = name
        self.books_file = "books.txt"
        self.lending_file = "lending.txt"
        self.booklist = self.load_books()
        self.lendDict = self.load_lending_data()

    def load_books(self):
        if not os.path.exists(self.books_file):
            return []
        with open(self.books_file, "r") as f:
            return [line.strip() for line in f if line.strip()]

    def load_lending_data(self):
        if not os.path.exists(self.lending_file):
            return {}
        lending = {}
        with open(self.lending_file, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    lending[parts[0]] = parts[1]
        return lending

    def save_books(self):
        with open(self.books_file, "w") as f:
            for book in self.booklist:
                f.write(book + "\n")

    def save_lending_data(self):
        with open(self.lending_file, "w") as f:
            for book, user in self.lendDict.items():
                f.write(f"{book}|{user}\n")

    def displayBooks(self):
        print(f"\nBooks available in {self.name}:")
        if not self.booklist:
            print("No books available.")
        for book in self.booklist:
            status = "Available" if book not in self.lendDict else f"Lent to {self.lendDict[book]}"
            print(f"- {book} ({status})")

    def find_book_by_title(self, title):
        for book in self.booklist:
            parts = book.split("|")
            if len(parts) >= 2 and parts[1].strip().lower() == title.lower():
                return book
        return None

    def lendBook(self, user, title):
        book = self.find_book_by_title(title)
        if not book:
            print("Book does not exist in the library.")
        elif book not in self.lendDict:
            self.lendDict[book] = user
            self.save_lending_data()
            print("Lending record has been updated.")
        else:
            print(f"Book is already lent to {self.lendDict[book]}.")

    def addBook(self, book):
        if book in self.booklist:
            print("Book already exists.")
        else:
            self.booklist.append(book)
            self.save_books()
            print("Book has been added to the library.")

    def returnBook(self, title):
        book = self.find_book_by_title(title)
        if not book:
            print("Book does not exist in the library.")
        elif book in self.lendDict:
            del self.lendDict[book]
            self.save_lending_data()
            print("Book has been returned.")
        else:
            print("This book was not lent out.")

def main():
    library = Library(name="Public")

    while True:
        print(f"\nWelcome to the {library.name} Library. Choose an option:")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")

        choice = input("Your choice: ").strip()

        if choice == "1":
            library.displayBooks()

        elif choice == "2":
            title = input("Enter the book name to lend: ").strip()
            user = input("Enter your name: ").strip()
            library.lendBook(user, title)

        elif choice == "3":
            book = input("Enter full book details (e.g. ID|Title|Author|Category|True): ").strip()
            library.addBook(book)

        elif choice == "4":
            title = input("Enter the book name to return: ").strip()
            library.returnBook(title)

        else:
            print("Invalid option.")

        next_step = input("\nPress 'q' to quit or 'c' to continue: ").strip().lower()
        if next_step == "q":
            print("Exiting... Thank you for using the library system.")
            break
        elif next_step != "c":
            print("Invalid input. Continuing...")

main()