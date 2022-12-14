import random

class SizeMismatchError(Exception):
    "Number of inputs specified and Number of inputs provided don't match, or the number of input nodes and the size of the input data don't match"

class Node:
    def __init__(self,inValue):
        self.inValue = inValue
        self.bias = random.random()
        self.weight = random.random()
        self.outValue = self.inValue*self.weight + self.bias

class Layer:
    nodes = []
    def __init__(self, numberofNodes):
        for i in range(numberofNodes):
            self.nodes.append(Node(i))

class Network:
    def __init__(self,layers):
        self.layers = layers
        for i in range(1,len(layers)):
            layer1 = layers[i-1]
            layer2 = layers[i]


def Input(numberofInputs:int, inputs:list, inputLayer:Layer):
    if numberofInputs!=len(inputs) or len(inputs)!=len(inputLayer.nodes):
        raise SizeMismatchError
    for i in range(numberofInputs):
        inputLayer.nodes[i].inValue = inputs[i]






