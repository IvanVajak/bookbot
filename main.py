from stats import wordcount, lettercount

def main ():
    #get_book_text("books/frankenstein.txt")
    text = get_book_text("books/frankenstein.txt")
    count = wordcount(text)
    print(f"{count} words found in the document")
    letterdict = lettercount(text)
    print(letterdict)


def get_book_text (filepath):
    contents=""
    with open(filepath) as f:
        contents = f.read() 
    return contents
   # wordcount(contents)
   # lettercount(contents)


main()