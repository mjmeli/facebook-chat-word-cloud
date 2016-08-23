"""
    message_parser
    Enables parsing of messages from the Facebook HTML.
"""
import bisect
import datetime
from lxml import html
from collections import Counter
import dateutil.parser as dateparser

""" Unique message parser exception """
class MessageParserException(Exception):
    pass

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
            self.users = set()
        else:
            self.users = set(users)
        if messages is None:
            self.messages = []
        else:
            for message in messages:
                if not any(message.sender == user for user in self.users):
                    raise ValueError
            self.messages = sorted(messages, key=lambda x: x.date, reverse=False)

    # Add a user to the conversation
    def add_user(self, user):
        self.users.add(user)

    # Add a list of users to the conversation
    def add_users(self, users):
        self.users.update(users)

    # Add a message to the conversation
    def add_message(self, message):
        if not any(message.sender == user for user in self.users):
            raise ValueError
        bisect.insort(self.messages, message)

    # Return message contents
    def get_messages_contents(self):
        return [message.contents for message in self.messages]

""" The message parser itself """
class MessageParser:
    # HTML should be sent in as a string
    def __init__(self, htmlstr):
        if not isinstance(htmlstr, basestring):
            raise ValueError
        self.html = html.fromstring(htmlstr)

    # Parse the HTML for a conversation thread
    # Can send in either one user or a list of users
    def parse_thread(self, users):
        # Ensure users array is a list
        if type(users) is not list:
            users = [users]

        # Add user's name to the list of users
        users.append(self.get_users_name())

        # Create a new thread object
        thread = Thread(users)

        # Get all of the threads
        potential_threads = self.html.xpath("//div[@class='thread']")

        # For each thread, look to see whether the users specified are in
        # the conversation. If so, add all the messages. There may be multiple
        # threads in the conversation.
        matches = 0
        messages_added = 0
        messages_parsed = 0
        for potential_thread in potential_threads:
            # Extract the names as a list of strings
            try:
                potential_users = potential_thread.xpath("text()")[0].strip().split(", ")
                potential_users = [user.encode("utf-8") for user in potential_users]
            except (AttributeError, IndexError):
                # An exception may be thrown if a thread is found with no users
                # attached to it. Why does this happen? I don't know. Skip it.
                continue

            # Compare the users to see if we have a match
            if not Counter(users) == Counter(potential_users):
                # Not a match
                continue

            # Match if we get here. Track the number of matches
            matches = matches + 1

            # Get all of the message headers and message contents
            message_headers = potential_thread.xpath("div[@class='message']")
            message_contents = potential_thread.xpath("p")
            print "Found %d messages in thread #%d" % (len(message_headers), matches)

            # Extract the information from the messages
            for i, header in enumerate(message_headers):
                messages_parsed = messages_parsed + 1
                try:
                    sending_user = header.xpath("div/span[@class='user']/text()[1]")[0]
                    date = header.xpath("div/span[@class='meta']/text()[1]")[0]
                    contents = message_contents[i].xpath("text()")[0]

                    # Add a message to the thread
                    thread.add_message(Message(sending_user, date, contents))

                    messages_added = messages_added + 1
                except (AttributeError, IndexError):
                    # If the message is not a text message (i.e. picture), then
                    # the call to text() will throw this exception. Do not
                    # add this message as it contains no words.
                    continue
                except ValueError as e:
                    # Value error may be raised in a few scenarios. Namely, if
                    # a new user was added to the thread. In this scenario,
                    # skip the rest of the thread. Else, skip just this message.
                    if not sending_user in users:
                        break
                    else:
                        continue

        # If matches are zero, we couldn't find the conversation
        if matches == 0:
            raise MessageParserException("Conversation thread could not be found")

        # Print results
        print "RESULTS: Parsed %d threads and %d messages for %d text messages" % (matches, messages_parsed, messages_added)

        # Return the parsed thread
        return thread

    # Parse the HTML for the user's name
    def get_users_name(self):
        return self.html.xpath("/html/body/div/h1/text()")[0]
