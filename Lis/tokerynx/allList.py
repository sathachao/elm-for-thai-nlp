import tokerynx.lexitronData2Wordlist
import tokerynx.orchidCorpusWordlist
import tokerynx.royin2542Wordlist

wordlist = []
wordlist += tokerynx.lexitronData2Wordlist.wordlist
wordlist += tokerynx.orchidCorpusWordlist.wordlist
wordlist += tokerynx.royin2542Wordlist.wordlist
wordlist = sorted(wordlist)

symbollist = [' ', '.', ',', '/', '(', ')', '=', '+', '-', ':', ';', '\'',
              '"', '$', '?', '&', '#', '*', '>', '<', '^', '!', '{', '}', '@']

# print(len(wordlist))
