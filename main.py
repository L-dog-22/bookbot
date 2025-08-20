with open("/home/l_dog/workspace/github.com/L-dog-22/bookbot/books/frankenstein.txt") as get_book_text:
    bad_bitch = get_book_text.read(None)
    

word_count = bad_bitch.split(maxsplit=1)
#main = print(bad_bitch)
main = print(word_count)