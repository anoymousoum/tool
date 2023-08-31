# coding=utf-8

import os
import time

script = 'python run.py'
for i in range(100000):
    time.sleep(4)
    os.system(script)
