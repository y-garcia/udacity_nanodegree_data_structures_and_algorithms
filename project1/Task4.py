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


def get_telemarketers(texts_list, calls_list):
    telemarketers = set()
    texters_or_receivers = set()
    texts_count = len(texts_list)
    calls_count = len(calls_list)
    for i in range(max(texts_count, calls_count)):
        if i < texts_count:
            outgoing_texter = texts_list[i][0]
            receiving_texter = texts_list[i][1]
            texters_or_receivers.add(outgoing_texter)
            texters_or_receivers.add(receiving_texter)
        if i < calls_count:
            receiving_number = calls_list[i][1]
            texters_or_receivers.add(receiving_number)

    for call in calls_list:
        outgoing_number = call[0]
        if outgoing_number not in texters_or_receivers:
            telemarketers.add(outgoing_number)

    return sorted(telemarketers)


test_texts = [
    ["(080)1111", "(011)4567"],
    ["(080)1234", "(080)2222"]
]
test_calls = [
    ["(080)1111", "(011)4567"],
    ["(080)2222", "(011)4567"],
    ["(080)3333", "(022)2222"],
    ["(080)5555", "(080)4567"],
    ["(080)4444", "(080)3333"]
]
assert get_telemarketers(test_texts, test_calls) == ['(080)4444', '(080)5555']

print("These numbers could be telemarketers: ")
print(*get_telemarketers(texts, calls), sep='\n')
