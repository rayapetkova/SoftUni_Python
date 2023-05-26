import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


name_pattern = r"\w+"
domain_pattern = r"\.[a-z]+"

valid_domains = [".com", ".bg", ".org", ".net"]

while True:
    email = input()

    if email == "End":
        break

    domain_match = re.findall(domain_pattern, email)

    if len(email.split("@")[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if domain_match[0] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print(f"Email is valid")
