import random

class OpenedDoor():
    
    def __init__(self, temp=20, sigma_temp=0.1, sigma_acc=0.1, y_step=0.1):
        self.name_state = 'Opened'
        self.temp = temp
        self.sigma_temp = sigma_temp
        self.y_step = y_step
        self.acc = 0
        self.sigma_acc = sigma_acc

    def get_state(self):
        report_state = {'self.name_state': self.name_state,
                        'self.temp' : self.temp, 
                        'self.sigma_temp' : self.sigma_temp,
                        'self.y_step' : self.y_step}
        return report_state

    def set_temp(self, temp):
        self.temp = temp

    def set_step(self, step):
        self.y_step = step
          
    def get_value(self, step):
        temp_value = random.gauss(self.temp + step, self.sigma_temp)
        self.temp = temp_value
        return temp_value
    
    def get_smooth_acc(self, isbegining, isend):
        self.acc = random.gauss(0, self.sigma_acc)
        if isbegining :
            self.acc = random.gauss(0.5, self.sigma_acc)
        if isend:
            self.acc = - random.gauss(0.5, self.sigma_acc)
        return self.acc