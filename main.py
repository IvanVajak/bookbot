import sys
from stats import wordcount, lettercount, dictsorter

def main ():
    #get_book_text("books/frankenstein.txt")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count = wordcount(text)
    letterdict = lettercount(text)
   # print(letterdict)
    sorted_list= dictsorter(letterdict)

    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        char = entry["char"]
        numb = entry["num"]

        if char.isalpha():
            print(f"{char}: {numb}")

    print("============= END ===============")
    

def get_book_text (filepath):
    contents=""
    with open(filepath) as f:
        contents = f.read() 
    return contents
   # wordcount(contents)
   # lettercount(contents)


main()