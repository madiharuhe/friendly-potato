import numpy as np

X = np.array([[2, 9], [1, 5], [3, 6]], dtype=float) / np.amax([[2, 9], [1, 5], [3, 6]], axis=0)
y = np.array([[92], [86], [89]], dtype=float) / 100

sigmoid = lambda x: 1 / (1 + np.exp(-x))
dsigmoid = lambda x: x * (1 - x)

epoch, lr = 5, 0.1
wh, bh = np.random.uniform(size=(2, 3)), np.random.uniform(size=(1, 3))
wout, bout = np.random.uniform(size=(3, 1)), np.random.uniform(size=(1, 1))

for i in range(epoch):
    hlayer_act = sigmoid(np.dot(X, wh) + bh)
    output = sigmoid(np.dot(hlayer_act, wout) + bout)
    d_output = (y - output) * dsigmoid(output)
    wh += X.T.dot(d_output.dot(wout.T) * dsigmoid(hlayer_act)) * lr
    wout += hlayer_act.T.dot(d_output) * lr
    print(f"Epoch {i+1}\nInput: {X}\nActual: {y}\nPredicted: {output}\n")
