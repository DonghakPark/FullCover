import sys
from socket import *
from gasLeakage import *
import pandas as pd
import datetime
import time

def sen():

    gas = gasLeakage()

    getData = gas.getSensorData()
    gas.controlFan(getData)

    print("[DEBUG] Smoke Sensor Value = %u"%(getData))

    data = [[datetime.datetime.now(), getData]]
    submission = pd.DataFrame(data)
    submission.to_csv('./Gas_DataSet.csv', header = False, mode = 'a', index = False)
    time.sleep(0.5)
    return getData

if __name__ == "__main__":
    sen()