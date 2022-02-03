from time import sleep
#import psycopg2
import python.config as config
import python.stateMachine as stateMachine

#CONNECTION = "postgres://"+config.username+":"+config.password+"@"+config.host+":"+config.port+"/"+config.dbName
#query_create_table = "CREATE TABLE auto (data TIMESTAMP, balio INT);"

def main():
#    with psycopg2.connect(CONNECTION) as conn:
#        cursor = conn.cursor()

#    cursor = conn.cursor()
#    cursor.execute(query_create_table)
#    conn.commit()
#    cursor.close()
    
    #initialize state machine
    thermostat = stateMachine.transitions
    print("---Thermostat created---")
    while thermostat.LOOP:
        stateMachine.transitions.tempChange
        sleep(1)