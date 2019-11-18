#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import datetime

conf = __import__("000_conf")
bc = __import__("100_blockchain")

value_list = []
input_list = input("Please input 'Name, Role, Media, Point': ").split(",")
for i in input_list:
	value_list.append(i.strip())

### get genesis block
dt_now = datetime.datetime.now(datetime.timezone.utc)
block_list = [bc.Block(0, dt_now.isoformat(), value_list, "").setdict()]


### record
#print(json.dumps(block_list, indent=4))	# for-test

path_dir = conf.block_dir+"/"+dt_now.strftime('%Y')+"/"
path_file = dt_now.strftime('%Y%m%d')+"_"+dt_now.strftime('%H%M%S')+"_"+dt_now.strftime('%f')
os.makedirs(path_dir, exist_ok=True)
fw = open(path_dir+path_file+".json",'w')
json.dump(block_list, fw, indent=4)

print(path_file)
