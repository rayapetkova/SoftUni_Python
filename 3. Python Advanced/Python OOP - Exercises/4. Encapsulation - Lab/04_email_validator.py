class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):  # gosho@abv.bg -> gosho
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):  # gosho@abv.bg -> abv
        return mail in self.mails

    def __is_domain_valid(self, domain):  # gosho@abv.bg -> bg
        return domain in self.domains

    def validate(self, email):

        return self.__is_name_valid(email.split("@")[0]) and \
            self.__is_mail_valid(email.split("@")[1].split(".")[0]) and \
            self.__is_domain_valid(email.split("@")[1].split(".")[1])


# Test code:

# mails = ["gmail", "softuni"]
# domains = ["com", "bg"]
# email_validator = EmailValidator(6, mails, domains)
# print(email_validator.validate("pe77er@gmail.com"))
# print(email_validator.validate("georgios@gmail.net"))
# print(email_validator.validate("stamatito@abv.net"))
# print(email_validator.validate("abv@softuni.bg"))
