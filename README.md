# 🚗 Car Purchase Prediction using Decision Tree Classifier

This project demonstrates a basic use of the **Decision Tree Classifier** to predict whether a person is likely to buy a car based on their **age** and **income level**.

---

## 📊 Dataset

A small dummy dataset is used to train the model:

| Age | Income (0: Low, 1: High) | BuysCar (0: No, 1: Yes) |
|-----|--------------------------|--------------------------|
| 25  | 0                        | 0                        |
| 30  | 1                        | 1                        |
| 45  | 1                        | 1                        |
| 35  | 0                        | 0                        |
| 22  | 0                        | 0                        |
| 40  | 1                        | 1                        |

---

## 🧠 Model

- **Algorithm:** Decision Tree Classifier
- **Library:** `scikit-learn`
- **Features:** `Age`, `Income`
- **Target:** `BuysCar`

---

## 🧪 Prediction

The model is trained to predict whether a 28-year-old person with **high income** will buy a car:

```python
prediction = model.predict([[28, 1]])
print("Prediction (1: Buys, 0: Doesn’t Buy):", prediction[0])
Prediction (1: Buys, 0: Doesn’t Buy): 1
