#https://realpython.com/python-command-line-arguments/
#https://docs.python.org/3/howto/argparse.html

import argparse
from pyfiglet import Figlet

test = Figlet(font='ANSI Shadow')


parser = argparse.ArgumentParser()
#string input
parser.add_argument("-e" , "--echo" , help="echo the string you use here" )
#integer input
parser.add_argument("-s" , "--square", help="display a square of a given number" , type=int)
#optional input
parser.add_argument("-p" , "--proxy" , help="Enter Proxy info: 127.0.0.1")
args = parser.parse_args()

#banner
print(test.renderText('lodwad'))

##display
print(args.echo)
print(args.square**2)
print(args.proxy)
#optional argument
#if args.proxy:
#	print 'Proxy Info: ', args.proxy

