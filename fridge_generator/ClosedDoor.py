import random

class ClosedDoor():

    def __init__(self, temp=20, sigma_temp=0.1, sigma_acc=0.1, y_step=0.1, temp_frigo_min=4 , temp_frigo_max=5):
        self.name_state = 'Closed'
        self.temp = temp
        self.sigma_temp = sigma_temp
        self.y_step = y_step
        self.temp_frigo_min = temp_frigo_min
        self.temp_frigo_max = temp_frigo_max 
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

        # Temperature du frigo trop haute
        if  self.temp > self.temp_frigo_max :
            temp_value = random.gauss(self.temp - step, self.sigma_temp)
            
        # Temperature stable dans le frigo 
        elif self.temp_frigo_min < self.temp < self.temp_frigo_max :
            temp_value = random.gauss(self.temp, self.sigma_temp)
        
        # Temperature du frigo trop basse
        else :
            temp_value = random.gauss(self.temp + step, self.sigma_temp)

        self.temp = temp_value
        return temp_value

    def get_smooth_acc(self, isbegining, isend):
        self.acc = random.gauss(0, self.sigma_acc)
        return self.acc