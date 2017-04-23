import Tokerynx.dictionaries.lexitronData2Wordlist
import Tokerynx.dictionaries.orchidCorpusWordlist
import Tokerynx.dictionaries.royin2542Wordlist

wordlist = []
# wordlist += dictionaries.lexitronData2Wordlist.wordlist
# wordlist += dictionaries.orchidCorpusWordlist.wordlist
wordlist += Tokerynx.dictionaries.royin2542Wordlist.wordlist
wordlist = sorted(wordlist)

symbollist = [' ', '.', ',', '/', '(', ')', '=', '+', '-', ':', ';', '\'',
              '"', '$', '?', '&', '#', '*', '>', '<', '^', '!', '{', '}', '@']

# print(len(wordlist))
