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
    def __init__(self,layers):
        self.layers = layers
        for i in range(1,len(layers)):
            layer_connections = []
            layer1 = layers[i-1]
            layer2 = layers[i]

            for j in range(len(layer2)):
                weightedInput:float
                for k in range(len(layer1)):
                    from_node = layer1[k]
                    to_node = layer2[j]
                    layer_connections.append(Connection())
                    link = layer_connections[-1]
                    to_node.inValue = from_node*link.weight + link.bias
                    


                


def Input(numberofInputs:int, inputs:list, inputLayer:Layer):
    if numberofInputs!=len(inputs) or len(inputs)!=len(inputLayer.nodes):
        raise SizeMismatchError
    for i in range(numberofInputs):
        inputLayer.nodes[i].inValue = inputs[i]






