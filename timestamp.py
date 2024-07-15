import time
import os

while True:
    with open('timestamp.txt', 'r') as f:
        lines = f.readlines()
        timestamp = lines[0]

    if int(time.time()) - int(timestamp) >= 300:
        n = str(int(time.time()))
        os.system("python3 "+"UniswapRebalance.py")
        print("launched urebalance2.py")
        with open('logstarting.txt', 'w') as f:
            f.write("\n"+n+" "+"launched UniswapRebalance.py")
            f.close()
    time.sleep(240)
