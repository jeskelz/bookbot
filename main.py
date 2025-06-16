import sys #built-in sys module

# import from stats.py 
from stats import get_word_count, get_char_count, sort_characters

# takes a filepath as input and returns the contents of the file as a string
def get_book_text(path):
    with open(path) as f:
        return f.read() # read the contents of a file into a string
    

def main():
    if len(sys.argv) != 2: #If sys.argv doesn't have two entries
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1] # path to the book file


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path) # get the entire text of the book

    print("----------- Word Count ----------")
    word_count = get_word_count(text) # get the number of words
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_count = get_char_count(text) # character count
    sorted_chars = sort_characters(char_count)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
