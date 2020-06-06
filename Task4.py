"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

tele_call_outgoing = set()
tele_call_incoming = set()
tele_text_outgoing = set()
tele_text_incoming = set()

for entry in calls:
    tele_call_outgoing.add(entry[0])
    tele_call_incoming.add(entry[1])

for entry in texts:
    tele_text_outgoing.add(entry[0])
    tele_text_incoming.add(entry[0])

telemarketers = sorted(list(tele_call_outgoing - tele_call_incoming - tele_text_incoming - tele_text_outgoing))

print("These numbers could be telemarketers: ")
print(*telemarketers, sep = '\n')
