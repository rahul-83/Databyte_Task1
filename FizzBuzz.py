class MPNeuron:

    def __init__(self):
        self.w = []
        self.x = []
        for k in range(3):
            self.w.append(1)
            self.x.append(1)
        self.threshold = 3.5

    def __init__(self,n,threshold):
        for k in range(n):
            wi = input()
            self.w.append(wi)
        for m in range(n):
            xi = input()
            self.x.append(xi)
        self.threshold = threshold

Test = MPNeuron(4,3.5)
