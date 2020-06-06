"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from datetime import datetime

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
time_dict = {}

for entry in calls:
    time_dict[entry[0]] = time_dict.get(entry[0], 0) + int(entry[3])
    time_dict[entry[1]] = time_dict.get(entry[1], 0) + int(entry[3])

max_number = max(time_dict, key=time_dict.get)
max_duration = time_dict[max_number]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_number, max_duration))