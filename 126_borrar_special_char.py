# Borrar caracteres especiales

import re

def letters_only(txt):
	return re.sub('[^A-Za-z]+', '', txt)
