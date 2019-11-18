#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import datetime

conf = __import__("000_conf")
bc = __import__("100_blockchain")

value_list = []
input_list = input("Please input 'Token, Name, Role': ").split(",")
token = input_list.pop(0)
for i in input_list:
	value_list.append(i.strip())

### get previous data
this_index = 0
last_data_media = ""
last_data_point = ""
last_hash = ""

dir_year = token[0:4]
path_dir = conf.block_dir+"/"+dir_year+"/"
path_file = token
f = open(path_dir+path_file+".json", 'r')
json_data = json.load(f)
for item in json_data:
	if this_index <= int(item['index']):
		this_index = int(item['index']) + 1
		last_data_media = item['data'][2]
		last_data_point = item['data'][3]
		last_hash = item['hash']
value_list.append(last_data_media)
value_list.append(last_data_point)

### get next block
dt_now = datetime.datetime.now(datetime.timezone.utc)
block = bc.Block(this_index, dt_now.isoformat(), value_list, last_hash).setdict()

### record
json_data.append(block)
#print(json.dumps(json_data, indent=4))	# for-test

fw = open(path_dir+path_file+".json",'w')
json.dump(json_data, fw, indent=4)
