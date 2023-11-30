# write your code here
import numpy as np
import pandas as pd
import tensorflow as tf
import keras
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import GridSearchCV

# tf.keras.datasets.mnist.load_data(path="mnist.npz")

# Stage 1/5
# Import datasets. Reshape and prepare.

(x_train, y_train), (x_test_, y_test_) = keras.datasets.mnist.load_data()
x_train = np.reshape(x_train, [x_train.shape[0], -1])

# print(f"Classes: {np.unique(y_train)} "
#       f"\nFeatures' shape: {x_train.shape}"
#       f" \nTarget's shape: {y_train.shape}"
#       f"\nmin: {x_train.min()}, max: {x_train.max()}")


# Stage 2/5
size = 6000
X_train, X_test, y_train, y_test = train_test_split(x_train[:size], y_train[:size], test_size=0.3, random_state=40)
s = pd.Series(y_train)

# print(f"x_train shape: {X_train.shape} "
#       f"\nx_test shape: {X_test.shape}"
#       f" \ny_train shape: {y_train.shape}"
#       f"\ny_test shape: {y_test.shape} "
#       f"\nProportion of samples per class in train set: \n{s.value_counts(normalize=True)}")

# Stage 3/5

KN = KNeighborsClassifier()
DT = tree.DecisionTreeClassifier()
LR = LogisticRegression(random_state=40)
RF = RandomForestClassifier(random_state=40)

models = [KN, DT, LR, RF]
models_ = ["KNeighborsClassifier", "DecisionTreeClassifier", "LogisticRegression", "RandomForestClassifier"]


def fit_predict_eval(model, features_train, features_test, target_train, target_test, prin=True):
    # here you fit the model
    model.fit(features_train, target_train)
    # make a prediction
    pred = model.predict(features_test)
    # calculate accuracy and save it to score
    score = model.score(features_test, target_test)
    if prin:
        print(f'Model: {model}\nAccuracy: {score}\n')
    return score


# def test(models, features_train, features_test, target_train, target_test, prin=True):
#     scor = []
#     for model in models:
#         a = fit_predict_eval(
#             model=model,
#             features_train=features_train,
#             features_test=features_test,
#             target_train=target_train,
#             target_test=target_test,
#             prin=prin)
#         scor.append(a)
#     return scor


#scores = test(models, X_train, X_test, y_train, y_test, prin=False)
# print(f'The answer to the question: {models_[scores.index(max(scores))]} - {max(scores)}')

# Stage 4/5

N_X_train, N_X_test = Normalizer().transform(X_train), Normalizer().transform(X_test)
# N_scores = test(models, N_X_train, N_X_test, y_train, y_test)
comp = 0
# for score, N_score in zip(scores, N_scores):
#     if N_score > score:
#         comp += 1
# if comp >= comp/len(scores):
#     comp = "yes"
# else:
#     comp = "no"
#
# answerM = []
# answerV = []
# for i in range(2):
#     answerM.append(models_[N_scores.index(max(N_scores))])
#     answerV.append(max(N_scores))
#     N_scores.pop(i)
#     models_.pop(i)
#
# print(f"The answer to the 1st question: {comp}")
#
# print(f'The answer to the 2nd question: {answerM[0]}-{answerV[0].round(3)},'
#       f' {answerM[1]}-{answerV[1].round(3)}')

# Stage 5/5

KN_param = {'n_neighbors': [3, 4],
            'weights': ['uniform', 'distance'],
            'algorithm': ['auto', 'brute']
            }
RF_param = {'n_estimators': [300, 500],
            'max_features': ['sqrt', 'log2'],
            'class_weight': ['balanced', 'balanced_subsample']
            }
# Grid search for KN model
grid_search_KN = GridSearchCV(estimator=KN, param_grid=KN_param, n_jobs=-1)

grid_search_KN.fit(N_X_train, y_train)
best_params = grid_search_KN.best_params_  # the optimal parameter combination
best_score = grid_search_KN.best_score_  # mean cross-val score of the best_estimator
best_model = grid_search_KN.best_estimator_  # the estimator with the highest score

test_score_KN = grid_search_KN.score(N_X_test, y_test).round(3)
# Grid search for RF model
grid_search_RF = GridSearchCV(estimator=RF, param_grid=RF_param, n_jobs=-1)
grid_search_RF.fit(N_X_train, y_train)
test_score_RF = grid_search_RF.score(N_X_test, y_test).round(3)

print(f"K-nearest neighbours algorithm, \n"
      f"best estimator: {grid_search_KN.best_estimator_} \n"
      f"accuracy: {test_score_KN}")
print(f"Random forest algorithm, \n"
      f"best estimator: {grid_search_RF.best_estimator_} \n"
      f"accuracy: {test_score_RF}")