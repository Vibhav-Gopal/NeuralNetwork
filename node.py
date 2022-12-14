import random

class SizeMismatchError(Exception):
    "Number of inputs specified and Number of inputs provided don't match, or the number of input nodes and the size of the input data don't match"

class Node:
    def __init__(self,inValue):
        self.inValue = inValue


class Layer:
    nodes = []
    def __init__(self, numberofNodes):
        for i in range(numberofNodes):
            self.nodes.append(Node(i))

class Connection:
    def __init__(self):
        self.weight = random.random()
        self.bias = random.random()

class Network:
    connections = []
    def __init__(self,layers:list):
        self.layers = layers
        for i in range(1,len(layers)):
            layer_connections = []
            layer1 = layers[i-1]
            layer2 = layers[i]

            for j in range(len(layer2)):
                weightedInput = 0
                to_node = layer2[j]
                for k in range(len(layer1)):
                    from_node = layer1[k]
                    layer_connections.append(Connection())
                    link = layer_connections[-1]
                    weightedInput += from_node*link.weight + link.bias
                to_node.inValue = weightedInput
            self.connections.append(layer_connections)

def Input(numberofInputs:int, inputs:list, inputLayer:Layer):
    if numberofInputs!=len(inputs) or len(inputs)!=len(inputLayer.nodes):
        raise SizeMismatchError
    for i in range(numberofInputs):
        inputLayer.nodes[i].inValue = inputs[i]

inputLayer = Layer(2)
outputLayer = Layer(3)

model = Network([inputLayer,outputLayer])




