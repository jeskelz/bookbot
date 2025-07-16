import sys
import datetime  # U1 - imports datetime for Report#
import os  # lets code interact with OS

from stats import get_num_words, get_lower_count, sort_char_counts, get_top_words

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# U4 - error handling for invalid/wrong path in WSL. now gives updated list based on directory
def get_book_text(path):
    try:
        with open(path, encoding="UTF-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Wrong or invalid path. Try this code instead:  python3 main.py books/bookname.txt\n")
        print("Available books are:")

        if not os.path.exists("books"):  # checks if 'books' folder exists
            print("'books' folder not found.")
        else:
            book_files = os.listdir("books")  # code for directory searching
            txt_files = sorted([f for f in book_files if f.endswith(".txt")])  # only searches for .txt files which are the books' extension
            if not txt_files:  # if no books are inside the folder, it will print this
                print("No books found in the 'books' folder.")
            else:
                for i, filename in enumerate(txt_files, start=1):
                    print(f"{i}. {filename[:-4]}")  # Removes .txt extension on the output
                    
        sys.exit(1)

def main(): # report collection for output
    book_path = sys.argv[1]
    book_filename = os.path.basename(book_path)         # gets bookname
    book_name = os.path.splitext(book_filename)[0]      # gets removes bookname extension
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    char_counts = get_lower_count(text)
    sorted_chars = sort_char_counts(char_counts)

    report_lines = []
    report_lines.append("============ BOOKBOT ============")
    report_lines.append("Analyzing book found at " + book_path + "...\n")

    report_lines.append("----------- Word Count ----------")
    report_lines.append(f"Found {num_words} total words\n")

    report_lines.append("---------- Top 10 Words ---------")  #U3 - shows top 10 words
    top_words, total_words = get_top_words(text, top_n=10)
    report_lines.append("Word | Count   | %")
    report_lines.append("---------------------")
    for word, count in top_words:
        percent = (count / total_words) * 100
        report_lines.append(f"{word:4} | {count:7} | {percent:5.1f}%")
    report_lines.append("")

    report_lines.append("--------- Character Count -------") #U2 - show output like a table and include percentages
    total_chars = sum(item["num"] for item in sorted_chars)
    report_lines.append("Char | Count   | %")
    report_lines.append("---------------------")
    for item in sorted_chars:
        percent = (item["num"] / total_chars) * 100
        report_lines.append(f"{item['char']:4} | {item['num']:7} | {percent:5.1f}%")
    report_lines.append("")

    now = datetime.datetime.now() #U1 - also generate Report# at the bottom
    timestamp = now.strftime("%Y%m%d%H%M%S")
    report_number = f"0000{timestamp}"
    report_label = f"Report #{report_number}"
    report_lines.append("============= END ===============")
    report_lines.append(report_label)

    # Prints the report to terminal if successful
    for line in report_lines:
        print(line)

    # Saves report to books/reports/ folder
    reports_folder = os.path.join("books", "reports")
    os.makedirs(reports_folder, exist_ok=True)  # creates the 'report' folder inside the 'books' folder if none exists

    report_filename = os.path.join(reports_folder, f"{book_name}_Report#{report_number}.txt") #creates file name and saves as .txt
    with open(report_filename, "w", encoding="utf-8") as f:
        for line in report_lines:
            f.write(line + "\n")

main()
