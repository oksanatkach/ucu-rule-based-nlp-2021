import random
import re
import requests
import json
from sparql_request import get_capital

wiki_URL = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=2&exintro=&explaintext=&format=json&utf8=&redirects=&titles="


class Bot:
    def __init__(self):
        self.bot = 'Bot: '
        self.user = 'You: '
        self.launch()

    def first_meeting(self):
        return "Hi, welcome! How can I help you?"

    def hello_response(self):
        answers = ['Hi!', 'Hello!', 'Glad to see you again.']
        return random.choice(answers)

    def goodbye_response(self):
        answers = ['Bye!', 'I will miss you']
        return random.choice(answers)

    def wiki_request(self, term):
        #@todo: send a simple get request to wikipedia and return the abstract
        return

    def get_response(self, user_text):
        if re.search('hi|hello', user_text):
            return self.hello_response()

        #@todo: parse a question like "Who is Barack Obama?" and return a response from wikipedia
        #@todo: parse a question like "What is trypophobia?" and return a response from wikipedia
        #@todo: parse a command like "Say cat" so that the bot replies "cat"
        #@todo: parse a question about capitals like "what is the capital of Ukraine?" and use SPARQL to get the reply

        else:
            return "I don't know what to say."

    def launch(self):
        print(self.bot + self.first_meeting())

        user_text = input(self.user)
        while not re.search('bye|stop|exit', user_text):
            response = self.get_response(user_text)
            print(self.bot + response)
            user_text = input(self.user)
        print(self.goodbye_response())


if __name__ == '__main__':
    Bot()
