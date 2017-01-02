import netrc
#import bcrypt

class dbconnectionsinfo:

	def __init__(self, environment='dev'):
		self.environment = environment
		self.machinename = 'mysql'
		self.host = 'localhost'
		self.username = 'bbs'
		self.db = '80sBBS'

		self.pwd = ''
		if environment == 'dev':
			# Read from the .netrc file in your home directory
			secrets = netrc.netrc()
			hostinfo = secrets.authenticators(self.machinename)
			self.pwd = hostinfo[2]
 
# For potential future use:
# def generatedbsecrets(host, username, rawpassword, mastersecretkey):
# 	salt = bcrypt.gensalt()
# 	saltedpassword = rawpassword + salt + mastersecretkey
# 	hashedpassword = bcrypt.hashpw(combo_password, salt)
