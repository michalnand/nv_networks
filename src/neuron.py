
class NUNeuron:
    def __init__(self, time_constant = 1.0, dt = 0.001):
        self.time_constant  = time_constant
        self.dt             = dt
        self.alpha          =  self.time_constant / (self.time_constant + self.dt)

        self.y  = 0.0

        self.yh     = 0.9
        self.yl     = 0.1
        self.state  = 0

    def process(self, input):

        self.y = self.alpha*self.y + (1.0 - self.alpha)*input

        if self.state == 0:
            if self.y > self.yh:
                self.state = 1
        else:
            if self.y < self.yl:
                self.state = 0

    def set_state(self, state):
        self.state = state


    def get_rc_output(self):
        return self.y

    def get(self):
        return 1 - self.state

class NVNeuron:

    def __init__(self, time_constant = 1.0, dt = 0.001):
        self.time_constant  = time_constant
        self.dt             = dt
        self.alpha          =  self.time_constant / (self.time_constant + self.dt)

        self.y  = 0.0
        self.x0 = 0.0
        self.x1 = 0.0

        self.yh     = 0.9
        self.yl     = 0.1
        self.state  = 0

    def process(self, input):
        self.x1 = self.x0
        self.x0 = input

        self.y = self.alpha*self.y + (self.x0 - self.x1)

        if self.state == 0:
            if self.y > self.yh:
                self.state = 1
        else:
            if self.y < self.yl:
                self.state = 0

    def set_state(self, state):
        self.state = state


    def get_rc_output(self):
        return self.y

    def get(self):
        return 1 - self.state

    def get_dt(self):
        return self.dt
