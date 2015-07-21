import random, math
class Trainer:
    def __init__(self,x,y,a):
        self.inputs = []
        self.inputs.append(x)
        self.inputs.append(y)
        self.inputs.append(1)
        self.answer = a
class Perceptron:
    def __init__(self,n,c):
        self.weights = []
        self.c = c
        for i in range(0,n):
            self.weights.append(random.uniform(-1,1))
    def train(self, inputs, desired):
        guess = self.feedforward(inputs)
        error = desired - guess
        for i in range(0, len(self.weights)):
            self.weights[i] += self.c * error * inputs[i]
    def feedforward(self, inputs):
        sum = 0
        for i in range( 0 , len(self.weights)):
            sum += inputs[i] * self.weights[i]
        return self.activate(sum)
    def activate(self,sum):
        if sum > 0:
            return 1
        else:
            return -1
    def getWeights(self):
        return self.weights

training = []
points = 20000
count = 0
xmin = -400
ymin = -100
xmax =  400
ymax =  100
def f(x):
    return 0.4*x+1

def slope():
    x1 = xmin;
    y1 = f(x1);
    x2 = xmax;
    y2 = f(x2);
    return (y2-y1)/(x2-x1)

ptron = Perceptron(3, 0.001)


# Constructs training points

for i in range(0, points):
    x = random.uniform(xmin, xmax)
    y = random.uniform(ymin, ymax)
    answer = 1
    if y < f(x):
        answer = -1
    training.append(Trainer(x, y, answer))
    ptron.train(training[i].inputs, training[i].answer)
    weights = ptron.getWeights();
    x1 = xmin;
    y1 = (-weights[2] - weights[0]*x1)/weights[1]
    x2 = xmax;
    y2 = (-weights[2] - weights[0]*x2)/weights[1]
    print (y2-y1)/(x2-x1)
print "Answer: "+str(slope())
