import neuron
import image_plot

import numpy as np
import random

neurons_count = 256
connections_density = 0.05

connections = np.zeros((neurons_count, neurons_count))

for y in range(0, neurons_count):
    for x in range(0, neurons_count):
        if random.random() >= connections_density:
            r = random.random()*2.0 - 1.0
            connections[y][x] = r


nv_time_constant = 0.001


neurons = []
for i in range(0, neurons_count):
    neurons.append(neuron.NUNeuron(nv_time_constant))


time_steps = 256

firing_image = image_plot.ImageSave(time_steps, neurons_count)
activation_image = image_plot.ImageSave(time_steps, neurons_count)

for time_step in range(0, time_steps):

    print("time step = ", time_step)

    neuron_inputs = np.zeros((neurons_count))
    for neuron_idx in range(0, neurons_count):
        sum = 0.0
        for i in range(0, neurons_count):
            sum+= neurons[i].get()*connections[neuron_idx][i]

        neuron_inputs[neuron_idx] = sum

    for neuron_idx in range(0, neurons_count):
        neurons[neuron_idx].process(neuron_inputs[neuron_idx])


    for neuron_idx in range(0, neurons_count):
        firing_image.put_pixel(time_step, neuron_idx, neurons[neuron_idx].get())
        activation_image.put_pixel(time_step, neuron_idx, neurons[neuron_idx].get_activation())


firing_image.save("firing.png")
activation_image.save("activation.png")
