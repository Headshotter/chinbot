#!/usr/bin/env python
"""
roulette.py - phenny Roulette Game Module
Copyright 2010-2013, Kenneth Sham
Licensed under the Eiffel Forum License 2.

More info:
 * phenny: https://github.com/myano/phenny/
 * Phenny: http://inamidst.com/phenny/
"""

import random
from datetime import datetime, timedelta
random.seed()

# edit this setting for roulette counter. Larger, the number, the harder the game.
ROULETTE_SETTINGS = {
    # the bigger the MAX_RANGE, the harder/longer the game will be
    'MAX_RANGE' : 2000,

    # game timeout in minutes (default is 1 minute)
    'INACTIVE_TIMEOUT' : 1,
}

# edit this setting for text displays
ROULETTE_STRINGS = {
    'TICK' : '*TICK*',
    'KICK_REASON' : '*SNIPED! YOU LOSE!*',
    'GAME_END' : 'Game stopped.',
    'GAME_END_FAIL' : "%s: Please wait %s seconds to stop Roulette.",
}

## do not edit below this line unless you know what you're doing
ROULETTE_TMP = {
    'LAST-PLAYER' : None,
    'NUMBER' : None,
    'TIMEOUT' :timedelta(minutes=ROULETTE_SETTINGS['INACTIVE_TIMEOUT']),
    'LAST-ACTIVITY' : None,
}

def roulette (phenny, input):
    global ROULETTE_SETTINGS, ROULETTE_STRINGS, ROULETTE_TMP
    ROULETTE_TMP['NUMBER'] = random.randint(0,1)
    if ROULETTE_TMP['NUMBER'] == 1:
        phenny.write(['BAN', '%s %s :%s' % (input.sender, input.nick, ROULETTE_STRINGS['KICK_REASON'])])
    else:
        phenny.say(ROULETTE_STRINGS['TICK'])
roulette.commands = ['roulette','superyolo','yolo']
roulette.priority = 'low'
roulette.rate = 60 

if __name__ == '__main__':
    print __doc__.strip()
