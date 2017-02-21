import codecs
import glob

filelist = []
filelist += glob.glob('../resources/article/*.txt')
filelist += glob.glob('../resources/encyclopedia/*.txt')
filelist += glob.glob('../resources/news/*.txt')
filelist += glob.glob('../resources/novel/*.txt')

sentences = []

for filename in filelist:
    file = codecs.open(filename, 'r', 'utf-8')
    lines = file.readlines()
    for sentence in lines:
        sentences += [sentence.replace('|\r\n', '').split('|')]

print(str(len(sentences)) + ' senteces loaded...')
