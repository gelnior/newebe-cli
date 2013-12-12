# Newebe CLI

Small client to use the distributed social network Newebe from the command
line. It's useful when you're too lazy to open a web browser.

# Usage

This displays the last 10 messages you received:

      newebe_cli.py get lastmessages

This posts a new message to your contacts:

      newebe_cli.py post <message>

Full usage:

    Usage:
      newebe_cli.py get lastmessages [--config=config_file]
      newebe_cli.py post <message> [--tag=<tag>] [--config=config_file]
      newebe_cli.py (-h | --help)
      newebe_cli.py --version
    Options:
      -h --help                Show this screen.
      --version                Show version.
      --tag=<tag>              Post messaage with given tag.
      --config=<config_file>   Change config file location
                               (default: ~/.newebe-config).



