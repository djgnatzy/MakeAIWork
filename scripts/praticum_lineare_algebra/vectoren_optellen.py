#!/user/bin/#!/usr/bin/env python3

# Gebruik twee lijsten [] - want onveranderlijk
# Tel van beiden index [0] bij elkaar op, zo ook voor indices [1] en [2] etc.

a = [0, 3, 4]
b = [1, 4, 7]

c = [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

print (c)
type (c)
print ()

# Opgezocht
# Vectors in Linear Algebra

a = [0, 3, 4]
b = [1, 4, 7]

print("Vector a = ", a)
print("Vector b = ", b)

# This is a 4 dimensional vector
# a list in python is a vector in linear algebra

# adding vectors
sum = []
for i in range(len(a)):
    sum.append(a[i] + b[i])

print("Vector Addition = ", sum)
# This is how we can print a vector in python
