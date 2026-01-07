import math

def relu(x):

  return max(0, x)

def sigmoid(x):

  return 1 / (1 + math.exp(-x))

free, win, offer = 1, 0, 1

w1 = [0.5, -0.2, 0.3]   

w2 = [0.4, 0.1, -0.5]  

h1_input = sum([free, win, offer][i] * w1[i] for i in range(3))

h2_input = sum([free, win, offer][i] * w2[i] for i in range(3))

h1_output = relu(h1_input)

h2_output = relu(h2_input)

print("H1 input:", h1_input)

print("H2 input:", h2_input)

output_input = h1_output * 0.7 + h2_output * 0.2

print("Output neuron input:", output_input)

print("Final output:", sigmoid(output_input))