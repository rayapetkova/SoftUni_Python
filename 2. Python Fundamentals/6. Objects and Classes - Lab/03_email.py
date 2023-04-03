class Email:
    is_sent = False

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


all_emails = []

while True:
    command = input()
    if command == "Stop":
        break
    line = command.split()
    message_sender, message_receiver, message = line[0], line[1], line[2]
    email = Email(message_sender, message_receiver, message)
    all_emails.append(email)

indices = list(map(int, input().split(", ")))

for idx in indices:
    all_emails[idx].send()

for some_email in all_emails:
    print(some_email.get_info())