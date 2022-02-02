from mimetypes import init
from pickle import TRUE
from transitions import Machine
import random

class machine:

    STATESLIST = ['start', 'warming', 'cooling', 'off']
    LOOP = True
    list1 = [0, 1, 2]

    def __init__(self):
        self.machine = Machine(model = self, states=machine.STATESLIST, initial  = 'start')
        self.temp = 16

        self.machine.add_transition(trigger='init', source='start', dest='warming', after='tempChange(temp,1)')
        self.machine.add_transition(trigger='tenp_max', source='warming', dest='cooling', after='tempChange(temp,0)')
        self.machine.add_transition(trigger='tenp_min', source='cooling', dest='warming', after='tempChange(temp , 1)')
        self.machine.add_transition(trigger='power_off', source='*', dest='OFF', after='stopMachine')

    def tempChange(self, operation):
        if operation == 1:
            self.temp += random.choice(list1)

    def stopMachine(self):
        LOOP = False