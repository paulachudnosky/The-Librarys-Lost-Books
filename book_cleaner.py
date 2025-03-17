# Data Cleaning Module

def clean_data(books):
    """
    Cleans book data by standardizing author names, validating publication years,
    and removing duplicates based on title and author.
    """
    cleaned_books = []
    seen_books = set()

    for book in books:
        title, author, year = book

        # Assign "Author Unknown" if the author field is empty
        author = author.strip() or "Author Unknown"

        # Validate publication year
        try:
            year = int(year)
            if year < 0 or year > 2025:
                year = 0  # Default to 0 if the year is invalid
        except ValueError:
            year = 0

        # Create a unique key for detecting duplicates (Title + Author)
        book_key = (title.strip().lower(), author.strip().lower())
        if book_key not in seen_books:
            seen_books.add(book_key)
            cleaned_books.append([title.strip(), author, year])

    return cleaned_books
