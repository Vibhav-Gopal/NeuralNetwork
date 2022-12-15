import random
from math import exp

class SizeMismatchError(Exception):
    "Number of inputs specified and Number of inputs provided don't match, or the number of input nodes and the size of the input data don't match"

class Node:
    def __init__(self,inValue):
        self.inValue = inValue


class Layer:
    
    def __init__(self, numberofNodes):
        self.nodes = []
        for i in range(numberofNodes):
            self.nodes.append(Node(i))

class Connection:
    def __init__(self):
        self.weight = random.random()/10
        self.bias = (random.random())/10

class Network:
    def __init__(self,layers:list,connections:list):
        self.layers = layers
        self.connections = connections
def Activation( value:float, name:str='linear'):
    if name=='linear':
        return ActivationLinear(value)
    elif name=='sigmoid':
        return ActivationSigmoid(value)

def ActivationLinear(inValue:float):
    return inValue
    
def ActivationSigmoid(inValue:float):
    return 1/(1+exp(-inValue))

def Link(layers:list,activations:list):
    connections=[]
    for i in range(1,len(layers)):
        layer_connections = []
        layer1 = layers[i-1]
        layer2 = layers[i]
        activation = activations[i-1]
        for j in range(len(layer2.nodes)):
            weightedInput = 0
            to_node = layer2.nodes[j]
            for k in range(len(layer1.nodes)):
                from_node = layer1.nodes[k]
                layer_connections.append(Connection())
                link = layer_connections[-1]
                weightedInput += from_node.inValue*link.weight + link.bias
            to_node.inValue = Activation(weightedInput,activation)
        connections.append(layer_connections)
    return Network(layers,connections)

def LoadInput(numberofInputs:int, inputs:list, inputLayer:Layer,activation:str):
    if numberofInputs!=len(inputs) or len(inputs)!=len(inputLayer.nodes): 
        raise SizeMismatchError
    for i in range(numberofInputs):
        inputLayer.nodes[i].inValue = Activation(inputs[i],activation)

inputLayer = Layer(2) 
hiddenLayer = Layer(5)
outputLayer = Layer(3)
inputs = [1,2]
LoadInput(2,inputs,inputLayer,'linear')
layers = [inputLayer,hiddenLayer,outputLayer]
activations = ['linear','sigmoid']
model = Link(layers,activations)

for node in model.layers[0].nodes:
    print(node.inValue)

print('and')

for node in model.layers[1].nodes:
    print(node.inValue)

print('and')

for node in model.layers[2].nodes:
    print(node.inValue)




