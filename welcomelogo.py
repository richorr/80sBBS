from pyfiglet import Figlet

def formatlogo(logo, font):
	plaintext = Figlet (font)
	formattedText = "<pre>" + plaintext.renderText(logo) + "</pre>"
	return formattedText

