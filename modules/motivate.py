#!/usr/bin/env python
'''
motivate.py - motivate Module
Copyright 2013 Michael Yanovich (yanovich.net)
Licensed under the Eiffel Forum License 2.

More info:
 * phenny: https://github.com/myano/phenny/
 * Phenny: http://inamidst.com/phenny/
'''

def motivate(phenny, input):
    '''!m -- motivate somebody!'''
    if input:
        nick = input
        nick = (nick[3:]).strip()
        phenny.say("You're doing good work, %s!" % (nick))
motivate.rule = r'(?u)^(\!|\.)m\s+(\S+)'

if __name__ == '__main__':
    print __doc__.strip()
