import sys
from gasLeakage import *
import pandas as pd
import datetime
import time

def sen():
    count =0    
    temp = []
    
    gas = gasLeakage()

    while count <=20:
        getData = gas.getSensorData()
        gas.controlFan(getData)

        print("[DEBUG] Smoke Sensor Value = %u"%(getData))

        data = [[datetime.datetime.now(), getData]]
        submission = pd.DataFrame(data)
        submission.to_csv('./Gas_DataSet.csv', header = False, mode = 'a', index = False)
        time.sleep(0.5)
        temp.append(getData)
        temp2.appned(str(getData))
        count +=1
    return temp, temp2

if __name__ == "__main__":
    sen()