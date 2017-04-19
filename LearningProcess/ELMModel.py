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
        print(confusion_matrix(y_true=np.argmax(xTest, axis=1), y_pred=np.argmax(yTest, axis=1)))


########Example for ELM
# iris = datasets.load_iris()
# 
# X = iris.data
# Y = np.zeros((len(iris.target), 3), dtype=np.int)
# 
# temp = iris.target
# 
# for i in range(len(temp)):
#     Y[i][temp[i]] = 1
# 
# 
# x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# 
# elmModel = hpelm.ELM(inputs=4, outputs=3, classification="c")
# 
# elmModel.add_neurons(number=20, func="sigm")
# elmModel.train(X=x_train, T=y_train)
# 
# y_predicted = elmModel.predict(x_test)
# 
# # y_predicted = y_predicted.argmax[1]
# # y_test = y_test.argmax[1]
# 
# print(confusion_matrix(y_true=np.argmax(y_test, axis=1), y_pred=np.argmax(y_predicted, axis=1)))
