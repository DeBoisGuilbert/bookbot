import sys

from stats import count_words, count_characters, sorted_list_of_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def print_report(raw_values):
    
    for entry in raw_values:
        entry_char = entry.get("char")
        if entry_char != None and entry_char.isalpha():
            char_count = entry.get("num")
            print(F"{entry_char}: {char_count}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    contents = get_book_text(sys.argv[1])
    print(F"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = count_words(contents)
    print(F"Found {num_words} total words")
    print("--------- Character Count -------")
    char_dict = count_characters(contents)
    print_report(sorted_list_of_dicts(char_dict))
    print("============= END ===============")

main()