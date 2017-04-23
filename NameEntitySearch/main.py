from tkinter import *
from tkinter import ttk

from ThaiVectors.ELMTraining.elmmain import ELMModel
from NameEntitySearch.tokerynx.tokenizian import Tokenizian
import gensim
import numpy as np

class NameEntitySearch(ttk.Frame):

    def __init__(self, isapp=True, name='nameentitysearch'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Name Entity Search')
        self.isapp = isapp
        self.text = None

        self.model = gensim.models.Word2Vec.load('thaivectors/vectors_0.0.1.model')
        self.tokenizer = Tokenizian(dictionary=list(self.model.vocab))
        self.elmModel = ELMModel(False, 500, 2, 1, 1000)
        self.elmModel.load('../ThaiVectors/ELMTraining/elmModel')

        self.create_widgets()

        self.prevText = ''

    def create_widgets(self):
        self.create_demo_panel()

    def create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP)

        self.txt_panel(demoPanel)
        self.search_panel(demoPanel)

    def reset_highlight(self):
        self.text.tag_remove('search', 0.0, END)

    def highlight_txt_at(self, start, end):
        self.text.tag_add('search', start, end)

    def txt_panel(self, parent):
        # create scrolled text widget
        txtFrame = ttk.Frame(self)
        txtFrame.pack(side=TOP, fill=BOTH, expand=Y)

        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.updateText(sv))

        self.text = Text(txtFrame, height=20, setgrid=True, wrap=WORD,
                    undo=True, pady=2, padx=3)
        xscroll = ttk.Scrollbar(txtFrame, command=self.text.xview,
                                orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(txtFrame, command=self.text.yview,
                                orient=VERTICAL)
        self.text.configure(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set, font=("Courier", 16))

        # configure 'search' style tag
        self.text.tag_configure('search', background='yellow')

        # position in frame and set resize constraints
        self.text.grid(row=0, column=0, sticky=NSEW)
        yscroll.grid(row=0, column=1, sticky=NSEW)
        txtFrame.rowconfigure(0, weight=1)
        txtFrame.columnconfigure(0, weight=1)

        # add text to scrolled text widget
        # txt = 'This is a test'
        #
        # self.text.insert(END, txt)

        # self.text.bind('<KeyRelease>', lambda evt: self.updateText(evt))
        self.text.event_add('<<Paste>>', '<Control-v>')
        self.text.event_add('<<Copy>>', '<Control-c>')

    def search_panel(self, parent):
        f = ttk.Frame(parent)
        f.pack(side=TOP)

        btn = ttk.Button(text='Search', command=self.updateText)
        btn.pack(in_=f, side=TOP, padx=10, pady=10)

    def updateText(self, evt=None):
        self.reset_highlight()
        raw_text = self.text.get('1.0', 'end-1c')
        if raw_text == self.prevText:
            return
        self.prevText = raw_text

        raw_texts = raw_text.split('\n')
        self.searchingOffset = 0 # increase by raw_text for highlight newline correctly (line counter)
        for raw_text in raw_texts:
            self.searchingOffset += 1
            tokenized = self.tokenize(raw_text)
            print(tokenized)

            if len(tokenized) >= 1 and len(tokenized[0]) >= 1:
                document = tokenized[0]
            else:
                continue

            modelDimension = len(self.model[document[0]].tolist())
            X = [] # Input
            x = []
            left = 2
            right = 2
            self.tokenizedText = document
            for i in range(len(document)):
                x = []
                for j in range(left, 0, -1):
                    if i - j < 0:
                        # x += [const.BLANK]
                        x += [0.]*modelDimension
                        # y += [0]
                    else:
                        # x += [document[i-j][0]]
                        x += self.model[document[i - j]].tolist()
                        # y += [document[i-j][1]]
                # x += [document[i][0]]
                x += self.model[document[i]].tolist()
                for j in range(1, right + 1):
                    if i + j >= len(document):
                        # x += [const.BLANK]
                        x += [0.]*modelDimension
                        # y += [0]
                    else:
                        # x += [document[i + j][0]]
                        x += self.model[document[i + j]].tolist()
                        # y += [document[i + j][1]]
                # print(len(x))
                # print(x)
                X += [x]

            self.checkAllNameEntities(X)



    def tokenize(self, text):
        self.tokenizer.setText(text)
        return self.tokenizer.longestMatchingTokenizations

    def checkAllNameEntities(self, X):
        i = 0
        for x in X:
            y = self.checkNameEntity(x)
            if y == 1:
                self.highlightText(i)
            i += 1

    def checkNameEntity(self, x):
        X = np.asarray(x)
        X = X[np.newaxis]
        yPredicted = self.elmModel.model.predict(X)
        return np.argmax(yPredicted)

    def highlightText(self, idx):
        startIdx = 0
        for i in range(0, idx):
            startIdx += len(self.tokenizedText[i])
        endIdx = startIdx + len(self.tokenizedText[idx])
        self.highlight_txt_at(str(self.searchingOffset) + '.' + str(startIdx),
                              str(self.searchingOffset) + '.' + str(endIdx))
        print('HL from', startIdx, 'to', endIdx)

if __name__ == '__main__':
    NameEntitySearch().mainloop()
