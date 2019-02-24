import neuron


class Bicore:
    def __init__(self, time_constant = 1.0):
        self.na = neuron.NVNeuron(time_constant)
        self.nb = neuron.NVNeuron(time_constant)


    def process(self, input = [0, 0]):
        in_a = self.nb.get() + input[0]
        self.na.process(in_a)

        in_b = self.na.get() + input[1]
        self.nb.process(in_b)

        return [self.na.get(), self.nb.get()]

    def get(self):
        return [self.na.get(), self.nb.get()]

    def get_activation(self):
        return [self.na.get_activation(), self.nb.get_activation()]
