import re
import glob

thainumber = {0: '๐', 1: '๑', 2: '๒', 3: '๓', 4: '๔', 5: '๕', 6: '๖', 7: '๗', 8: '๘', 9: '๙'}
wordlist = set()

filenames = glob.glob('utf8\\*.asp.utf8')
print(len(filenames), filenames)
for filename in filenames:
    print('Loading file: ', filename)
    file = open(filename, mode='r+', encoding='utf-8')
    data = file.read()
    data = re.findall(r'<font color = blue>[<b>]*(.*?)[<\/b>]*<\/font>', data)
    print(len(data), ':', data)
    for words in data:
        words = words.split(', ')
        for word in words:
            while word[-1] in thainumber.values() or word[-1] == ' ':
                word = word[:-1]
            print(len(word), ':', word, ord(word[-1]))
            wordlist.add(word)

wordlist = sorted(wordlist)

print('Total number of words: ', len(wordlist))

file = open('../../dictionaries/royin2542Wordlist.py', mode='w+', encoding='utf-8')
file.write('wordlist = ' + str(wordlist))
