#!/usr/bin/env python

import os
import json
import requests
from docopt import docopt

DOC = """Newebe CLI.

Usage:
  newebe_cli.py get lastmessages [--tag=<tag>] [--config=config_file]
  newebe_cli.py post <message> [--tag=<tag>] [--config=config_file]
  newebe_cli.py (-h | --help)
  newebe_cli.py --version
Options:
  -h --help                Show this screen.
  --version                Show version.
  --tag=<tag>              Post messaage with given tag.
  --config=<config_file>   Change config file location
                           (default: ~/.newebe-config).
"""
CONFIG_FILE_NAME = os.path.join(os.path.expanduser('~'), '.newebe-config')


def get_config(config_file_name):
    """
    Get config from config file
    """
    with open(config_file_name) as config_file:
        lines = config_file.readlines()
        if len(lines) > 1:
            url = lines[0].strip()
            password = lines[1].strip()
            url = 'https://%s/' % url
            return (url, password)

    return (None, None)


def login(url, password):
    """
    Log the cli so the user can access to his newebe.
    """
    requests.post(url + 'login/', {"password": password}, verify=False)


def last_messages(url, password):
    """
    Return a string containing the last 10 messages of the newebe news feed.
    """
    messages = []
    resp = requests.get(url + 'microposts/all/', verify=False)
    for message in reversed(resp.json()["rows"]):
        messages.append("-" * 80)
        date = message["date"].replace("T", " ").replace("Z", " ")
        messages.append("%s - %s" % (message["author"], date))
        messages.append(message["content"])
    messages.append("-" * 80)
    return "\n".join(messages)


def post_message(url, message, tag):
    '''
    Post a new message to your Newebe.
    '''
    path = url + 'microposts/all/'
    data = {"content": message, "tags": [tag]}
    resp = requests.post(path, json.dumps(data), verify=False)
    print resp.text


def main():
    arguments = docopt(DOC, version='Newebe CLI 0.1.0')

    if arguments["--config"]:
        config_file = arguments["--config"]
    else:
        config_file = CONFIG_FILE_NAME
    (url, password) = get_config(config_file)

    if arguments["get"] and arguments["lastmessages"]:
        login(url, password)
        print last_messages(url, password)

    if arguments["post"]:
        message = arguments["<message>"]
        tag = arguments["--tag"]
        if not tag:
            tag = "all"
        post_message(url, message, tag)


if __name__ == '__main__':
    main()
