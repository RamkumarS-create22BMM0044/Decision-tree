# decision_tree_car_purchase.py

from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Dataset: Age, Income (0: Low, 1: High), BuysCar (0: No, 1: Yes)
data = {
    'Age': [25, 30, 45, 35, 22, 40],
    'Income': [0, 1, 1, 0, 0, 1],
    'BuysCar': [0, 1, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

X = df[['Age', 'Income']]
y = df['BuysCar']

model = DecisionTreeClassifier()
model.fit(X, y)

# Predict for new customer
prediction = model.predict([[28, 1]])
print("Prediction (1: Buys, 0: Doesn’t Buy):", prediction[0])
