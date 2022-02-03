from transitions import Machine
import random

class thermostat(object):

    STATESLIST = ['start', 'warming', 'cooling', 'off']

    def __init__(self):
        self.machine = Machine(model=self, states=thermostat.STATESLIST, initial ='start')
        self.temp = 20
        self.LOOP = True

        self.machine.add_transition(trigger='initialize', source='start', dest='warming')
        self.machine.add_transition(trigger='temp_max', source='warming', dest='cooling')
        self.machine.add_transition(trigger='temp_min', source='cooling', dest='warming')
        self.machine.add_transition(trigger='power_off', source='*', dest='OFF', after='stopMachine')

    def tempChange(self):
        if self.machine.get_state(self.state).name == 'start':
            print("---Thermostat starting---")

        elif self.machine.get_state(self.state).name == 'warming':
                self.temp += random.random()
                print("---Warming the space. Actual temperature: " + str(self.temp) + "---")

        elif self.machine.get_state(self.state).name == 'cooling':
                self.temp -= random.random()
                print("---Cooling the space. Actual temperature: " + str(self.temp) + "---")

        else:
            print("---NO STATE FOUND---")
            
    def stopMachine(self):
        self.LOOP = False
        print("---Stoping thermostat---")
