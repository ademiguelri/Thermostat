from opcua import Client
import time
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/ademiguel/Desktop/Timescale')
import connection

client = Client("opc.tcp://127.0.0.1:4840")

client.connect()
print("Client connected")

while True:

    Temp = client.get_node('ns=2;s="V1_Te"')
    #print(Temp.get_value())
    Time = client.get_node('ns=2;s="V1_Ti"')
    #print(Time.get_value())
    State = client.get_node('ns=2;s="V1_St"')

    if State == 'start':
        connection.thermostat.initialize()
    elif Temp.get_value() > 23 and State == 'warming':
        connection.thermostat.temp_max()
    elif Temp.get_value() < 16 and State == 'cooling':
        connection.thermostat.temp_min()  

    time.sleep(2)

