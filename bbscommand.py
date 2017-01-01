import json

# Validates to see if the user possesses the appropriate POWER 
# and PRESTIGE to perform the command
def authCommand():
	#TODO(richorr) Add the validation code
	return true 

def modemconnect(phone):
	with open('data/bbs.json') as f:
		bbsdata = json.load(f)
	bbsToConnect = [bbs for bbs in bbsdata['bbslist'] if bbs['phone'] == phone]
	print(bbsToConnect)
	#TODO(richorr) Update user state
	return bbsToConnect

def modemdisconnect(phone):
	#TODO(richorr) Add disconnect code - reset the users connect state
	return "not implemented"

def modemlist(prestige):
	with open('data/bbs.json') as f:
		bbsdata = json.load(f)
	count = 0
	bbslist = []
	for bbs in bbsdata['bbslist']:
		if bbs['minPrestige'] <= prestige:
			bbslist.append("[{}] {} - {}\n".format(count, bbs['name'], bbs['phone']))
			count+=1
	print(bbslist)
	return bbslist

