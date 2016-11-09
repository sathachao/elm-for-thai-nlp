import re
file = open('orchid97.crp.utf', mode='r+', encoding='utf-8')
data = file.read()
data = re.findall(r'([#][0-9]+[\n](?:.*?[\n]*)*?\/\/\n(?:.*?[\n]*)*?\/\/)', data)

wordlist = set()
# data = data[:3]
datasets = {}
validFlag = True

for dataset in data:
    validFlag = True
    dataset = dataset.split('\n')
    idx = 1
    originalText = ''
    tokenizedText = '|'
    print(dataset)
    if dataset[idx][:2] == '%E':
        continue
    while dataset[idx][-2:] == '//' or dataset[idx][-2:] == '\\\\':
        originalText += dataset[idx][:-2]
        idx += 1
    if len(originalText) > 50:
        continue
    while dataset[idx] != '//':
        text = re.findall(r'.*[\/@]', dataset[idx])[0][:-1]
        if text == '<space>':
            text = ' '
        elif text == '<full_stop>':
            text = '.'
        elif text == '<comma>':
            text = ','
        elif text == '<slash>':
            text = '/'
        elif text == '<left_parenthesis>':
            text = '('
        elif text == '<right_parenthesis>':
            text = ')'
        elif text == '<equal>':
            text = '='
        elif text == '<plus>':
            text = '+'
        elif text == '<minus>':
            text = '-'
        elif text == '<colon>':
            text = ':'
        elif text == '<semi_colon>':
            text = ';'
        elif text == '<apostrophe>':
            text = '\''
        elif text == '<quotation>':
            text = '"'
        elif text == '<dollar>':
            text = '$'
        elif text == '<question_mark>':
            text = '?'
        elif text == '<ampersand>':
            text = '&'
        elif text == '<number>':
            text = '#'
        elif text == '<asterisk>':
            text = '*'
        elif text == '<greater_than>':
            text = '>'
        elif text == '<less_than>':
            text = '<'
        elif text == '<circumflex_accent>':
            text = '^'
        elif text == '<exclamation>':
            text = '!'
        elif text == '<left_curly_bracket>':
            text = '{'
        elif text == '<right_curly_bracket>':
            text = '}'
        elif text == '<at_mark>':
            text = '@'
        elif text == '<at_mark>PUNC':
            text = '@'
        elif text == '<at_mark>FIXN':
            text = '@'
        elif text == '<at_mark>NCMN':
             text = '@'
        elif text[:1] == '<' or (len(text) <= 1 and not text.isdigit()):
            print(dataset, text, 'validFlag set to False')
            validFlag = False
            break
        else:
            wordlist.add(text)
        tokenizedText += text
        tokenizedText += '|'
        idx += 1
    if not validFlag:
        continue
    datasets[originalText] = tokenizedText
    # print(originalText)
    # print(tokenizedText)
    # print('===================================')

wordlist = sorted(wordlist)

print('Total number of dataset: ', len(datasets))
print('Total number of words: ', len(wordlist))

file = open('../../datasets/orchidCorpusDataset.py', mode='w+', encoding='utf-8')
file.write('datasets = ' + str(datasets))

file = open('../../dictionaries/orchidCorpusWordlist.py', mode='w+', encoding='utf-8')
file.write('wordlist = ' + str(wordlist))
for i in wordlist:
    if ' ' in i:
        print(i)
print('These could be invalid words')
