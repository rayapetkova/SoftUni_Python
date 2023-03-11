import re

text = input()

pattern = r"(^|\s)(?P<email>[a-zA-Z\d]+[\.\-\_]*[a-zA-Z\d]*@[a-zA-Z]+[\-]*[a-zA-Z]*\.[\.a-zA-z]*[a-zA-Z])"
valid_emails = re.finditer(pattern, text)

for valid_email in valid_emails:
    print(valid_email["email"])