import file_handler
import book_cleaner
import book_manager

def menu():
    """
    Displays the main menu and handles user interactions.
    Loads and processes book data, then provides options for viewing, searching, and adding books.
    """

    # Load and clean book data from CSV
    books = file_handler.load_books_from_csv("books.csv")
    cleaned_books = book_cleaner.clean_data(books)
    books_by_author, books_by_year = book_manager.group_books(cleaned_books)

    # Save cleaned data to a CSV file
    file_handler.save_books_to_csv("cleaned_books.csv", cleaned_books)

    while True:
        # Display menu options
        print("\n📚 How would you like to view the data?")
        print("1. View books organized by Author")
        print("2. View books organized by Year")
        print("3. Search for a book")
        print("4. Add a new book")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            # Display books grouped by author
            for author, books in sorted(books_by_author.items()):
                print(f"\n👤 {author}:")
                for title, year in books:
                    print(f"   - {title} ({year})")

        elif choice == "2":
            # Display books grouped by year
            for year, books in sorted(books_by_year.items()):
                print(f"\n📅 {year}:")
                for title, author in books:
                    print(f"   - {title} (Author: {author})")

        elif choice == "3":
            # Search for books by title or author
            book_manager.search_books(cleaned_books)

        elif choice == "4":
            # Add a new book and update grouped lists
            book_manager.add_new_book(cleaned_books)
            books_by_author, books_by_year = book_manager.group_books(cleaned_books)

        elif choice == "5":
            # Save updated book lists before exiting
            file_handler.save_books_to_txt("books_by_author.txt", books_by_author, books_by_year)
            print("\n📁 Data has been saved. 👋 Exiting the program...")
            break

        else:
            print("\n⚠️ Invalid option. Please try again.")