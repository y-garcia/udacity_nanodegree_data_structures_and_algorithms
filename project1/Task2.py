"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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
duration_by_number = {}
for call in calls:
    incoming_number = call[0]
    answering_number = call[1]
    duration = int(call[3])
    if incoming_number not in duration_by_number:
        duration_by_number[incoming_number] = 0
    if answering_number not in duration_by_number:
        duration_by_number[answering_number] = 0
    duration_by_number[incoming_number] += duration
    duration_by_number[answering_number] += duration

numbers = list(duration_by_number.keys())
durations = list(duration_by_number.values())
max_duration = max(durations)
number_longest_on_the_phone = numbers[durations.index(max_duration)]

print(f"{number_longest_on_the_phone} spent the longest time, {max_duration} seconds, on the phone during September 2016.")
