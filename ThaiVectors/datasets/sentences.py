import codecs
import glob
import datasets.constants as const

filelist = []
filelist += glob.glob('../resources/article/*.txt')
filelist += glob.glob('../resources/encyclopedia/*.txt')
filelist += glob.glob('../resources/news/*.txt')
filelist += glob.glob('../resources/novel/*.txt')

exceptions = ["\"", ]

sentences = []
documents = []

docCount = -1

count = 0

for filename in filelist:
    file = codecs.open(filename, 'r', 'utf-8')
    lines = file.readlines()

    docCount += 1
    documents.append([])

    for sentence in lines:
        # if sentence.count("http") > 0 or sentence.count("www") > 0 or sentence.count("WWW") > 0:
        #     if len(documents[docCount]) > 0:
        #         docCount += 1
        #         documents.append([])
        #     continue
        newSentence = []
        newDoc = []
        for word in sentence.replace('|\r\n', '').split('|'):

            wordType = 0
            if word.count("<NE>") > 0:
                wordType = 1
                word = (word.replace('<NE>', '')).replace("</NE>", '')
            word = (word.replace('<AB>', '')).replace("</AB>", '')

            # Sentence
            newSentence.append(word)

            # Extract Class
            newDoc += [[word, wordType]]
            count += 1

        sentences += [newSentence] + [[const.NEW_LINE]]
        documents[docCount] += newDoc + [[const.NEW_LINE, 0]]

print(str(len(sentences)) + ' sentences loaded...')
