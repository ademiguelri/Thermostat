from time import sleep
import datetime
from warnings import catch_warnings;
import psycopg2
import python.config as config
import python.stateMachine as stateMachine

CONNECTION = "postgres://"+config.username+":"+config.password+"@"+config.host+":"+config.port+"/"+config.dbName
query_create_table = "CREATE TABLE therm (datetime TIMESTAMP, temp FLOAT);"
query_create_hypertable = "SELECT create_hypertable('therm', 'datetime');"
drop_table = "DROP TABLE therm;"

def main():
    with psycopg2.connect(CONNECTION) as conn:
        cursor = conn.cursor()

    cursor = conn.cursor()
    try:
        cursor.execute(query_create_table)
        conn.commit()
        cursor.execute(query_create_hypertable)
        conn.commit()
    except:
        cursor.execute(drop_table)
    finally:
        conn.commit()


        #initialize state machine
        thermostat = stateMachine.thermostat()
        print("---Thermostat created---")
        print("Startig state: "+ thermostat.machine.get_state(thermostat.state).name)
        while thermostat.LOOP:
            print("---Temp Change---")
            thermostat.tempChange()
         
            if thermostat.state == 'start':
                thermostat.initialize()
            elif thermostat.temp > 23 and thermostat.state == 'warming':
                thermostat.temp_max()
            elif thermostat.temp < 16 and thermostat.state == 'cooling':
                thermostat.temp_min()

            ct = datetime.datetime.now()
            print(ct)
            cursor.execute("INSERT INTO therm (datetime, temp) VALUES (current_timestamp,"+str(thermostat.temp)+")")
            conn.commit()
            sleep(1)

        cursor.close()

if __name__ == "__main__":
   main()