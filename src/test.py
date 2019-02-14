import neuron

time_constant = 0.0005

n0 = neuron.NVNeuron(time_constant)
n1 = neuron.NVNeuron(time_constant)
n2 = neuron.NVNeuron(time_constant)
n3 = neuron.NVNeuron(time_constant)
n4 = neuron.NVNeuron(time_constant)
n5 = neuron.NVNeuron(time_constant)
n6 = neuron.NVNeuron(time_constant)
n7 = neuron.NVNeuron(time_constant)


for i in range(0, 1000):

    n0.process(0)
    n1.process(1)
    n2.process(1)
    n3.process(1)
    n4.process(1)
    n5.process(1)
    n6.process(1)
    n7.process(1)

input = 0.0

for i in range(0, 1000):


    n0.process(input)
    n1.process(n0.get())
    n2.process(n1.get())
    n3.process(n2.get())
    n4.process(n3.get())
    n5.process(n4.get())
    n6.process(n5.get())
    n7.process(n6.get())

    input = n7.get()


    time_ms = round(i*n0.get_dt()*1000.0, 1)
    print(time_ms, n0.get(), n1.get(), n2.get(), n3.get(), n4.get(), n5.get(), n6.get(), n7.get())

'''
time_constant = 0.1
neurons_count = 6


net = []
for i in range(0, neurons_count):
    net.append(neuron.NVNeuron(time_constant))



for i in range(0, 100):

    input = 0.0
    if i > 10:
        input = 1.0
    if i > 50:
        input = 0.0


    for j in range(0, neurons_count):
        net[j].process(input)
        input = net[j].get()

    print(i, end = " : ")
    for j in range(0, neurons_count):
        print(net[j].get(), end = " ")

    print()
'''
