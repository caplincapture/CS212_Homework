def search(pattern, text):
    """Return true if pattern appears anywhere in text
	   For example, match(your_code_here, text)"""
    if pattern.startswith('^'):
        return match(pattern[1:], text) 
    else:
        return match('.*'+ pattern, text) 

def match(pattern, text):
    if pattern == '': # if the pattern is the empty string, then that matches anything, 
    				  # even if text is empty, return True
        return True
    elif pattern == '$': 
        return (text == '') # the dollar sign means that matches only at the very end of the text, 
        					# return True only if text is empty string, parentheses is a convention
    elif len(pattern) > 1 and pattern[1] in '*?':
    	return True
    else: # already dealt with first character, now dealing with next ones
        return (match1(pattern[0], text) and match(pattern[1:], text[1:])) 