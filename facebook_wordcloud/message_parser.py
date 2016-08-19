"""
    message_parser
    Enables parsing of messages from the Facebook HTML.
"""
import bisect
import datetime
from bs4 import BeautifulSoup
import dateutil.parser as dateparser

""" Represents a message in the message thread """
class Message:
    # Each message has a sender, date, and a contents
    def __init__(self, sender, date, contents):
        self.sender = sender
        if not isinstance(date, datetime.date):
            self.date = dateparser.parse(date)
        else:
            self.date = date
        self.contents = contents

    # Comparison of two Messages relies on their date
    def __lt__(self, other):
        return self.date < other.date
    def __gt__(self, other):
        return self.date > other.date

    # String representation of a message
    def __repr__(self):
        date_str = self.date.strftime("%a %b %d, %Y %I:%M %p")
        return self.sender + " (" + date_str + "): " + self.contents

""" Represents a conversation thread """
class Thread:
    # Each thread has a list of users and a list of messages
    def __init__(self, users=None, messages=None):
        if users is None:
            self.users = []
        else:
            self.users = users
        if messages is None:
            self.messages = []
        else:
            for message in messages:
                if not any(message.sender == user for user in self.users):
                    raise ValueError
            self.messages = sorted(messages, key=lambda x: x.date, reverse=False)

    # Add a user to the conversation
    def add_user(self, user):
        self.users.append(user)

    # Add a list of users to the conversation
    def add_users(self, users):
        self.users.extend(users)

    # Add a message to the conversation
    def add_message(self, message):
        if not any(message.sender == user for user in self.users):
            raise ValueError
        bisect.insort(self.messages, message)

""" The message parser itself """
class MessageParser:
    # HTML should be sent in as a string
    def __init__(self, html):
        if not isinstance(html, basestring):
            raise ValueError
        self.html = BeautifulSoup(html, "html.parser")
