from tokerynx.allList import symbollist
from tokerynx.allList import wordlist

englishcharlist = list(chr(i) for i in range(ord('A'),ord('Z')+1)) + list(chr(i) for i in range(ord('a'),ord('z')+1))
numbercharlist = list(chr(i) for i in range(ord('0'),ord('9')+1))

nonacceptcharlist = englishcharlist + numbercharlist

# usage:
# t = Tokenizian(sentence)
# print(t.longestMatchingTokenizations)

class Tokenizian:

    def __init__(self, text='', dictionary=wordlist):
        self.dictionary = dictionary
        self.setText(text)

    def setText(self, text):
        self.originalText = text
        self.genPossibleTokenizationsIdx()
        self.genPossibleTokenizations()

    def genPossibleTokenizations(self):
        self.possibleTokenizations = []
        self.longestMatchingTokenizations = []
        sentenceLength = len(self.originalText)
        shortestPathLength = min(list(len(tokenization) for tokenization in self.possibleTokenizationsIdx) + [sentenceLength,])
        for tokenization in self.possibleTokenizationsIdx:
            text = self.originalText
            for idx in tokenization[::-1]:
                text = text[:idx] + '|' + text[idx:]
            text = text.split('|')[1:-1]
            self.possibleTokenizations.extend([text])
            if len(tokenization) == shortestPathLength:
                self.longestMatchingTokenizations.extend([text])

    def genPossibleTokenizationsIdx(self):
        text = self.originalText
        sentenceLength = len(text)
        startIdxQueue = {0}
        maxTraversedIdx = 0
        graph = {}
        unknownIdx = []
        while len(startIdxQueue) > 0:
            # idx = min(startIdxQueue)  # uncomment this to gen all path
            idx = max(startIdxQueue)    # get path with optimal time
            maxTraversedIdx = max(maxTraversedIdx, idx)
            if maxTraversedIdx >= sentenceLength:
                break
            startIdxQueue.remove(idx)
            possibleMoves = [item+idx for item in self.getPossibleMoves(text[idx:])]
            graph[idx] = possibleMoves
            startIdxQueue = startIdxQueue.union(set(possibleMoves))
            """
            # Unknown word condition
            if len(startIdxQueue) <= 0:
                if maxTraversedIdx < sentenceLength:
                    startIdxQueue.add(maxTraversedIdx+1)
                    graph[maxTraversedIdx] = [maxTraversedIdx+1]
                    unknownIdx += (maxTraversedIdx,)
                    continue
                break
            """
        self.graph = graph
        self.unknownIdx = unknownIdx
        if graph == {}:
            self.possibleTokenizationsIdx = [()]
            return
        self.possibleTokenizationsIdx = list(self.getAllPaths(graph, 0, sentenceLength))

    def getPossibleMoves(self, s):
        if s[:1] in symbollist:
            return [1]
        possibleMoves = []
        sIdx = 0
        eIdx = 1
        possibleWords = list(filter(lambda item: item[sIdx:eIdx] == s[sIdx:eIdx], self.dictionary))
        possibleWords.sort()
        while len(possibleWords) > 0:
            if eIdx > len(s):
                break
            if s[sIdx:eIdx] == possibleWords[0]:
                possibleMoves.append(eIdx)
                possibleWords.remove(possibleWords[0])
            eIdx += 1
            possibleWords = list(filter(lambda item: item[sIdx:eIdx] == s[sIdx:eIdx], possibleWords))
        return possibleMoves

    def getAllPaths(self, graph, sNode, eNode, currentPath=()):
        if sNode in graph:
            for child in graph[sNode]:
                if child == eNode:
                    yield currentPath+(sNode,)+(eNode,)
                else:
                    for path in self.getAllPaths(graph, child, eNode, currentPath+(sNode,)):
                        yield path

    def printAllInfo(self):
        print('Original Text:', self.originalText)
        print('Length of Original Text:', len(self.originalText))
        print('Graph:', self.graph)
        print('Unknown Index:', self.unknownIdx)
        for idx in self.unknownIdx:
            print(self.originalText[idx])
        print('Possible Tokenizations:', self.possibleTokenizationsIdx)
        for tokenization in self.possibleTokenizations:
            print(tokenization)
        print('Longest Matching Tokenizations:', self.longestMatchingTokenizations)
        for tokenization in self.longestMatchingTokenizations:
            print(tokenization)




