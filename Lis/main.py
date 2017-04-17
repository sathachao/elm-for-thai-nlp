import sys

from Tokerynx.tokenizian import Tokenizian
import instructions
import gensim

class Lis:
    def __init__(self):
        self.actions = instructions.actions
        self.components = instructions.components

        # create thaivectors folder and put the model at root
        self.model = gensim.models.Word2Vec.load('ThaiVectors/vectors_0.0.1.model')

        self.tokenizer = Tokenizian(dictionary=list(self.model.vocab))
        self.action = None
        self.component = None


    def exec(self, raw_text):
        if raw_text in self.getSimilarWords('จบ'):
            return 1
        elif raw_text[:4] == 'lsdo':
            try:
                eval(raw_text[5:])
            except:
                print(sys.exc_info()[0])
            return 0

        tokenized = self.tokenize(raw_text)
        if len(tokenized) == 0:
            print('ไม่รู้จัก "%s"' % raw_text)
        else:
            tokenized = tokenized[0]
            if self.action == None:
                self.action = self.getAction(tokenized)
            if self.component == None:
                self.component = self.getComponent(tokenized)
            if self.action == None and self.component == None:
                print('ไม่เข้าใจ "%s"' % raw_text)
            elif self.action == None:
                print('จะให้ทำอะไรกับ%s' % self.component)
            elif self.component == None:
                print('จะให้%sอะไร' % self.action)
            else:
                try:
                    instruction = '%s.%s()' % (self.components[self.component], self.actions[self.action])
                    print('DEBUG:', 'Executing', instruction)
                    eval(instruction)
                except:
                    print('%sไม่สามารถ%sได้' % (self.component, self.action))
                finally:
                    self.action = None
                    self.component = None
        return 0

    def tokenize(self, text):
        self.tokenizer.setText(text)
        return self.tokenizer.longestMatchingTokenizations

    def getAction(self, words):
        result = None
        max_sim = -1
        for word in words:
            for action in self.actions:
                sim = self.model.similarity(word, action)
                if sim >= 0.5 and max_sim < sim:
                    result = action
                    max_sim = sim
        return result

    def getComponent(self, words):
        result = None
        max_sim = -1
        for word in words:
            for component in self.components:
                sim = self.model.similarity(word, component)
                if sim >= 0.5 and max_sim < sim:
                    result = component
                    max_sim = sim
        return result

    def getSimilarWords(self, word):
        # TODO:
        return [word] + []

if __name__ == '__main__':
    print('リズ starts operating')

    lis = Lis()
    terminate_flag = 0
    while terminate_flag == 0:
        raw_text = input('>> ') # enter 'lsdo command' for eval(command)
        terminate_flag = lis.exec(raw_text)

    print('リズ terminated')
