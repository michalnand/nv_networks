import neuron


class NuBicore:
    def __init__(self, time_constant = 1.0):
        self.na = neuron.NUNeuron(time_constant)
        self.nb = neuron.NUNeuron(time_constant)


    def process(self, input = [0, 0]):
        self.na.process(input[0])
        self.nb.process(input[1])

        return [self.na.get(), self.nb.get()]

    def get(self):
        return [self.na.get(), self.nb.get()]

    def get_activation(self):
        return [self.na.get_activation(), self.nb.get_activation()]
