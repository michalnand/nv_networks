import neuron


class NvBicore:
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



class NVNCore:
    def __init__(self, count = 8, time_constant = 1.0):
        self.count = count
        self.neurons = []

        self.input = []

        self.output = []
        self.output_activation = []


        for i in range(0, self.count):
            self.neurons.append(neuron.NVNeuron(time_constant))
            self.input.append(0)
            self.output.append(0)
            self.output_activation.append(0)


    def process(self, input = []):
        if len(input) == len(self.input):
            self.input = input
        else:
            alpha = 1.0

        for i in range(0, self.count):
            next_idx = (i+1)%self.count

            input_ = self.neurons[next_idx].get() + self.input[i]
            self.neurons[i].process(input_)
            self.output[i] = self.neurons[i].get()
            self.output_activation[i] = self.neurons[i].get_activation()

        return self.output



    def get(self):
        return self.output

    def get_activation(self):
        return self.output_activation

    def get_count(self):
        return self.count




class NUNCore:
    def __init__(self, count = 8, time_constant = 1.0):
        self.count = count
        self.neurons = []

        self.input = []

        self.output = []
        self.output_activation = []


        for i in range(0, self.count):
            self.neurons.append(neuron.NUNeuron(time_constant))
            self.input.append(0)
            self.output.append(0)
            self.output_activation.append(0)

    def process(self, input = []):
        if len(input) == len(self.input):
            self.input = input
        else:
            alpha = 1.0

        for i in range(0, self.count):
            next_idx = (i+1)%self.count

            input_ = self.neurons[next_idx].get() + self.input[i]
            self.neurons[i].process(input_)
            self.output[i] = self.neurons[i].get()
            self.output_activation[i] = self.neurons[i].get_activation()

        return self.output

    def get(self):
        return self.output

    def get_activation(self):
        return self.output_activation

    def get_count(self):
        return self.count
