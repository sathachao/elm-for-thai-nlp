import codecs
import glob

filelist = []
filelist += glob.glob('../resources/article/*.txt')
filelist += glob.glob('../resources/encyclopedia/*.txt')
filelist += glob.glob('../resources/news/*.txt')
filelist += glob.glob('../resources/novel/*.txt')



for filename in filelist:
    file = codecs.open(filename, 'r', 'utf-8')
    writeFile = codecs.open(filename + "_fixed", 'w', 'utf-8')
    lines = file.readlines()

    for line in lines:
        if not (line.count("http") > 0 or line.count("www") > 0 or line.count("WWW") > 0):
            writeFile.write(line)

print("File Fixing Done")
