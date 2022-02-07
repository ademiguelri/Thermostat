from opcua import Client
import time
import config

client = Client(config.URL1)

client.connect()
print("Client connected")

while True:
    Temp = client.get_node('ns=2;s="V1_Te"')
    print(Temp.get_value())

    Time = client.get_node('ns=2;s="V1_Ti"')
    print(Time.get_value())

    time.sleep(2)

