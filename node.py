import random

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
        self.weight = random.random()
        self.bias = random.random()

class Network:
    def __init__(self,layers:list,connections:list):
        self.layers = layers
        self.connections = connections


    
def Link(layers:list):
    connections=[]
    for i in range(1,len(layers)):
        layer_connections = []
        layer1 = layers[i-1]
        layer2 = layers[i]

        for j in range(len(layer2.nodes)):
            weightedInput = 0
            to_node = layer2.nodes[j]
            for k in range(len(layer1.nodes)):
                from_node = layer1.nodes[k]
                layer_connections.append(Connection())
                link = layer_connections[-1]
                weightedInput += from_node.inValue*link.weight + link.bias
            to_node.inValue = weightedInput
        connections.append(layer_connections)
        return Network(layers,connections)

def LoadInput(numberofInputs:int, inputs:list, inputLayer:Layer):
    if numberofInputs!=len(inputs) or len(inputs)!=len(inputLayer.nodes): 
        raise SizeMismatchError
    for i in range(numberofInputs):
        inputLayer.nodes[i].inValue = inputs[i]

inputLayer = Layer(2) 
hiddenLayer = Layer(5)
outputLayer = Layer(3)
inputs = [1,2]
LoadInput(2,inputs,inputLayer)

model = Link([inputLayer,hiddenLayer,outputLayer])

for node in model.layers[-1].nodes:
    print(node.inValue)




