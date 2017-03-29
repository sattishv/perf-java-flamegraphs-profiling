#!/usr/bin/env python
from __future__ import print_function
import sys
import fileinput
from subprocess import call
import socket
import time 
import json


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


hostname = socket.gethostname()
timestamp = int(time.time())
docs = list()
try:
    for line in fileinput.input():
        fields = line.split(" ")
        key = ("_").join(fields[0:len(fields)-1])
        
        try:
            value = int(float(fields[-1].strip()))
        except(ValueError):
            eprint(line)
            continue

        #stack = key.split(";")
        #~ command_pid = stack[0].split("-")
        #~ command = command_pid[0]
        #~ pid = command_pid[0]

        stack_depth = len(key.split(";"))

        if not (stack_depth > 40 and value < 5):
			#print(line.strip())
            
            document = dict()
            document["timestamp"] = timestamp 
            document["hostname"] = hostname 
            document["stack"] = key
            document["value"] = value

            print(json.dumps(document))
            
            #~ s = "{"
            #~ for key in document:
                #~ s += '"' + str(key) + '":"'+ str(document[key]) + '",'
            #~ s = s[:-1]
            #~ s += "}"
            #~ print(s)
            
except (KeyboardInterrupt, IOError):
    #When terminate signal or something happens that means the end of the program, send the buffered data and exit
    pass










        
        









        
        

