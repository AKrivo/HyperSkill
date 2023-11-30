from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


param_grid = {
    "n_neighbors": [3, 5, 10, 13],
    "weights": ["uniform", "distance"],
    "algorithm": ["auto", "ball_tree", "kd_tree"],
}

grid_search = GridSearchCV(
    estimator=KNeighborsRegressor(), param_grid=param_grid, n_jobs=-1
)
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_   # the optimal parameter combination
best_score = grid_search.best_score_     # mean cross-val score of the best_estimator
best_model = grid_search.best_estimator_ # the estimator with the highest score

test_score = grid_search.score(X_test, y_test)

df = pd.DataFrame(grid_search.cv_results_)