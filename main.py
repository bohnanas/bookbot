# function to open the file and get its contents
def get_book_text(file):
    with open(file) as f:
        content = f.read()
    
    return content

# get some functions from stats.py
from stats import word_counter
from stats import char_counter
from stats import sorter # TO DO

def main():
    # passes in the *relative* path
    text = get_book_text("books/frankenstein.txt")

    num_of_words = word_counter(text)
    char_count = char_counter(text)

    print(f"{num_of_words} words found in the document")
    print(char_count)

main()