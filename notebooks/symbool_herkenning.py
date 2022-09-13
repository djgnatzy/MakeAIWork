import math as mt
from math import exp

# Define symbols

symbolVecs = {'0': (1, 0), 'x': (0 ,1)} # voor cost functie
symbolChars = dict((value, key) for key, value in symbolVecs.items ())

# Define datasets (training should normally be much larger than test set for best results)

trainingSet = (
    ((
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ),  '0'),
    ((
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0)
    ),  '0'),
    ((
        (0, 1, 0),
        (1, 1, 1),
        (0, 1, 0)
    ),  'x'), 
    ((
        (1, 0, 1),
        (0, 1, 0),
        (1, 0, 1)
    ),  'x'),  
)     

# Two possible Outputs thus, matrix (1,2) 2-nodes, therefore we need matrix Input (trainingSet) (3,3) or (9,1) 9-nodes * matrix Weight (2,9) 18-links

# input nodes do not get input from the links, output nodes get input from the links

#================================================#

# class Node: 
# def __init__(self):
#     self.value = None (is X or 0?)
#     self.inLinks = [self.outNode?]  > 9 links = input links > is voor de Output dus moet 2 waardes worden?
#
#     for rowIndex in range(len(self.inNode)):                                                  9x doorlopen
#         for columnIndex in range(len(-weights-[0])):                                          2x doorlopen
#             for termIndex in range(len(self.inNode[rowIndex])):                               1x doorlopen
#                 matrixC[rowIndex][columnIndex] += self.inNode[rowIndex][termIndex] * -weights-[termIndex][columnIndex]
#
# Node()

#================================================#

# class Link:
# def __init__(self, inNode, outNode):
#     self.weight = 0.5
#     self.inNode = list(trainingSet) ?                                                                                          > 9x
#     self.outNode = self.inNodes * self.weight + alles bij elkaar optellen (for all elements self.inNode) if is X or 0    > 2x
#
# Link()

#================================================#

# Add to output - https://machinelearningmastery.com/softmax-activation-function-with-python/
# def Softmax():
#
# transform values into probabilities
#    from math import exp, done
# calculate each probability
#
# p1 = exp(1) / (exp(1) + exp(2))
# p2 = exp(2) / (exp(1) + exp(2))
#
# report probabilities

# print(p1, p2)

# report sum of probabilities

# print(p1 + p2)

#================================================#

# def Loss()
# Cost function is mean squared error: 4 x 
# Compute differences between the observed values and the predictions.  answerX = (y - y^), answer0 = (y - y^)
# Square each of these differences > use math.exp(y - y^)
# Add all these squared differences together > .add? + + voor alle input matrices
# Divide this sum by the sample length > len() /4


#================================================#

# for rowIndex in range(len(trainingSet)):
#     for columnIndex in range(len(matrixB[0])):
#          for termIndex in range(len(trainingSet[rowIndex])):
#              matrixC[rowIndex][columnIndex] += trainingSet[rowIndex][termIndex] * matrixB[termIndex][columnIndex]
#
# for result in matrixC:
#    print(result)