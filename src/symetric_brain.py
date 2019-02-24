import neuron
import core

import image_plot

time_steps = 1024
nv_time_constant = 0.002

c0 = core.NVNCore(8, nv_time_constant)
c1 = core.NVNCore(8, nv_time_constant)
c2 = core.NVNCore(8, nv_time_constant)
c3 = core.NVNCore(8, nv_time_constant)

firing_image = image_plot.ImageSave(time_steps, 8*4)
activation_image = image_plot.ImageSave(time_steps, 8*4)

for time_step in range(0, time_steps):

    c0.process()
    c1.process(c1_input)
    c2.process(c2_input)
    c3.process(c3_input)


    idx = 0
    for i in range(0, c0.get_count()):
        firing_image.put_pixel(time_step, idx, c0.get()[i])
        activation_image.put_pixel(time_step, idx, c0.get_activation()[i])
        idx+= 1

    for i in range(0, c1.get_count()):
        firing_image.put_pixel(time_step, idx, c1.get()[i])
        activation_image.put_pixel(time_step, idx, c1.get_activation()[i])
        idx+= 1

    for i in range(0, c2.get_count()):
        firing_image.put_pixel(time_step, idx, c2.get()[i])
        activation_image.put_pixel(time_step, idx, c2.get_activation()[i])
        idx+= 1

    for i in range(0, c3.get_count()):
        firing_image.put_pixel(time_step, idx, c3.get()[i])
        activation_image.put_pixel(time_step, idx, c3.get_activation()[i])
        idx+= 1






firing_image.save("firing.png")
activation_image.save("activation.png")
