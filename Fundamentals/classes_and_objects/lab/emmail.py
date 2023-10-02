class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    command = input()
    if command == "Stop":
        break

    sequence = command.split()
    sender = sequence[0]
    receiver = sequence[1]
    content = sequence[2]
    email = Email(sender, receiver, content)
    emails.append(email)

sent_emails_indexes = [int(i) for i in input().split(', ')]

for index, email in enumerate(emails):
    if index in sent_emails_indexes:
        email.send()
    print(email.get_info())

