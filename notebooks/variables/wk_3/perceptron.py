x_input = [0.1, 0.5, 0.2]
w_weights = [0.4, 0.3, 0.6]
threshold = 0.5

def step(weighted_sum):
    if weighted_sum > threshold:
        return 1 # ('x' > (1,0))
    else:
        return 0 # ('0' > (0,1))
    
def perceptron():
    weighted_sum = 0
    for x,w in zip (x_input, w_weights):
         weighted_sum += x*w
         print(weighted_sum)
    return step(weighted_sum)        

output = perceptron()
print('output: '+ str(output))

# https://www.youtube.com/watch?v=-KLnurhX-Pg&ab_channel=PythonSimplified

# input x weights = weighted sum < threshold