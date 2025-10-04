import sys
from stats import get_num_words, get_num_characters, report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def print_func(book, text, char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    get_num_words(text)
    print("--------- Character Count -------")
    for dic in char_dict:
        char, num = dic.values()
        if char.isalpha():
            print(f"{char}: {num}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    text_dict = get_num_characters(text)
    sorted_chars = report(text_dict)
    print_func(book=sys.argv[1], text=text, char_dict=sorted_chars)

main()
