#!/usr/bin/env python
"""
rand.py - jenni Rand Module
Copyright 2010-2013, Michael Yanovich (yanovich.net)
Licensed under the Eiffel Forum License 2.

More info:
 * jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import random
import re

def rand(jenni, input):
    random.seed()
    randinte = random.randint(0, 5)
    jenni.say(str(input.nick) + ": rate " + str(randinte) + "/5")

rand.commands = ['rate']
rand.priority = 'medium'

if __name__ == '__main__':
    print __doc__.strip()
