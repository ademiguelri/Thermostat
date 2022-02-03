from time import sleep
import psycopg2
import python.config as config
import python.stateMachine as stateMachine

#CONNECTION = "postgres://"+config.username+":"+config.password+"@"+config.host+":"+config.port+"/"+config.dbName
#query_create_table = "CREATE TABLE auto (dateTime TIMESTAMP, info INT);"

def main():
#    with psycopg2.connect(CONNECTION) as conn:
#        cursor = conn.cursor()

#    cursor = conn.cursor()
#    cursor.execute(query_create_table)
#    conn.commit()
#    cursor.close()

    
    #initialize state machine
    thermostat = stateMachine.thermostat()
    print("---Thermostat created---")
    print("Startig state: "+ thermostat.machine.get_state(thermostat.state).name)
    while thermostat.LOOP:
        print("---Temp Change---")
        thermostat.tempChange()
        sleep(1)
        if thermostat.state == 'start':
            thermostat.initialize()
        elif thermostat.temp > 23:
            thermostat.temp_max()
        elif thermostat.temp < 19:
            thermostat.temp_min()

if __name__ == "__main__":
    main()