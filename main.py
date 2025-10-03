import sys
from stats import get_num_words, get_num_characters, report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    get_num_words(text)
    print("--------- Character Count -------")
    text_dict = get_num_characters(text)
    sorted_chars = report(text_dict)
    for dic in sorted_chars:
        char, num = dic.values()
        if char.isalpha():
            print(f"{char}: {num}")
main()
