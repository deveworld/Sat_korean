from download import download
from proccess import preproccess
from sat_db import url, files

if __name__ == "__main__":
  print("downloading...")
    for hash, name in files.items():
      download(f"{url}{hash}", name)
  print("")
  print("checking...")
  for name in files.values():
    if not os.path.exists(f"{name}.pdf"):
      print(f"{name}.pdf not exists! It may be an error.")
  print("downloading done")
  print("")
  print("proccessing to 'text.txt' ...")
  
  f = open('text.txt', 'w')
  for file in files.values:
	  with fitz.open(f'{file}.pdf') as doc:
		for page in doc:
			text = preproccess(page.get_text())
			print(text.split("\n")[0])
			f.write(text)
  f.close()
  
  print("proccessing done")
