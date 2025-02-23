def get_book_text(file):
    with open(file) as f:
        content = f.read()
    
    return content

def word_counter(string):
    words = string.split()

    return len(words)

def main():
    text = get_book_text("books/frankenstein.txt")

    num_of_words = word_counter(text)
    print(f"{num_of_words} words found in the document")

main()