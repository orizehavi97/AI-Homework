import math
from fastapi import FastAPI
from sklearn.linear_model import LogisticRegression
import numpy as np

app = FastAPI(title="Logistic Regression via GET /logistic/predict")

# --- Train a simple model at startup ---
X_train = np.array([[0], [1], [2], [3], [4], [5]], dtype=float)
y_train = np.array([0, 0, 0, 1, 1, 1], dtype=float)

model = LogisticRegression()
model.fit(X_train, y_train)

# Coefficients
b0 = model.intercept_[0]
b1 = model.coef_[0][0]


@app.get("/logistic/predict")
def get_prediction(x: float = 0):
    z = b0 + b1 * x
    probability = 1 / (1 + math.exp(-z))
    result = float(model.predict(np.array([[x]], dtype=float))[0])
    return {
        "x": x,
        "probability": probability,
        "y_pred": result
    }
