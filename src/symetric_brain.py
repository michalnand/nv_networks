import neuron
import bicore
import nu_bicore

import image_plot


nv_time_constant = 0.001
nu_time_constant = 0.001

bicore = bicore.Bicore(nv_time_constant)

s0 = nu_bicore.NuBicore(nu_time_constant)
s1 = nu_bicore.NuBicore(nu_time_constant)
s2 = nu_bicore.NuBicore(nu_time_constant)
s3 = nu_bicore.NuBicore(nu_time_constant)
s4 = nu_bicore.NuBicore(nu_time_constant)
s5 = nu_bicore.NuBicore(nu_time_constant)
s6 = nu_bicore.NuBicore(nu_time_constant)


time_steps = 128
neurons_count = 16

firing_image = image_plot.ImageSave(time_steps, neurons_count)
activation_image = image_plot.ImageSave(time_steps, neurons_count)

for i in range(0, time_steps):
    time_step = i


    bicore.process()
    s0.process(bicore.get())
    s1.process(s0.get())
    s2.process(s1.get())
    s3.process(s2.get())
    s4.process(s3.get())
    s5.process(s4.get())
    s6.process(s5.get())


    firing_image.put_pixel(time_step, 0, bicore.get()[0])
    firing_image.put_pixel(time_step, 1, bicore.get()[1])

    firing_image.put_pixel(time_step, 2, s0.get()[0])
    firing_image.put_pixel(time_step, 3, s0.get()[1])

    firing_image.put_pixel(time_step, 4, s1.get()[0])
    firing_image.put_pixel(time_step, 5, s1.get()[1])

    firing_image.put_pixel(time_step, 6, s2.get()[0])
    firing_image.put_pixel(time_step, 7, s2.get()[1])

    firing_image.put_pixel(time_step, 8, s3.get()[0])
    firing_image.put_pixel(time_step, 9, s3.get()[1])

    firing_image.put_pixel(time_step, 10, s4.get()[0])
    firing_image.put_pixel(time_step, 11, s4.get()[1])

    firing_image.put_pixel(time_step, 12, s5.get()[0])
    firing_image.put_pixel(time_step, 13, s5.get()[1])

    firing_image.put_pixel(time_step, 14, s6.get()[0])
    firing_image.put_pixel(time_step, 15, s6.get()[1])



    activation_image.put_pixel(time_step, 0, bicore.get_activation()[0])
    activation_image.put_pixel(time_step, 1, bicore.get_activation()[1])

    activation_image.put_pixel(time_step, 2, s0.get_activation()[0])
    activation_image.put_pixel(time_step, 3, s0.get_activation()[1])

    activation_image.put_pixel(time_step, 4, s1.get_activation()[0])
    activation_image.put_pixel(time_step, 5, s1.get_activation()[1])

    activation_image.put_pixel(time_step, 6, s2.get_activation()[0])
    activation_image.put_pixel(time_step, 7, s2.get_activation()[1])

    activation_image.put_pixel(time_step, 8, s3.get_activation()[0])
    activation_image.put_pixel(time_step, 9, s3.get_activation()[1])

    activation_image.put_pixel(time_step, 10, s4.get_activation()[0])
    activation_image.put_pixel(time_step, 11, s4.get_activation()[1])

    activation_image.put_pixel(time_step, 12, s5.get_activation()[0])
    activation_image.put_pixel(time_step, 13, s5.get_activation()[1])

    activation_image.put_pixel(time_step, 14, s6.get_activation()[0])
    activation_image.put_pixel(time_step, 15, s6.get_activation()[1])

firing_image.save("firing.png")
activation_image.save("activation.png")
