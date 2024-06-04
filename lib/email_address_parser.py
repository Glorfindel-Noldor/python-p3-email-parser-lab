# your code goes here!
import re

# class EmailAddressParser:
#     def __init__(self, var):
#         self.var = var

#     def audit(self):
#         if (""" condition here """):
#             return self.parse()
#         else: raise ValueError('your email does not qualify!')




class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses
    
    def parse(self):
        # Split the string by spaces and commas
        parts = re.split(r'[ ,]+', self.addresses)
        # Use a regular expression to filter out non-email parts
        email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
        emails = [part for part in parts if email_pattern.fullmatch(part)]
        # Return the sorted list of emails
        return sorted(emails)
