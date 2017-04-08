#!/usr/bin/env python
from __future__ import print_function
import sys
import fileinput
from subprocess import call
import time 
import requests
import json


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_data(start_time, end_time):
    get_endpoint = 'http://mongodb:5001/stacks/'
    payload = {'start_time': start_time, "end_time": end_time}

    r = requests.get(get_endpoint, params=payload)
    if r.status_code != 200:
        eprint("COULDN'T GET DOCS")
        exit(1)
    else:
        print(json.dumps(r.json()))


if __name__ == "__main__":
    if len(sys.argv) < 3 :
        eprint("Missing arguments, at least two timestamps are needed, first one will be start time and seconds one will be end time")
        exit(1)
    try:
		start_time = int(sys.argv[1]) #1491644120
		end_time = int(sys.argv[2]) #1491644133
    except ValueError:
		eprint("Parameters must be integers, in fact UNIX Timestamps")
		exit(1)

    get_data(start_time, end_time)

