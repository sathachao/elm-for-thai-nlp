from urllib.request import urlretrieve

noText = []

for i in range(1, 47):

    root = 'http://rirs3.royin.go.th/'
    subfolder = 'word%d/' % i
    filename = 'word%d.txt' % i
    url = root + subfolder + filename
    print('Downloading: ' + root + subfolder + filename)
    try:
        urlretrieve(root + subfolder + filename, filename)
    except:
        print(url + ' cannot be downloaded')
        noText += [i,]


for i in noText:
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
            break
        j += 1
