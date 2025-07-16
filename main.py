import sys #built-in sys module
import os
from colorama import Fore, Style, init

# import from stats.py 
from stats import get_word_count, get_char_count, sort_characters, get_top_words

init(autoreset=True)

# takes a filepath as input and returns the contents of the file as a string
def get_book_text(path):
    with open(path) as f:
        return f.read() # read the contents of a file into a string

# get report file name
def get_next_report_filename(prefix="report_", suffix=".txt"):
    existing = [f for f in os.listdir() if f.startswith(prefix) and f.endswith(suffix)]
    nums = []

    for filename in existing:
        try:
            num = int(filename[len(prefix):-len(suffix)])
            nums.append(num)
        except ValueError:
            continue

    next_num = max(nums) + 1 if nums else 1
    return f"{prefix}{next_num}{suffix}"

def write_report(lines, filename):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")
    

def main():
    if len(sys.argv) != 2: #If sys.argv doesn't have two entries
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1] # path to the book file
    text = get_book_text(book_path)
    report_lines = []


    # get the entire text of the book
    print(Fore.GREEN + Style.BRIGHT + "============ BOOKBOT ============")
    print(Fore.YELLOW + f"Analyzing book found at {book_path}...")
    report_lines.append("============ BOOKBOT ============")
    report_lines.append(f"Analyzing book found at {book_path}...")


    # get the number of words
    print(Fore.CYAN + "----------- Word Count ----------")
    word_count = get_word_count(text)
    print(Fore.YELLOW + f"Found {word_count} total words")
    report_lines.append("----------- Word Count ----------")
    report_lines.append(f"Found {word_count} total words")
    

    # character count
    print(Fore.CYAN + "--------- Character Count -------")
    report_lines.append("--------- Character Count -------")
    char_count = get_char_count(text)
    sorted_chars = sort_characters(char_count)

    for item in sorted_chars:
        line = f"{item['char']}: {item['num']}"
        print(Fore.MAGENTA + line)
        report_lines.append(line)


    # Top 10 Most Common Words
    print(Fore.CYAN + "----------- Top 10 Words --------")
    report_lines.append("----------- Top 10 Words --------")
    top_words = get_top_words(text)

    for word, count in top_words:
        line = f"{word}: {count}"
        print(Fore.BLUE + line)
        report_lines.append(line)

    print(Fore.GREEN + "============= END ===============")
    report_lines.append("============= END ===============")

    # Generate numbered filename
    filename = get_next_report_filename()
    write_report(report_lines, filename)
    print(Fore.GREEN + f"📄 Report saved as {filename}")

main()
