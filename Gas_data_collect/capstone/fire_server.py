import sys
from socket import *
from capstone.gasLeakage import *
import pandas as pd
import datetime
import time

def main():

    ''' print("[DEBUG] Connect Server Start")

    SERVER_ADDR = '192.168.0.101'
    PORT = 1626
    BUFSIZE = 1024

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((SERVER_ADDR, PORT))
    '''
    
    gas = gasLeakage()

    while True:
        '''server_recv = client_socket.recv(BUFSIZE)

        if server_recv == -1:
            print("[DEBUG] Exit")
            break;
        '''
        
        getData = gas.getSensorData()
        gas.controlFan(getData)

        '''
        sensor_data = bytes(getData)

        client_socket.send(sensor_data)
        '''
        print("[DEBUG] Smoke Sensor Value = %u"%(getData))
        
        data = [[datetime.datetime.now(), getData]]
        submission = pd.DataFrame(data)
        submission.to_csv('./Gas_DataSet.csv', header = False, mode = 'a', index = False)
        time.sleep(0.5)
        

    print("END")


if __name__ == "__main__":
    main()