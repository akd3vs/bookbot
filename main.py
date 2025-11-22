import sys

from stats import get_book_words, get_book, get_book_number_of_letters, sort_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    book = sys.argv[1]
    book_content = get_book(book)
    words = get_book_words(book_content)
    letter_count = get_book_number_of_letters(book_content)
    letter_count_sorted = sort_dict(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at { book }...")
    print("----------- Word Count ----------")
    print(words)
    print("--------- Character Count -------")
    for letter, count in letter_count_sorted:
        print(f"{letter}: {count}")
    print("============= END ===============")

main()
