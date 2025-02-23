def get_book_text(file):
    with open(file) as f:
        content = f.read()
    
    return content

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

main()