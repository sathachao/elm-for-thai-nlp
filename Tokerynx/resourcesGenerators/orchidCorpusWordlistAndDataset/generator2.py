from dictionaries.royin2542Wordlist import wordlist

import re
file = open('orchid97.crp.utf', mode='r+', encoding='utf-8')
data = file.read()
data = re.findall(r'([#][0-9]+[\n](?:.*?[\n]*)*?\/\/\n(?:.*?[\n]*)*?\/\/)', data)

datasets = {}
validFlag = True

for dataset in data:
    validFlag = True
    dataset = dataset.split('\n')
    idx = 1
    originalText = ''
    tokenizedText = '|'
    if dataset[idx][:2] == '%E':
        continue
    while dataset[idx][-2:] == '//' or dataset[idx][-2:] == '\\\\':
        originalText += dataset[idx][:-2]
        idx += 1
    # print(dataset, len(dataset[idx:-1]))
    if len(dataset[idx:-1]) > 8:
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
        elif text[:1] == '<':
            # print(dataset, text, 'Warning: text[:1] == \'<\', validFlag set to False')
            validFlag = False
            break
        elif text == 'ถี่':
            # print(dataset, text, 'Warning: text[:1] == \'<\', validFlag set to False')
            validFlag = False
            break
        elif len(text) <= 1 and not text.isdigit():
            # print(dataset, text, 'Warning: len(text) <= 1 and not text.isdigit(), validFlag set to False')
            validFlag = False
            break
        elif text not in wordlist:
            # print(dataset, text, 'Warning: text not in wordlist, validFlag set to False')
            validFlag = False
            break
        tokenizedText += text
        tokenizedText += '|'
        idx += 1
    if not validFlag:
        continue
    datasets[originalText] = tokenizedText
    # print(originalText)
    # print(tokenizedText)
    # print('===================================')


print('Total number of dataset: ', len(datasets))

file = open('../../datasets/orchidCorpusDataset.py', mode='w+', encoding='utf-8')
file.write('dataset = ' + str(datasets))

