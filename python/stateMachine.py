from transitions import Machine
import random

class thermostat(object):

    STATESLIST = ['start', 'warming', 'cooling', 'off']

    def __init__(self):
        self.machine = Machine(model=self, states=thermostat.STATESLIST, initial ='start')
        self.temp = 16
        self.LOOP = True

        self.machine.add_transition(trigger='initialize', source='start', dest='warming')
        self.machine.add_transition(trigger='temp_max', source='warming', dest='cooling')
        self.machine.add_transition(trigger='temp_min', source='cooling', dest='warming')
        self.machine.add_transition(trigger='power_off', source='*', dest='OFF', after='stopMachine')


    def tempChange(self):
        if self.machine.get_state(self.state).name == 'start':
            self.machine.trigger('initialize')
            print("---Thermostat starting---")
        elif self.machine.get_state(self.state).name == 'warming':
            if self.temp < 21:
                self.temp += random()
                print("---Warming the space. Actual temperature: " + self.tempChange + "---")
            else:
                self.machine.temp_max()
        elif self.machine.get_state(self.state).name == 'cooling':
            if self.temp > 20:
                self.temp -= random()
                print("---Cooling the space. Actual temperature: " + self.tempChange + "---")
            else:
                self.machine.temp_min()
        else:
            print("---NO STATE FOUND---")
    def stopMachine(self):
        self.LOOP = False
        print("---Stoping thermostat---")
