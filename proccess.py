import re
from sat_db import cleaner, trimer

def preproccess(string):
	cleaned_string = string
	for from_clean, to_clean in cleaner.items():
		cleaned_string = cleaned_string.replace(from_clean, to_clean)
	re_string = re.sub('[^0-9a-zA-Zㄱ-ㅊ가-힣.,:?%\n ]', '', cleaned_string).split("\n")
	trim_string = ""
	for line in re_string:
		trim_line = line.strip()
		trim_line = trim_line.replace("  ", " ")
		if re.sub('[^가-힣.]', '', trim_line) in trimer:
			#print(trim_line)
			continue
		#spelled_sent = spell_checker.check(trim_line)
		#hanspell_line = spelled_sent.checked
		#trim_string += hanspell_line
		trim_string += trim_line
		trim_string += "\n"
	return trim_string
