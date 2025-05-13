import re

pattern = r'^[a-zA-Z][a-zA-Z0-9]+\d$'

def is_string_valid_using_regex(s):
    return bool(re.fullmatch(pattern, s))

def is_string_valid_using_cfg(s):
    # Must be at least 3 chars
    if len(s) < 3:
        print("The rules state that the string length n must be >= 3")
        return False
    # First char must be letter, last char must be digit
    if not (s[0].isalpha() and s[-1].isdigit()):
        print("The rule state that the first character in the string must be a letter")
        print("The rule state that the last character in the string must be a digit")
        return False
    # Middle chars must be alphanumeric
    if not all(ch.isalnum() for ch in s[1:-1]):
        print("The only accepted input terminals is only Alphabets and Digits")
        return False
    return True

while True:
    string = input("INPUT STRING: ")
    print("RE result:   ", "Accepted" if is_string_valid_using_regex(string) else "Rejected")
    print("CFG result:  ", "Accepted" if is_string_valid_using_cfg(string)   else "Rejected")