class MPNeuron:

    def __init__(self):
        self.w = []
        self.x = []
        for i in range(3):
            self.w.append(1)
            self.x.append(1)
        self.threshold = 2.5

    def MP_Neuron_Input(self,n,threshold):
        self.w = []
        self.x = []
        for i in range(n):
            win = input()
            self.w.append(int(win))
        for i in range(n):
            xin = input()
            self.x.append(int(xin))
        self.threshold = threshold

    def MP_Neuron_Evaluate(self):
        final_value = 0
        for i in range(len(self.w)):
            final_value += self.w[i]*self.x[i]
        if(final_value>self.threshold):
            return 1
        else:
            return 0

Test = MPNeuron()
print(Test.MP_Neuron_Evaluate())

#For Three input NAND Gate, we have weights as [1,1,1] and Threshold of 2.
Test.MP_Neuron_Input(3,2)
print(Test.MP_Neuron_Evaluate())