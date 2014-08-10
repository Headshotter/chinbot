#!/usr/bin/env python
"""
scores.py - phenny Slap Module
Copyright 2009-2013, Michael Yanovich (yanovich.net)

More info:
 * phenny: https://github.com/myano/phenny/
 * Phenny: http://inamidst.com/phenny/
"""

import random

def slap(phenny, input):
    """.slap <target> - Slaps <target>"""
    text = input.group().split()
    if len(text) < 2 or text[1].startswith('#'): return
    if text[1] == phenny.nick:
        if (input.nick not in phenny.config.admins):
            text[1] = input.nick
        else: text[1] = 'herself'
    if text[1] in phenny.config.admins:
        if (input.nick not in phenny.config.admins):
            text[1] = input.nick
    verb = random.choice(('reks %s', 'castarates %s', 'fugging reks %s','fugging reks %s','reks %s in the testicles','twistens %ss testicles', 'fuggs %s mahther', 'anals %s', 'roundhouse kicks %s', 'rusty hooks %s', 'pwns %s', 'owns %s')) % (text[1])
    phenny.write(['PRIVMSG', input.sender, ' :\x01ACTION', verb, '\x01'])
slap.commands = ['slap', 'slaps','rek']
slap.priority = 'medium'
slap.rate = 60

if __name__ == '__main__':
    print __doc__.strip()
