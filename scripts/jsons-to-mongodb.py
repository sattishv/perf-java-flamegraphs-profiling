#!/usr/bin/env python
from __future__ import print_function
import sys
import fileinput
from subprocess import call
import socket
import time 
import requests
import json
import ast

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


headers = {'content-type': 'application/json'}


def send_docs(docs):
    #r = requests.post(post_endpoint, data={"docs": json.dumps(docs)})
    r = requests.post(post_endpoint, headers=headers,data=json.dumps(docs))
    if r.status_code != 201 : #and r.text['ok'] != 1: 
        eprint("[MONGODB SENDER] couldn't properly post documents to address " + post_endpoint)
        eprint(r.text)
	return False
    else:
        print ("Post was done at: " +  time.strftime("%D %H:%M:%S", time.localtime()) + " with " + str(len(docs)) + " documents , timestamp is " + str(time.time()))
        return True
    

post_doc_buffer_length = 2000
failed_connections = 0
abort = False
post_endpoint = 'http://mongodb:5000/cpu'
json_documents = []
try:
    for line in fileinput.input():
        try:
            #new_doc = json.loads(line)
            new_doc = ast.literal_eval(line)
            json_documents = json_documents + [new_doc]
        except ValueError:
            print ("Error with document " + str(line))
            continue

        length_docs = len(json_documents)
        if(length_docs >= post_doc_buffer_length):
            try:
                send_docs(json_documents)
            except(requests.exceptions.ConnectTimeout):
                eprint("[MONGODB SENDER] couldn't send documents to address " + post_endpoint + " and tried for " + str(failed_connections) + " times")
            json_documents = []
            if abort : exit(1)
            sys.stdout.flush()
    send_docs(json_documents)
except (KeyboardInterrupt, IOError):
    #When terminate signal or something happens that means the end of the program, send the buffered data and exit
    pass









        
        

