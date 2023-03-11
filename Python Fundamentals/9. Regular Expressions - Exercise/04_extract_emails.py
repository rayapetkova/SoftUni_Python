import re

text = input()

pattern = r"(^|\s)(?P<email>[a-zA-Z0-9]+[\.\-\_]*[a-zA-Z0-9]*@[a-zA-Z\-]+[a-zA-Z\-]\.[\.a-zA-z]*[a-zA-Z])"
valid_emails = re.finditer(pattern, text)

for valid_email in valid_emails:
    print(valid_email["email"])