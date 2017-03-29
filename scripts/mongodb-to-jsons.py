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

get_endpoint = 'http://mongodb:27080/profiling/map_reduce_example/_find'


batch_size = 100
payload = {'batch_size': batch_size}
r = requests.get(get_endpoint, params=payload)
if r.status_code != 200 and r.text['ok'] != 1:
	eprint("COULDN'T GET DOCS")
	exit(1)
else:
	query_id = r.text['id']
	print(r.text["results"])


done = False
payload = {'batch_size': batch_size, "id": query_id}


while (not done):
	r = requests.get(get_endpoint, params=payload)
	if r.status_code != 200 and r.text['ok'] != 1:
		eprint("COULDN'T GET DOCS")
		exit(1)
	else:
		docs = r.text["results"] 
		if len(docs) < batch_size:
			done = True
		print(docs)

