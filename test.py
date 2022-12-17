from simpnet import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

inputLayer = Layer(2)
# hiddenLayer = Layer(3)
outputLayer = Layer(2)
layers = [inputLayer,outputLayer]
activations = ['linear']
model:Network
x = np.arange(-1.0, 1.0, 0.1)
y = x
for i in range(len(x)):
    for j in range(len(y)):
        inputs = [x[i],y[j]]
        inputLayer = LoadInput(inputs,inputLayer,'linear')
        model = Link(layers,activations)
        prediction = Predict(model,inputs)
        output:int
        if prediction[0]>prediction[1]:
            output = 1
        else:
            output = 0
        if output==1:
            plt.scatter(x[i],y[j],c='green')
        else:
            plt.scatter(x[i],y[j],c='red')

plt.show()

