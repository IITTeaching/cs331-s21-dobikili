import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    
    notsorted = book_to_words(book_url)
    
    decodedList = []
    encodedList = []
    
    finishedSortedList = []
    
    encoded = setting_length(notsorted)
    
    value = maxLength(encoded) - 1

    
    
    for i in range (value, -1, -1):
        
        count_sort(encoded, i)
        
    y = 0
    
    for i in encoded:
        decodedList.append(i.decode())
    
    for words in decodedList:
        for j in range (len(words)):
            if words[j] == '\0':
                y = words[:j]
                break
       
        encodedList.append(y)
    
    for words in encodedList:
        finishedSortedList.append(words.encode('ascii','replace'))
    
    return finishedSortedList

def setting_length (notsorted):
    
    encoded = []
    decoded = []
    
    words_equalLength = []
    
    maxSize = 0
    
    for i in notsorted:
        decoded.append(i.decode())
    
    for word in decoded:
        if len(word) > maxSize:
            maxSize = len(word)
    
    for words in decoded:
        if len(words) < maxSize:
            words += ('\0'*(maxSize - len(words))) 
            words_equalLength.append(words)
    
    for words in words_equalLength:
        encoded.append(words.encode('ascii','replace'))
    
    return encoded

def maxLength (notsorted):
    
    maxSize = 0
    
    for word in notsorted:
        if len(word) > maxSize:
            maxSize = len(word)
    
    return maxSize

def count_sort (notsorted, value):
   
    x = len(notsorted)
   
    output = [None] * (x)

    counter = [0] * (256)

    
    for i in range(x):
        index = (notsorted[i][value])
        counter[index] += 1
    
    
    for i in range(1, 256):
        counter[i] += counter[i - 1]
    
    i = x - 1
    
    while i >= 0:
        index = (notsorted[i][value])
        output[counter[index] - 1] = notsorted[i]
        counter[index] -= 1
        i -= 1
    
    i = 0
    
    for i in range(0, len(notsorted)):
        notsorted[i] = output[i]
        
# print (radix_a_book('https://www.gutenberg.org/files/84/84-0.txt')[0:40])
# print (sorted (book_to_words('https://www.gutenberg.org/files/84/84-0.txt'))[0:40])
        