import numpy as np
import pandas as pd
import os
import requests
from matplotlib import pyplot as plt


# scroll to the bottom to start coding your solution


def one_hot(data: np.ndarray) -> np.ndarray:
    y_train = np.zeros((data.size, data.max() + 1))
    rows = np.arange(data.size)
    y_train[rows, data] = 1
    return y_train


def plot(loss_history: list, accuracy_history: list, filename='plot'):
    # function to visualize learning process at stage 4

    n_epochs = len(loss_history)

    plt.figure(figsize=(20, 10))
    plt.subplot(1, 2, 1)
    plt.plot(loss_history)

    plt.xlabel('Epoch number')
    plt.ylabel('Loss')
    plt.xticks(np.arange(0, n_epochs, 4))
    plt.title('Loss on train dataframe from epoch')
    plt.grid()

    plt.subplot(1, 2, 2)
    plt.plot(accuracy_history)

    plt.xlabel('Epoch number')
    plt.ylabel('Accuracy')
    plt.xticks(np.arange(0, n_epochs, 4))
    plt.title('Accuracy on test dataframe from epoch')
    plt.grid()

    plt.savefig(f'{filename}.png')


if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('fashion-mnist_train.csv' not in os.listdir('../Data') and
            'fashion-mnist_test.csv' not in os.listdir('../Data')):
        print('Train dataset loading.')
        url = "https://www.dropbox.com/s/5vg67ndkth17mvc/fashion-mnist_train.csv?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/fashion-mnist_train.csv', 'wb').write(r.content)
        print('Loaded.')

        print('Test dataset loading.')
        url = "https://www.dropbox.com/s/9bj5a14unl5os6a/fashion-mnist_test.csv?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/fashion-mnist_test.csv', 'wb').write(r.content)
        print('Loaded.')

    # Read train, test data.
    raw_train = pd.read_csv('../Data/fashion-mnist_train.csv')
    raw_test = pd.read_csv('../Data/fashion-mnist_test.csv')

    X_train = raw_train[raw_train.columns[1:]].values
    X_test = raw_test[raw_test.columns[1:]].values

    y_train = one_hot(raw_train['label'].values)
    y_test = one_hot(raw_test['label'].values)

    # write your code here


# Stage 1/7

def scale(X_train, X_test):
    X_tr = X_train / X_train.max(axis=1, keepdims=True)
    X_te = X_test / X_test.max(axis=1, keepdims=True)
    return X_tr, X_te


def xavier(n_in, n_out):
    part = n_in + n_out
    bound = (np.sqrt(6)) / (np.sqrt(part))
    w = np.random.uniform(-bound, bound, (n_in, n_out))
    return w


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X_trainS, X_testS = scale(X_train, X_test)


#
def mse(pred, real):
    return np.mean((pred - real) ** 2)


def dmse(pred, real):
    return 2 * (pred - real)


def dsigm(x):
    return sigmoid(x) * (1 - sigmoid(x))


#
# Stage 2/7

class OneLayerNeural:
    def __init__(self, n_features, n_classes):
        self.w = xavier(n_features, n_classes)
        self.b = np.zeros_like(xavier(1, n_classes))
        self.forw = None
        # Initiate weights and biases using Xavier

    def forward(self, X):
        self.forw = sigmoid(np.dot(X, self.w) + self.b)
        return self.forw

    def backprop(self, X, y, alpha):
        activation = self.forw
        delta = dmse(activation, y) * dsigm((np.dot(X, self.w) + self.b))
        cw = np.dot(X.transpose(), delta)
        #cb = np.sum(delta, axis=0, keepdims=True)
        cb = delta
        #     # Updating your weights and biases.
        self.w = self.w - alpha * cw
        self.b = self.b - alpha * cb
        # Calculate and return the loss for monitoring
        loss = mse(self.forward(X), y)
        return loss

rows, n_featuresX = X_trainS.shape
n_classesX = 10
test = OneLayerNeural(n_featuresX, n_classesX)
a = test.forward(X_trainS[:2, :])
b = test.backprop(X_trainS[:2, :], y_train[:2, :], 0.1)
# d = test.forward(X_trainS[:2, :])
# c = mse(d, y_train[:2, :])


# Stage 3/7.flatten().tolist()

arr1 = np.array([-1, 0, 1, 2])
arr2 = np.array([4, 3, 2, 1])

#print(a1, b)
print(mse(arr1, arr2).flatten().tolist(), dmse(arr1, arr2).flatten().tolist(), dsigm(arr1).flatten().tolist(), b.flatten().tolist())
