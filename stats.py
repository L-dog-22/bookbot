Char_dict = {}


with open("/home/l_dog/workspace/github.com/L-dog-22/bookbot/books/frankenstein.txt") as get_book_text:
    file_contents = get_book_text.read(None)
    
#for i in word_list redundant use word_count instead 
word_list = file_contents.split()
word_count = len(word_list)
for i in word_list:
    if i in Char_dict:
        Char_dict[i] += 1
    else:
        Char_dict[i] = 1

   

#main = print(word_count, "words found in the document")
#main = print(stat_dict)


cheese = print(word_count, "words found in the document")
toast = print(Char_dict)
    