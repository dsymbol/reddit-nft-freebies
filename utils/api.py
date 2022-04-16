from prawcore import ResponseException
from time import sleep
import requests
import random
import praw
import string
import sys

class API:
    def __init__(self, client_id, client_secret, username, password):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.user_agent = API.uagent(10)

    def authorize(self):
        return praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
            username=self.username,
            password=self.password,
        )

    def authorized(self, reddit):
        try:
            reddit.user.me()
        except ResponseException:
            print("Invalid credentials")
            sys.exit()
        else:
            print(f"Logged in as: {self.username}")
            width = 13 + len(self.username)
            print('-' * width)
            sleep(1)

    def shadowban_check(self):
        print("Performing a shadowban check")
        response = requests.get(f"https://www.reddit.com/user/{self.username}/about.json",
                                headers={'User-agent': f"{self.user_agent}"}).json()
        if "error" in response:
            if response["error"] == 404:
                raise Exception(f"{self.username} is shadowbanned.")
            else:
                print(response)
        else:
            print(f"{self.username} is not shadowbanned!")

    @staticmethod
    def uagent(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str