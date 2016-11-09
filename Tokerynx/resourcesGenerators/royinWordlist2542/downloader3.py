from urllib.request import urlretrieve

for i in range(1, 47):
    for j in range(1, 20):
        root = 'http://rirs3.royin.go.th/'
        subfolder = 'word%d/' % i
        filename = 'word-%d-a%d.asp' % (i, j)
        url = root + subfolder + filename
        print('Downloading: ' + root + subfolder + filename)
        try:
            urlretrieve(root + subfolder + filename, filename)
        except:
            print('Not such file name', root + subfolder + filename)

    for j in range(1, 20):
        root = 'http://rirs3.royin.go.th/'
        subfolder = 'word%d/word%d/' % (i, i)
        filename = 'word-%d-a%d.asp' % (i, j)
        url = root + subfolder + filename
        print('Downloading: ' + root + subfolder + filename)
        try:
            urlretrieve(root + subfolder + filename, filename)
        except:
            print('Not such file name', root + subfolder + filename)
