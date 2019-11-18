#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import glob

conf = __import__("000_conf")
bc = __import__("100_blockchain")

input_value = input("Please input 'Name': ")
input_value = input_value.strip()

view_list = []
files = glob.glob(conf.block_dir+"/*/*.json")
for file in files:
	this_index = 0
	last_name = ""
	f = open(file, 'r')
	json_data = json.load(f)
	for item in json_data:
		if this_index <= int(item['index']):
			last_name = item['data'][0]
	if last_name == input_value:
		view_list.append({'file':file,'block':item})

### show
for view in view_list:
	print(view['file'])
	print(json.dumps(view['block'], indent=4))
