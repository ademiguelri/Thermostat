import imp
from opcua import Server
import random
import datetime
import time


import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/ademiguel/Desktop/Timescale')
import connection

server = Server()

server.set_endpoint("opc.tcp://0.0.0.0:4840")

name = "OPCUA_SIMULATION_SERVER"
#addspace = server.register_namespace(name)
id = 'ns=2;s="V1"'

node =  server.get_objects_node()

Param = node.add_object(id, "Parameters")

Temp = Param.add_variable('ns=2;s="V1_Te"', "Temperature", 0)
Time = Param.add_variable('ns=2;s="V1_Ti"', "Time", 0)
State = Param.add_variable('ns=2;s="V1_St"', "State", 0)

Temp.set_writable()
Time.set_writable()
State.set_writable()

server.start()
print("Server started at {}".format("opc.tcp://127.0.0.1:4840"))

#thermostat = connection.thermostat()
#print("---Thermostat created---")
#print("Startig state: "+ thermostat.machine.get_state(thermostat.state).name)


Temperature = 20

while True:

    TIME = datetime.datetime.now()
    STATE = thermostat.machine.get_state(thermostat.state).name
    
    if thermostat.machine.get_state(thermostat.state).name == 'start':
            print("---Thermostat starting---")
    elif thermostat.machine.get_state(thermostat.state).name == 'warming':
            Temperature += random.random()
            print("---Warming the space. Actual temperature: " + str(Temperature) + "---")

    elif thermostat.machine.get_state(thermostat.state).name == 'cooling':
            Temperature -= random.random()
            print("---Cooling the space. Actual temperature: " + str(Temperature) + "---")

    Temp.set_value(Temperature)
    Time.set_value(TIME)
    State.set_value(STATE)

    time.sleep(2)