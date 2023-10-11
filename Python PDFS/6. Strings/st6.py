import re

# Regular expression pattern
pattern = r'^Hello, \w+!$'

# String to match against the pattern
string_to_match = "Hello, Alice!"

match = re.match(pattern, string_to_match)

if match:
    print("String matches the pattern.")
else:
    print("String does not match the pattern.")
