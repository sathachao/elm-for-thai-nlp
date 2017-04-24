from ThaiVectors.ELMTraining.elmmain import ELMModel
import numpy as np
from sklearn.model_selection import train_test_split

elmModel = ELMModel(False, 500, 2, 1, 500)
elmModel.load()

import csv
reader = csv.reader(open('../datasets/nnIO.all'), delimiter=' ')
readerLength = 2000

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

cm = elmModel.test(x_test, y_test)
print(cm[0][1] / (cm[0][0] + cm[0][1]))
print(cm[1][0] / (cm[1][0] + cm[1][1]))
