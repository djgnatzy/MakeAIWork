#!/user/bin/#!/usr/bin/env python3

# Gebruik twee lijsten [] - want onveranderlijk
# Tel van beiden index [0] bij elkaar op, zo ook voor indices [1] en [2] etc.

a = [0, 3, 4]
b = [1, 4, 7]

# Tel van beiden index [0] bij elkaar op, zo ook voor indices [1] en [2] etc.

c = [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

print (c)
type (c)
print ()

# Opgezocht! - Vectors in Linear Algebra

a = [0, 3, 4]
b = [1, 4, 7]

print("Vector a = ", a)
print("Vector b = ", b)

# Twee onveranderlijke lijsten []

# Variabele die de nieuw berekende vector gaat weergeven 'sum'
#
# Indeces in lijst a doorlopen en bij corresponderende indeces in lijst b optellen
# Beperk het aantal keer dat de lijst doorlopen wordt door de length van
# lijst a te gebruiken
#
# Druk het resultaat af


sum = []
for i in range(len(a)):
    sum.append(a[i] + b[i])

print("Vector Addition = ", sum)

