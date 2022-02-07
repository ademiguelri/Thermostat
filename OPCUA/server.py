from opcua import Server
from random import randint
import datetime
import time
import config

server = Server()

server.set_endpoint(config.URL)

name = "OPCUA_SIMULATION_SERVER"
#addspace = server.register_namespace(name)
id = 'ns=2;s="V1"'

node =  server.get_objects_node()

Param = node.add_object(id, "Parameters")

Temp = Param.add_variable('ns=2;s="V1_Te"', "Temperature", 0)
Time = Param.add_variable('ns=2;s="V1_Ti"', "Time", 0)

Temp.set_writable()
Time.set_writable()

server.start()
print("Server started at {}".format(config.URL))

while True:
    Temperature = randint(10,50)
    TIME = datetime.datetime.now()

    print(Temperature, TIME)

    Temp.set_value(Temperature)
    Time.set_value(TIME)

    time.sleep(2)