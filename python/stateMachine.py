from mimetypes import init
from pickle import TRUE
from transitions import Machine
import random

class transitions:

    STATESLIST = ['start', 'warming', 'cooling', 'off']

    def __init__(self):
        self.machine = Machine(model = self, states=transitions.STATESLIST, initial  = 'start')
        self.temp = 16
        self.LOOP = True

        self.machine.add_transition(trigger='init', source='start', dest='warming', after='tempChange')
        self.machine.add_transition(trigger='temp_max', source='warming', dest='cooling', after='tempChange')
        self.machine.add_transition(trigger='temp_min', source='cooling', dest='warming', after='tempChange')
        self.machine.add_transition(trigger='power_off', source='*', dest='OFF', after='stopMachine')

    def tempChange(self):
        if self.machine.state == 'start':
            self.machine.init()
        elif self.machine.state == 'warming':
            if self.temp < 21:
                self.temp += random()
            else:
                self.machine.temp_max()
        elif self.machine.state == 'cooling':
            if self.temp > 21:
                self.temp -= random()
            else:
                self.machine.temp_min()

    def stopMachine(self):
        self.LOOP = False