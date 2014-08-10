import time

isvote = 0
votenum = 0
voted=[]
nick=''
def votekick(phenny, input):
	text=input.group()
	if isvote == 0:
		global nick
		nick = text.split(' ')[1]
		phenny.say("Vote to kick %s in the next 60 seconds" % (nick))
		phenny.say("give %s the boot ,drop a line saying '.vote yes' or '.vote no'" % (nick))
		global isvote
		global votenum
		global voted
		isvote=1
		votenum=0
		time.sleep(60)
		if votenum > 2:
			phenny.say("THEN IT IS DECIDED !!!")
			channel = input.sender
			reason = "kick by vote!"
			phenny.write(['KICK', '%s %s :%s' % (input.sender, nick, 'kick by vote !')])
		else:
			phenny.say("kick by vote failed ,only %s /3 votes" % (votenum))
		votenum=0
		isvote=0
		voted=[]
	else:
		phenny.say("we are already in a vote nigger")
votekick.commands = ['votekick']
votekick.priority = 'high'
	
def votecount(phenny, input):
	global isvote
	global votenum
	text=input.group()
	if isvote==1:
		if input.nick in voted or input.nick==nick:
			phenny.say("%s :You think this a motherflipping game,i think nod :DDDD" % (input.nick))
		else:
			if text.split(' ')[1]=="yes":
				phenny.say("vote accepted ! %s /3" % (votenum+1))
				votenum += 1
				voted.append(input.nick)
			elif text.split(' ')[1]=="no":
				phenny.say("vote accepted ! %s /3" % (votenum-1))
				votenum -= 1
				voted.append(input.nick)

			else:
				phenny.say("vote rejected !")
	else:
		phenny.say("were not voting yet nigger ,.votekick! <nick> to begin voting")
votecount.commands =['vote']
votecount.priority = 'medium'


if __name__ == "__main__":
    print __doc__.strip()

