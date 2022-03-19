from random import choice, sample
from string import digits
import os

#      _          _            _       ____                           _              _  _     ____            _           _
#     / \   _ __ | |_ ___  ___| |__   / ___|  ___ _ __ ___   ___  ___| |_ ___ _ __  | || |   |  _ \ _ __ ___ (_) ___  ___| |_
#    / _ \ | '_ \| __/ _ \/ __| '_ \  \___ \ / _ \ '_ ` _ \ / _ \/ __| __/ _ \ '__| | || |_  | |_) | '__/ _ \| |/ _ \/ __| __|
#   / ___ \| |_) | ||  __/ (__| | | |  ___) |  __/ | | | | |  __/\__ \ ||  __/ |    |__   _| |  __/| | | (_) | |  __/ (__| |_
#  /_/   \_\ .__/ \__\___|\___|_| |_| |____/ \___|_| |_| |_|\___||___/\__\___|_|       |_|   |_|   |_|  \___// |\___|\___|\__|
#          |_|                                                                                             |__/
# | ------------------------------------------------------------------------------------------------------------------------ |
# Based on implementation @ https://xkpasswd.net/
# Authors: Obafemi Teminife, Adedeji Abubakar Sanusi, David Adegoke, Leonard Efe Oriobor

welcome = """
  ___      _   _               ___                              _    ___                       _
 | _ \_  _| |_| |_  ___ _ _   | _ \__ _ _______ __ _____ _ _ __| |  / __|___ _ _  ___ _ _ __ _| |_ ___ _ _
 |  _/ || |  _| ' \/ _ \ ' \  |  _/ _` (_-<_-< V  V / _ \ '_/ _` | | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
 |_|  \_, |\__|_||_\___/_||_| |_| \__,_/__/__/\_/\_/\___/_| \__,_|  \___\___|_||_\___|_| \__,_|\__\___/_|
	  |__/
	Type h to see help menu
"""

info = """
Having a weak password is not good for a system that demands high confidentiality and security of user credentials.
It turns out that people find it difficult to make up a strong password that is strong enough to prevent unauthorized users from memorizing it.
Creating a strong password and remembering it is a tedious task.
This program generates a random password from the given input word hints, allowing users to both secure their information while maintaining easy rememberance

Example:
	Input any number of word hints separated by spaces
	Hints: singing snoring surrender disperser deputize
	Password: !!49singing:snoring:surrender:disperser:deputize:05!!

Commands
	h: Prints this help message
	q: quit
"""


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def transform(hints):
    transformed = []
    for hint in hints:
        cond = choice([True, False])
        if(cond == True):
            transformedHint = [p.capitalize() for p in hint]
            transformed.append("".join(transformedHint))
        else:
            transformed.append(hint)
    return transformed


symbols = ['!', '@', '$', '%', '^', '&', '*', '-',
           '_', '+', '=', ':', '|', '~', '?', '/', '.', ';']


def generatePassword(hints):
    separator = choice(symbols)
    padding = f"{choice(symbols)}"*2
    startDigits = ''.join(sample(digits, 2))
    endDigits = ''.join(sample(digits, 2))
    stuff = f'{separator}'.join(hints)
    final = [padding, startDigits, stuff, separator, endDigits, padding]
    return ''.join(final)


run = True

while run:
    clear()
    print(welcome)
    start = input("==> ")
    if start == 'q':
        run = False
    elif(start == 'h'):
        print(welcome)
        print(info)
    else:
        rawHints = start.split(" ")
        hints = transform(rawHints)
        print(generatePassword(hints))
        print('\n\n')
        input("Press enter to continue...")
