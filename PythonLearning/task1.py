#!/usr/bin/env python

import re
from datetime import datetime

#use ?P<name>...to name a matched group,so you can get it by group('name')
m=re.search("output_(?P<year>\d{4})\.(?P<month>\d{2})\.(?P<day>\d{2})\.txt","output_1981.10.21.txt")

year=m.group('year')
month=m.group('month')
day=m.group('day')

#get the weekday of a particual date
weekday=datetime(int(year),int(month),int(day)).strftime('%w')

#construct output format
output='output_'+year+'-'+month+'-'+day+'-'+weekday+'.txt'

print(output)




