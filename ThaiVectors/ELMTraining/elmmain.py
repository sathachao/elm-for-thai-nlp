import hpelm
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


class ELMModel:
    # Need one-hot vector for output classes
    def __init__(self, isEmpty, sequenceLength, numClasses, dimension, numHiddenNodes):
        self.model = hpelm.ELM(inputs=sequenceLength*dimension, outputs=numClasses, classification="c")
        self.model.add_neurons(number=numHiddenNodes, func="tanh")

    def train(self, xTrain, yTrain):
        self.model.train(X=xTrain, T=yTrain)

    def test(self, xTest, yTest):
        yPredicted = self.model.predict(xTest)
        cm = confusion_matrix(y_true=np.argmax(yTest, axis=1), y_pred=np.argmax(yPredicted, axis=1))
        print(cm)
        return cm

    def save(self, fname='elmModel'):
        self.model.save(fname)

    def load(self, fname='elmModel'):
        self.model.load(fname)

if __name__ == '__main__':
    ########Example for ELM
    import csv
    reader = csv.reader(open('../datasets/nnIO.all'), delimiter=' ')
    readerLength = 10000

    X = np.zeros((readerLength, 500), dtype=np.float)
    Y = np.zeros((readerLength, 2), dtype=np.int)

    i = 0
    for row in reader:
        Y[i][eval(row[0])] = 1
        for j in range(1, 501):
            X[i][j-1] = eval(row[j])
        # print(row)
        # print(Y[i])
        # print(X[i])
        i += 1
        if i >= readerLength:
            break

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

    elmModel = ELMModel(False, 500, 2, 1, 1000)
    elmModel.train(x_train, y_train)
    elmModel.test(x_train, y_train)
    cm = elmModel.test(x_test, y_test)
    print(cm[0][1] / (cm[0][0] + cm[0][1]))
    print(cm[1][0] / (cm[1][0] + cm[1][1]))

    elmModel.save()
