from ThaiVectors.datasets.sentences import documents
import ThaiVectors.datasets.constants as const
import gensim, logging, random

def generateNGram(wordSeq, model, left=2, right=2, limit=50000):
    X = []  # Input
    Y = []  # Output
    zeroes = [0 * x for x in range(200)]

    file = open("nnIO.csv", "w")

    count = 0

    necount = 0
    netarget = 164669 # number of ne

    non_necount = 0
    non_netarget = 400000 - 164669

    modelDimension = len(model[wordSeq[0][0][0]].tolist())

    for document in wordSeq:
        for i in range(len(document)):
            if count >= limit:
                return [X, Y]
            count += 1
            x = []
            y = []
            for j in range(left, 0, -1):
                if i - j < 0:
                    # x += [const.BLANK]
                    x += [0.]*modelDimension
                    # y += [0]
                else:
                    # x += [document[i-j][0]]
                    x += model[document[i - j][0]].tolist()
                    # y += [document[i-j][1]]
            # x += [document[i][0]]
            x += model[document[i][0]].tolist()
            y += [document[i][1]]
            if y == [0]:
                if non_necount >= non_netarget:
                    count -= 1
                    continue
                if random.random() > 0.05:
                    count -= 1
                    continue
                non_necount += 1
            else:
                necount += 1
            for j in range(1, right + 1):
                if i + j >= len(document):
                    # x += [const.BLANK]
                    x += [0.]*modelDimension
                    # y += [0]
                else:
                    # x += [document[i + j][0]]
                    x += model[document[i + j][0]].tolist()
                    # y += [document[i + j][1]]
            # print(len(x))
            # print(x)
            X += [x]
            Y += [y]

            # Write to file


    return [X, Y]

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = gensim.models.Word2Vec.load('../thaiVectors/vectors_0.0.1.model')
print(model)

number_of_inst = 400000

nnIO = generateNGram(wordSeq=documents, model=model, limit=number_of_inst)

print("nnIO is generated...")

print(nnIO[1].count([0]))
print(nnIO[1].count([1]))

f = open('nnIO.train', 'w')
for i in range(int(number_of_inst*0.8)):
    f.write(' '.join(str(x) for x in nnIO[1][i]) + ' ' + ' '.join(str(x) for x in nnIO[0][i]) + '\n')
f.close()

f = open('nnIO.test', 'w')
for i in range(int(number_of_inst*0.8) + 1, number_of_inst):
    f.write(' '.join(str(x) for x in nnIO[1][i]) + ' ' + ' '.join(str(x) for x in nnIO[0][i]) + '\n')
f.close()


f = open('nnIO.all', 'w')
for i in range(number_of_inst):
    f.write(' '.join(str(x) for x in nnIO[1][i]) + ' ' + ' '.join(str(x) for x in nnIO[0][i]) + '\n')
f.close()

'''
f = open('nnIObp.train', 'w')
for i in range(number_of_inst):
    f.write(' ' + str(nnIO[1][i][0]) + ' ' + str(1 - nnIO[1][i][0]) + ' ' + ' '.join(str(x) for x in nnIO[0][i]) + '\n')
f.close()
'''



