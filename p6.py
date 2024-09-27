import csv

with open("enjoysport.csv") as f:
    data = list(csv.reader(f))

s = data[1][:-1]
g = [["?" for _ in s] for _ in s]

for example in data[1:]:
    attrs, label = example[:-1], example[-1].lower()
    if label == "yes":
        s = [s[i] if s[i] == attrs[i] else "?" for i in range(len(s))]
    elif label == "no":
        for i, val in enumerate(attrs):
            if s[i] != val:
                g[i][i] = s[i]

gh = [h for h in g if any(val != "?" for val in h)]
print(f"Specific Hypothesis: {s}")
print(f"General Hypothesis: {gh}")
