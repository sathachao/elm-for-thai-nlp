import numpy as np
import tensorflow as tf
import LearningProcess.BackpropagationModel as Backprop
import random

testModel = Backprop.BackpropagationModel(sequenceLength=3, numClasses=2,dimension=200,numHiddenNodes=100)

l = [[random.random() for i in range(3*200)] for j in range(4)]

dummyX = np.array(l, np.float32)
dummyY = np.array([[0,1], [0,1], [1,0], [1,0]], np.float32)

testModel.train(xTrain=dummyX, yTrain=dummyY)