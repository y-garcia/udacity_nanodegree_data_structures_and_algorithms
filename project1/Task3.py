"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import re
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
FIXED_PATTERN = r'^\((0\d+)\)'
MOBILE_PATTERN = r'^([789]\d{3})\d* \d+$'
BANGALORE_AREA_CODE = r'(080)'
TELEMARKETER_AREA_CODE = r'140'


def get_area_codes_from_bangalore(calls_list):
    area_codes = set()
    for call in calls_list:
        incoming_number = call[0]
        answering_number = call[1]

        fixed_match = re.match(FIXED_PATTERN, answering_number)
        mobile_match = re.match(MOBILE_PATTERN, answering_number)
        is_telemarketer = answering_number.startswith(TELEMARKETER_AREA_CODE)

        if incoming_number.startswith(BANGALORE_AREA_CODE):
            if fixed_match:
                area_codes.add(fixed_match.group(1))
            elif mobile_match:
                area_codes.add(mobile_match.group(1))
            elif is_telemarketer:
                area_codes.add(TELEMARKETER_AREA_CODE)

    return sorted(area_codes)


def get_local_calls_from_bangalore(calls_list):
    total_calls = 0.0
    local_calls = 0.0
    for call in calls_list:
        incoming_number = call[0]
        answering_number = call[1]

        if incoming_number.startswith(BANGALORE_AREA_CODE):
            total_calls += 1
            if answering_number.startswith(BANGALORE_AREA_CODE):
                local_calls +=1

    return local_calls / total_calls


test_calls = [
    ["(080)1234", "(011)4567"],
    ["(080)1234", "(011)3333"],
    ["(080)1234", "(022)3333"],
    ["(080)1234", "(333)3333"],
    ["(081)2222", "(222)3333"],
    ["(080)1234", "7774 1111"],
    ["(080)1234", "8774 1111"],
    ["(080)1234", "9774 1111"],
    ["(080)1234", "140314093"]
]
assert get_area_codes_from_bangalore(test_calls) == ['011', '022', '140', '7774', '8774', '9774']

test_calls = [
    ["(080)1234", "(080)4567"],
    ["(080)1234", "(011)3333"],
    ["(080)1234", "(022)3333"],
    ["(081)2222", "(222)3333"]
]
assert f"{get_local_calls_from_bangalore(test_calls):.2%}" == "33.33%"

print("The numbers called by people in Bangalore have codes:")
print(*get_area_codes_from_bangalore(calls), sep='\n')

print(f"{get_local_calls_from_bangalore(calls):.2%} percent of calls from fixed lines in Bangalore "
      f"are calls to other fixed lines in Bangalore.")
