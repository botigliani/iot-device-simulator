from OpeningDoor import OpeningDoor
from OpenedDoor import OpenedDoor
from ClosingDoor import ClosingDoor
from ClosedDoor import ClosedDoor


class StateController():

    def __init__(self):
        self.current_state = None
        self.storage = []
        self.current_temp = None
        self.iteration_counter = 0
        self.acc = None
        self.smooth_position = True
    
    def play_state(self, selected_state, duration, step, smooth_position):
        selected_state.set_temp(self.current_temp)
        self.current_state = selected_state
        print('Current state: {}'.format(self.current_state.get_state()))
        for i in range(duration):
            if smooth_position:
                isbegining = False
                isend = False
                if i < 3:
                    isbegining = True
                elif i > (duration - 3):
                    isend = True
                self.acc = self.current_state.get_smooth_acc(isbegining, isend)
            self.current_temp = self.current_state.get_value(step)
            value = {'msg_num': self.iteration_counter,
                     'temperature': self.current_temp,
                     'acceleration': self.acc}
            self.iteration_counter += 1
            self.storage.append(value)

    def scenario(self, initial_temp=100, closed_duration_1=80, opening_duration=20, opened_duration=80,
                 closing_duration=20, closed_duration_2=80, step=0.1):
        ''' 10 units == 1s '''
        # Initialization of states and parameters 
        self.current_temp = initial_temp
        opening =  OpeningDoor()
        opened = OpenedDoor()
        closing = ClosingDoor()
        closed = ClosedDoor()
        self.iteration_counter = 0
        smooth_position = True

        #  Step 0 : Closed Door
        self.play_state(closed, closed_duration_1, step, smooth_position)
        #  Step 1 : Opening Door
        self.play_state(opening, opening_duration, step, smooth_position)
        #  Step 2 : Opened Door
        self.play_state(opened, opened_duration, step, smooth_position)
        #  Step 3 : Closing Door
        self.play_state(closing, closing_duration, step, smooth_position)
        #  Step 4 : Closed Door
        self.play_state(closed, closed_duration_2, step, smooth_position)

        return self.storage
