#! python3
# phone-and-email-extractor.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile('''(
    ^(?:(?:\(?(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?(?:\(?0\)?[\s-]?)?)|(?:\(?0))(?:(?:\d{5}\)?[\s-]?\d{4,5})|(?:\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3}))|(?:\d{3}\)?[\s-]?\d{3}[\s-]?\d{3,4})|(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}))(?:[\s-]?(?:x|ext\.?|\#)\d{3,4})?$
)''')

#TODO: Create email regex

#TODO: Find matches in clipboard text

#TODO: Copy results to the clipboard.


