import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('m.csv')
x = data.iloc[:, :-1].apply(LabelEncoder().fit_transform)
y = LabelEncoder().fit_transform(data.iloc[:, -1])

model = DecisionTreeClassifier().fit(x, y)

inp = pd.DataFrame([["Overcast", "Cool", "Normal", "Strong"]], columns=x.columns).apply(LabelEncoder().fit_transform)
pred = model.predict(inp)[0]
print(f"\nFor input {inp.iloc[0].tolist()}, the prediction is '{pred}'.")
