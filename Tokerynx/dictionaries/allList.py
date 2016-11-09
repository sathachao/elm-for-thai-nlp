import dictionaries.lexitronData2Wordlist
import dictionaries.orchidCorpusWordlist
import dictionaries.royin2542Wordlist

wordlist = []
# wordlist += dictionaries.lexitronData2Wordlist.wordlist
# wordlist += dictionaries.orchidCorpusWordlist.wordlist
wordlist += dictionaries.royin2542Wordlist.wordlist
wordlist = sorted(wordlist)

symbollist = [' ', '.', ',', '/', '(', ')', '=', '+', '-', ':', ';', '\'',
              '"', '$', '?', '&', '#', '*', '>', '<', '^', '!', '{', '}', '@']

print('การ' in wordlist)
