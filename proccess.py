# from PyPDF2 import PdfReader
import fitz
import re
import sys
import sat_db
# from hanspell import spell_checker

cleaner = {
	"ⓐ": "a",
	"ⓑ": "b",
	"ⓒ": "c",
	"ⓓ": "d",
	"ⓔ": "e",
	"ⓕ": "f",
	"ⓖ": "g",
	"[A]": "A",
	"[B]": "B",
	"[C]": "C",
	"[D]": "D",
	"[E]": "E",
	"[F]": "F",
	"㉠": "ㄱ",
	"㉡": "ㄴ",
	"㉢": "ㄷ",
	"㉣": "ㄹ",
	"㉤": "ㅁ",
	"㉥": "ㅂ",
	"㉦": "ㅅ",
	"㉧": "ㅇ",
	"㉨": "ㅈ",
	"㉩": "ㅊ",
	"(가)": "가",
	"(나)": "나",
	"(다)": "다",
	"(라)": "라",
	"(마)": "마",
	"(바)": "바",
	"이 문제지에 관한 저작권은 한국교육과정평가원에 있습니다": "",
	"학년도 대학수학능력시험 문제지": "",
	"\n": "",
	".": ".\n",
	"?": "?\n",
	"짝수형": "",
	"홀수형": "",
	"화법과 작문": "",
	"언어와 매체": "",
	"  ": " ",
}

trimer = [
	"확인사항답안지의해당란에필요한내용을정확히기입표기했는지확인하시오.",
	"이어서선택과목문제가제시되오니자신이선택한과목인지확인하시오.",
	"다음글을읽고물음에답하시오.",
	"제교시.",
	".",
	"",
]

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
	

f = open('text.txt', 'w')

for file in files.values:
	with fitz.open(f'{file}.pdf') as doc:
	# reader = PdfReader(f'{file}.pdf')
	# for page in reader.pages:
		for page in doc:
			text = preproccess(page.get_text())
			print(text.split("\n")[0])
			f.write(text)
      
f.close()
