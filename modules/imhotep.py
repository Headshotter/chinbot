"""
imhotep - imhotep is invisible !
thanks gobi :3
"""
def imhotep(phenny, input):
	text=input.group().split()
	for x in text:
		if x=="imhotep":
			phenny.say("Imhotep is invisible !")
	try:
		var = text[0]
		if var=='rate':
			phenny.say('rated')
	except:
		var=0	
	
imhotep.event = 'PRIVMSG'
imhotep.rule= r'(.*)'
imhotep.priority = 'medium'

if __name__ == "__main__":
    print __doc__.strip()

