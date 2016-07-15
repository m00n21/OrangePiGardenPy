#!/usr/bin/env python
import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
import logging
import datetime
import time

logging.basicConfig(filename='watering.log',level=logging.DEBUG)


gpio.init()

gpio.setcfg(port.PG9, gpio.OUTPUT)
gpio.setcfg(port.PA11, gpio.INPUT)


gpio.pullup(port.PA11, 0)
gpio.pullup(port.PA11, gpio.PULLUP)

if gpio.input(port.PA11) == 0:
    gpio.output(port.PG9, 1)
    logging.info("Watering now : %s" % time.ctime())
    time.sleep(60)
    gpio.output(port.PG9, 0)
else:
    gpio.output(port.PG9, 0)

while gpio.input(port.PA11) == 1:
    logging.info('lol just waiting : %s' % time.ctime())
    time.sleep(60)
