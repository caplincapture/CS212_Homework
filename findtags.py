import re

def findtags(text):
	parms = '(\w+\s*=\s*"[^"]*\s*)*' # parsing parameters, one or more word char, quoted string, zero or more parameters
	tags = '(<\s*\w+\s*' + parms + '\s*/?>)' # angle bracket, angle tag, then angle bracket
	return re.findall(tags, text)