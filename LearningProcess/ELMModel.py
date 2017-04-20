import hpelm
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


class ELMModel:
    # Need one-hot vector for output classes
    def __init__(self, sequenceLength, numClasses, dimension, numHiddenNodes):
        self.model = hpelm.ELM(inputs=sequenceLength*dimension, outputs=numClasses, classification="c")
        self.model.add_neurons(number=numHiddenNodes, func="tanh")

    def train(self, xTrain, yTrain):
        self.model.train(X=xTrain, T=yTrain)

    def test(self, xTest, yTest):
        yPredicted = self.model.predict(xTest)
        print(confusion_matrix(y_true=np.argmax(yTest, axis=1), y_pred=np.argmax(yPredicted, axis=1)))

########Example for ELM
iris = datasets.load_iris()

X = iris.data
Y = np.zeros((len(iris.target), 3), dtype=np.int)

temp = iris.target

for i in range(len(temp)):
    Y[i][temp[i]] = 1


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

elmModel = ELMModel(4, 3, 1, 20)
elmModel.train(x_train, y_train)
elmModel.test(x_test, y_test)
