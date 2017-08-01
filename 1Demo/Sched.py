# -*- coding: utf-8 -*-

import sched
import time
from threading import Timer

s = sched.scheduler(time.time, time.sleep)

def print_time():
    print "From print_time", time.time()

def print_some_times1():
    print time.time()
    s.enter(5, 1, print_time, ())
    s.enter(10, 1, print_time, ())
    s.run()
    print time.time()

def print_some_times2():
    print time.time()
    Timer(5, print_time, ()).start()
    Timer(10, print_time, ()).start()
    time.sleep(11)  # sleep while time-delay events execute
    print time.time()


#print_some_times1()
print_some_times2()