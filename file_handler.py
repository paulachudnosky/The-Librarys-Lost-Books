import csv

# File Handling Module

def load_books_from_csv(filename):
    """
    Loads book data from a CSV file.
    Returns a list of books, each represented as a tuple (title, author, year).
    """
    books = []
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) == 3:
                    title, author, year = row
                    books.append((title, author, year))
    except FileNotFoundError:
        print(f"⚠️ {filename} not found. Starting with an empty list.")

    return books

def save_books_to_csv(filename, books):
    """
    Saves the list of books to a CSV file with headers.
    """
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "Publication Year"])
        writer.writerows(books)

def save_books_to_txt(filename, books_by_author, books_by_year):
    """
    Saves book data to separate text files, organized by author and by year.
    """
    with open("books_by_author.txt", mode="w", encoding="utf-8") as file:
        for author, books in sorted(books_by_author.items()):
            file.write(f"\n👤 {author}:\n")
            for title, year in books:
                file.write(f"   - {title} ({year})\n")

    with open("books_by_year.txt", mode="w", encoding="utf-8") as file:
        for year, books in sorted(books_by_year.items()):
            file.write(f"\n📅 {year}:\n")
            for title, author in books:
                file.write(f"   - {title} (Author: {author})\n")
