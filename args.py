#https://realpython.com/python-command-line-arguments/

#https://docs.python.org/3/howto/argparse.html

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)