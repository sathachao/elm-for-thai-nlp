import numpy as np
import tensorflow as tf

class BackpropagationModel:
    def __init__(self, sequenceLength, numClasses, dimension, numHiddenNodes):
        self.x = tf.placeholder(tf.float32, [None, sequenceLength * dimension])
        self.yhat = tf.placeholder(tf.float32, [None, numClasses])

        # Initialize weights
        self.W1 = tf.Variable(tf.random_uniform([sequenceLength * dimension, numHiddenNodes], minval=-0.001, maxval=0.001))
        self.b = tf.Variable(tf.random_uniform([numHiddenNodes], minval=-0.001, maxval=0.001))
        self.W2 = tf.Variable(tf.random_uniform([numHiddenNodes, numClasses], minval=-0.001, maxval=0.001))

        # Join layers
        self.hidden1 = tf.nn.tanh(tf.matmul(self.x, self.W1) + self.b)
        self.y = tf.nn.tanh(tf.matmul(self.hidden1, self.W2))

        self.costFn = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=self.y, labels=self.yhat))
        # costFn = tf.reduce_mean(-tf.reduce_sum(yhat * tf.log(y)), reduction_indices=[1])
        self.updateFn = tf.train.GradientDescentOptimizer(0.05).minimize(self.costFn)

        self.sess = tf.Session()
        init = tf.global_variables_initializer()
        self.sess.run(init)

    def train(self, xTrain, yTrain):

        currentLoss = pow(2, 63) - 2
        newLoss = pow(2, 63) - 1

        for epoch in range(1000):
            # if abs(currentLoss - newLoss) <= 0:
            #     break
            # else:
            #     currentLoss = newLoss
            for i in range(len(xTrain)):
                fdict = {self.x: xTrain, self.yhat: yTrain}
                temp = self.sess.run(self.updateFn, feed_dict=fdict)
                # a, b, newLoss = sess.run(updateFn, feed_dict={x: xTrain, yhat: yTrain})

    def test(self, xTest, yTest):
        correct_prediction = tf.equal(tf.argmax(self.y, 1), tf.argmax(self.yhat, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        fdict = {self.x: xTest, self.yhat: yTest}
        print(self.sess.run(accuracy, feed_dict=fdict))