import sys

# get some functions from stats.py file
from stats import word_counter
from stats import char_counter
from stats import sorter

# function to open the file and get its contents
def get_book_text(file):
    with open(file) as f:
        content = f.read()
    
    return content

def main():
    # if the user does not put in correct format, exit with 1 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # sets the path to be whatever the user puts as the second command line argument
    path = sys.argv[1] 
    text = get_book_text(path)

    # gets number of words and character list and count
    num_of_words = word_counter(text)
    char_count = char_counter(text)

    # formatting output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    sorted_list = sorter(char_count)
    
    for char_dict in sorted_list:
        for char, count in char_dict.items():
            if char.isalpha():  # only print alphabetical characters
                print(f"{char}: {count}")

main()