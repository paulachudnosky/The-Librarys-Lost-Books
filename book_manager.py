from collections import defaultdict
import file_handler

# Book Management Module

def group_books(books):
    """
    Groups books by author and by publication year.
    Returns two dictionaries: one sorted by author and one by year.
    """
    grouped_by_author = defaultdict(list)
    grouped_by_year = defaultdict(list)

    for title, author, year in books:
        grouped_by_author[author].append((title, year))
        grouped_by_year[year].append((title, author))

    return grouped_by_author, grouped_by_year

def search_books(books):
    """
    Allows the user to search for a book by title or author.
    Displays results if found.
    """
    query = input("\n🔎 Enter the book title or author to search: ").strip().lower()
    results = [book for book in books if query in book[0].lower() or query in book[1].lower()]

    if results:
        print("\n📚 Search Results:")
        for title, author, year in results:
            print(f"   - {title} | {author} | {year}")
    else:
        print("\n⚠️ No results found.")

def add_new_book(cleaned_books):
    """
    Adds a new book to the collection, ensuring valid data input.
    Saves the updated list to the CSV file.
    """
    title = input("Enter the book title: ").strip()
    author = input("Enter the author's name (leave blank if unknown): ").strip() or "Author Unknown"

    while True:
        try:
            year = int(input("Enter the publication year (use 0 if unknown): ").strip())
            if year < 0 or year > 2025:
                raise ValueError  # Force user to re-enter if invalid
            break
        except ValueError:
            print("⚠️ Invalid year. Please enter a number between 0 and 2025.")

    new_book = (title, author, year)

    # Add to in-memory list
    cleaned_books.append(new_book)

    # Save to CSV
    file_handler.save_books_to_csv("cleaned_books.csv", cleaned_books)

    print(f"\n✅ Book added: {new_book}\n")
