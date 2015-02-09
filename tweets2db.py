#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymongo
import json
import os
import re
from datetime import datetime

# conntect to database
con = pymongo.Connection('127.0.0.1', port=27017)
aufschrei = con.aufschreirevisited.tweets
# clear data collection (if exists)
aufschrei.drop()

#onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

# directory containing JSON-files (change if needed)
d = './data/aufschrei-tweets/'

files = [f for f in os.listdir(d) if os.path.isfile(os.path.join(d,f))]

for file in files:
    with open(os.path.join(d,file),'r',encoding="utf-8") as f:
        for index, line in enumerate(f):
            # if line not empty
            if line.strip():
                # get rid of newlines and linebreaks within text
                line = line.replace("\\n"," ")
                line = line.replace("\\\\r","/r")
                line = line.replace("\\r"," ")
                line = re.sub(',\s*$','',line,)
                # JSON object
                data = []
                try:
                    line = json.loads(line)
                    # change time format: string to datetime object
                    this = line['created_at']
                    this = datetime.strptime(this, "%a %b %d %X +0000 %Y")
                    line['created_at'] = this
                    line['time'] = int(datetime.strftime(this, "%H"))
                    # add to JSON object
                    data.append(line)
                    for line in data:
                        # save to database
                        aufschrei.save(line)
                except:
                    print("error! file: "+file)
                    print("\tline: "+str(index))
con.disconnect()
