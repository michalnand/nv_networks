import neuron

nv_time_constant = 0.002
nu_time_constant = 0.001


nv_0 = neuron.NVNeuron(nv_time_constant)
nv_1 = neuron.NVNeuron(nv_time_constant)

nu_0 = neuron.NUNeuron(nu_time_constant)
nu_1 = neuron.NUNeuron(nu_time_constant)


log_file = open("log.txt","w")

for i in range(0, 100):
    time_ms = round(i*nv_0.get_dt()*1000.0, 1)

    nv_0.process(nv_1.get())
    nv_1.process(nv_0.get())

    nu_0.process(nv_0.get())
    nu_1.process(nv_1.get())


    if nv_0.get() > nv_1.get():
        master = 1
    else:
        master = -1

    if nu_0.get() > nu_1.get():
        slave = 1
    else:
        slave = -1

    result_str = str(time_ms) + " "
    result_str+= str(nv_0.get()) + " "
    result_str+= str(nv_1.get()) + " "
    result_str+= str(nu_0.get()) + " "
    result_str+= str(nu_1.get()) + " "
    result_str+= str(round(nv_0.get_rc_output(), 4)) + " "
    result_str+= str(round(nv_1.get_rc_output(), 4)) + " "
    result_str+= str(round(nu_0.get_rc_output(), 4)) + " "
    result_str+= str(round(nu_1.get_rc_output(), 4)) + "\n"


    #print(time_ms, master, slave)
    print(result_str, end = "")
    log_file.write(result_str)

log_file.close()

'''
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
