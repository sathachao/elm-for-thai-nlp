from urllib.request import urlretrieve

for i in range(1, 47):
    j = 1
    while True:
        root = 'http://rirs3.royin.go.th/'
        subfolder = 'word%d/' % i
        filename = 'word-%d-a%d.asp' % (i, j)
        url = root + subfolder + filename
        print('Downloading: ' + root + subfolder + filename)
        try:
            urlretrieve(root + subfolder + filename, filename)
        except:
            print('Not such file name', root + subfolder + filename)
            break
        j += 1

    j = 10
    while True:
        root = 'http://rirs3.royin.go.th/'
        subfolder = 'word%d/' % i
        filename = 'word-%d-a%d.asp' % (i, j)
        url = root + subfolder + filename
        print('Downloading: ' + root + subfolder + filename)
        try:
            urlretrieve(root + subfolder + filename, filename)
        except:
            print('Not such file name', root + subfolder + filename)
            break
        j += 1

    j = 1
    while True:
        root = 'http://rirs3.royin.go.th/'
        subfolder = 'word%d/word%d/' % (i, i)
        filename = 'word-%d-a%d.asp' % (i, j)
        url = root + subfolder + filename
        print('Downloading: ' + root + subfolder + filename)
        try:
            urlretrieve(root + subfolder + filename, filename)
        except:
            print('Not such file name', root + subfolder + filename)
            break
        j += 1

    j = 10
    while True:
        root = 'http://rirs3.royin.go.th/'
        subfolder = 'word%d/word%d/' % (i, i)
        filename = 'word-%d-a%d.asp' % (i, j)
        url = root + subfolder + filename
        print('Downloading: ' + root + subfolder + filename)
        try:
            urlretrieve(root + subfolder + filename, filename)
        except:
            print('Not such file name', root + subfolder + filename)
            break
        j += 1
