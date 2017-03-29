#!/usr/bin/env python
from __future__ import print_function
import sys
import fileinput
from subprocess import call
import socket
import time 
import requests
import json

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

for line in fileinput.input():
	docs = json.loads(line)
	eprint("Ok was : " + str(docs["ok"]))
	eprint("Number of docs retrieved was : " + str(len(docs["results"])))
	for doc in docs["results"]:
		print(doc["_id"] + " " + str(float(doc["value"])))

