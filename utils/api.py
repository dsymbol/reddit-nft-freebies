import random
import string
import sys
import logging
from time import sleep

import praw
import requests
from prawcore import ResponseException


class API:
    def __init__(self, client_id, client_secret, username, password):
        self.username = username
        self.user_agent = API.uagent(10)
        self.auth = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=self.user_agent,
            username=self.username,
            password=password,
        )
        self.log = logging.getLogger(__name__)

    def authorize(self):
        self.shadowban_check()
        self.authorized()
        self.auth.read_only = False
        return self.auth

    def authorized(self):
        try:
            self.auth.user.me()
        except ResponseException as e:
            self.log.error("Invalid Credentials")
            self.log.error(str(e))
            sys.exit()
        else:
            self.log.info(f"Logged in as: {self.username}")
            sleep(1)

    def shadowban_check(self):
        self.log.info("Performing a shadowban check")
        response = requests.get(f"https://www.reddit.com/user/{self.username}/about.json",
                                headers={'User-agent': f"{self.user_agent}"}).json()
        if "error" in response:
            if response["error"] == 404:
                self.log.error(f"{self.username} is shadowbanned.")
                sys.exit()
            self.log.debug(response)
        else:
            self.log.info(f"{self.username} is not shadowbanned!")

    @staticmethod
    def uagent(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))
