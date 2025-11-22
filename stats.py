def get_book(filepath):
    with open(filepath, "r") as f:
        return f.read()

def get_book_words(book):
    book_words = book.split()
    return f"Found {len(book_words)} total words."

def get_book_number_of_letters(book):
    chars = {}
    for char in book:
        chars[char.lower()] = chars.get(char.lower(), 0) + 1

    return chars

def sort_dict(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
