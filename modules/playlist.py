#!/usr/bin/env python
"""
vid.py - phenny vid Module
Copyright 2008-2013, Michael Yanovich (yanovich.net)
Licensed under the Eiffel Forum License 2.

More info:
 * phenny: https://github.com/myano/phenny/
 * Phenny: http://inamidst.com/phenny/
"""

import random


def addvid(phenny, input):
    '''.addvid Ktbhw0v186Q '''
    text = input.group(2)
    if not text:
        return phenny.say('No vid provided')
    fn = open('vids.txt', 'a')
    output = 'www.youtube.com/watch?v=%s' % (text)
    fn.write(output)
    fn.write('\n')
    fn.close()
    phenny.reply('vid added.')
addvid.commands = ['addvid']
addvid.priority = 'low'
addvid.example = '.addvid'


def retrievevid(phenny, input):
    '''.vid <number> -- displays a given vid'''
    NO_QUOTES = 'There are currently no vids saved.'
    text = input.group(2)
    try:
        fn = open('vids.txt', 'r')
    except:
        return phenny.reply('Please add a vid first.')

    lines = fn.readlines()
    if len(lines) < 1:
        return phenny.reply(NO_QUOTES)
    MAX = len(lines)
    fn.close()
    random.seed()
    try:
        number = int(text)
        if number < 0:
            number = MAX - abs(number) + 1
    except:
        number = random.randint(1, MAX)
    if not (0 <= number <= MAX):
        phenny.reply("I'm not sure which vid you would like to see.")
    else:
        if lines:
            if number == 1:
                line = lines[0]
            elif number == 0:
                return phenny.say('There is no "0th" vid!')
            else:
                line = lines[number - 1]
            phenny.reply('vid %s of %s: ' % (number, MAX) + line)
        else:
            phenny.reply(NO_QUOTES)
retrievevid.commands = ['vid','playlist']
retrievevid.priority = 'low'
retrievevid.example = '.playlist'


def delvid(phenny, input):
    '''.rmvid <number> -- removes a given vid from the database. Can only be done by the owner of the bot.'''
    if not input.owner: return
    text = input.group(2)
    number = int()
    try:
        fn = open('vids.txt', 'r')
    except:
        return phenny.reply('No vids to delete.')
    lines = fn.readlines()
    MAX = len(lines)
    fn.close()
    try:
        number = int(text)
    except:
        phenny.reply('Please enter the vid number you would like to delete.')
        return
    if number > 0:
        newlines = lines[:number - 1] + lines[number:]
    elif number == 0:
        return phenny.reply('There is no "0th" vid!')
    elif number == -1:
        newlines = lines[:number]
    else:
        ## number < -1
        newlines = lines[:number] + lines[number + 1:]
    fn = open('vids.txt', 'w')
    for line in newlines:
        txt = line
        if txt:
            fn.write(txt)
            if txt[-1] != '\n':
                fn.write('\n')
    fn.close()
    phenny.reply('Successfully deleted vid %s.' % (number))
delvid.commands = ['rmvid', 'delvid']
delvid.priority = 'low'
delvid.example = '.rmvid'


if __name__ == '__main__':
    print __doc__.strip()
