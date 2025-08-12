def wordcount (text):
    count = text.split()
    zahler = 0
    for i in count:
        zahler += 1
    return zahler
 

def lettercount (stringy):
    lowy = stringy.lower()
    dicty = {}
    for char in lowy:
        
        if char in dicty:     
            dicty[char] += 1
        else:
            dicty[char] = 1

    return dicty
        
def dictsorter (dictarray):
    listofdict=[]
    for entry in dictarray:
        entry = {"char": entry,
                 "num": dictarray[entry]}
        listofdict.append(entry)
        
    def sort_on(item):
        return item["num"]
    listofdict.sort(reverse=True, key=sort_on)
    
    return listofdict

    

