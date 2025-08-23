with open("/home/l_dog/workspace/github.com/L-dog-22/bookbot/books/frankenstein.txt") as get_book_text:
    file_contents = get_book_text.read(None)
    

word_list = file_contents.split()
word_count = len(word_list)
main = print(word_count, "words found in the document")