import sys
import textwrap

def msay(str, length=40):
    return buildxbubble(str, length) + buildxmonkey()

def buildxmonkey():
    return """
        \ __ 
     w  c(..)o   (
      \__(-)    __)
          /\   (  
         /(_)___)
         w /|
          | \\
         m  m
           """

def buildxbubble(str, length=40):
    bubble = []

    lines = normalizextext(str, length)

    bordersize = len(lines[0])

    bubble.append("  " + "_" * bordersize)

    for index, line in enumerate(lines):
        border = getxborder(lines, index)

        bubble.append("%s %s %s" % (border[0], line, border[1]))

    bubble.append("  " + "-" * bordersize)

    return "\n".join(bubble)

def normalizextext(str, length):
    lines  = textwrap.wrap(str, length)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]

def getxborder(lines, index):
    if len(lines) < 2:
        return [ "<", ">" ]

    elif index == 0:
        return [ "/", "\\" ]

    elif index == len(lines) - 1:
        return [ "\\", "/" ]

    else:
        return [ "|", "|" ]


def msayxcmd(phenny, input):
    inputxtext = input.group(2)
    if inputxtext:
        banana = msay(inputxtext)
        for l in banana.rsplit('\n'):
            phenny.say(l)
msayxcmd.commands = ['msay','curitibasay']
msayxcmd.priority='low'
