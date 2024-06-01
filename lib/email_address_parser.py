# your code goes here!
import re
class EmailAddressParser:
    pattern = re.compile (r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9+._-]+\.[a-zA-Z0-9+._-]+)')
    def __init__(self, email_address):
        self.email_address = email_address


    def parse(self):
        email = re.split(r',|\s', self.email_address)
        parsed_email = set()
        for i in email:
            if self.pattern.fullmatch(i):
                parsed_email.add(i)
        return sorted(list(parsed_email))