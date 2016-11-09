import re
import glob

file = open('telex', mode='r+', encoding='utf-8')
filedata = file.read()

wordlist = re.findall(r'<tsearch>[\ ]*(.+)[\ ]*<\/tsearch>', filedata)
wordlist = set(wordlist)
wordlist = sorted(wordlist)

print('Total number of words: ', len(wordlist))

file = open('../../dictionaries/lexitronData2Wordlist.py', mode='w+', encoding='utf-8')
file.write('wordlist = ' + str(wordlist))
for i in wordlist:
    if ' ' in i:
        print(i)
print('These could be invalid words')
