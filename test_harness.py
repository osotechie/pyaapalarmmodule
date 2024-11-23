#!/usr/bin/env python3
import signal
import sys
from pyaapalarmmodule import AAPAlarmPanel

#This is a test harness for the pycrowipmodule library.

#Please Enter Own Details:
connectionType = 'serial'
ip = ''
port = '/dev/ttyUSB0'
code = '0000'


na = input(str.format("Config complete. Please press enter now to connect to the AAP {0} Module.  When finished, use Ctrl+C to disconnect and exit", connectionType.title()))
testpanel = AAPAlarmPanel(connectionType,ip, port, code)
testpanel.start()

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        testpanel.stop()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
