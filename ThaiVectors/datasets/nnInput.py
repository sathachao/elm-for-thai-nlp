from ThaiVectors.datasets.sentences import documents
import ThaiVectors.datasets.constants as const
import gensim, logging

def generateNGram(wordSeq, model, left=2, right=2, limit=50000):
    X = []  # Input
    Y = []  # Output
    zeroes = [0 * x for x in range(200)]

    file = open("nnIO.csv", "w")

    count = 0

    for document in wordSeq:
        for i in range(len(document)):
            if count > limit:
                return [X, Y]
            count += 1
            x = []
            y = []
            for j in range(left, 0, -1):
                if i - j < 0:
                    # x += [const.BLANK]
                    x += [zeroes]
                    y += [0]
                else:
                    # x += [document[i-j][0]]
                    x += model[document[i - j][0]].tolist()
                    y += [document[i-j][1]]
            # x += [document[i][0]]
            x += model[document[i][0]].tolist()
            y += [document[i][1]]
            for j in range(1, right + 1):
                if i + j >= len(document):
                    # x += [const.BLANK]
                    x += [zeroes]
                    y += [0]
                else:
                    # x += [document[i + j][0]]
                    x += model[document[i + j][0]].tolist()
                    y += [document[i + j][1]]

            X += [x]
            Y += [y]
    return [X, Y]

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = gensim.models.Word2Vec.load('../thaiVectors/vectors_0.0.1.model')

nnIO = generateNGram(wordSeq=documents, model=model)

print("nnIO is generated...")
