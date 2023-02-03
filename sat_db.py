url = "https://www.kice.re.kr/boardCnts/fileDown.do?fileSeq="

files = {
  "e55bd7816384388ffe786eb80d114589": "2023",
  # "6c164b64404b8f7ba92ac594fc69b36a": "2023-answer",
  "86d6f3be90d0815c863d5fe7c6d1d68c": "2022",
  # "f7683448be641c3b3f47900702ea29f2": "2022-answer",
  "c7ee9e67af649ecc4d45a7efc2979554": "2021",
  # "2717cf72fddf9944797408310a50239c": "2021-answer",
  "09774bbd708c3ea06c6063b0d07c6268": "2020",
  # "763665c2cfc4913cc4ab34660f12f12d": "2020-answer",
  "43c44a90c7d9fcbce72b442d1c5ab2f6": "2019",
  # "1315d626bb849b8ee39aad13fe5f3ed9": "2019-answer",
  "385e41cc2c1f55e0cfd901388a7674df": "2018",
  # "1f2c7f709dbed47ecede85156e83aa96": "2018-answer",
  "3da2d1fc7392160a6ed98783c257a218": "2017",
  # "8a8c8595663de38d8aa8d1277c8a9987": "2017-answer",
  "5cdd51c4ca410ca619c82dd73c537c57": "2016-A",
  # "5cdd51c4ca410ca619c82dd73c537c57": "2016-A-even",
  # "8db7830de319b3756c36f508418f6383": "2016-A-odd",
  "ff95daab1c3418bfdd328e4c798150d9": "2016-B",
  # "ff95daab1c3418bfdd328e4c798150d9": "2016-B-even",
  # "3b97bc094cd03f26cf63877e82dd6f2b": "2016-B-odd",
  # "1c039677019542a9ab66cb75adf6de00": "2016-answer",
  "03f5cef084175ac87e375001e7406f67": "2015-A", # 2015 doesn't have even.
  # "03f5cef084175ac87e375001e7406f67": "2015-A-odd", # 2015 doesn't have even.
  # "b8c1643c0fc9ab1d079e2437a5962691": "2015-A-odd-answer",
  "321c5a7d8c1c22d4862f856e0aec7ba7": "2015-B",
  # "321c5a7d8c1c22d4862f856e0aec7ba7": "2015-B-odd",
  # "b9b3295f0ae7a649873a097bb966031e": "2015-B-odd-answer",
  "91d371872e7cb73bef41dd74231b06d5": "2014-A", # 2014 doesn't have even, too.
  # "91d371872e7cb73bef41dd74231b06d5": "2014-A-odd", # 2014 doesn't have even, too.
  # "8ee8da1f11072b947f01c07fe945cf71": "2014-A-odd-answer",
  "3e8e60dedd2ebfeccbb0e42eb3760afa": "2014-B",
  # "3e8e60dedd2ebfeccbb0e42eb3760afa": "2014-B-odd",
  # "2f366a8f207c7ab63ae08302f8346a10": "2014-B-odd-answer",
}

# 2017 ~ 2022 is zip file.
zip_files = [
  "2017", "2018", "2019", "2020", "2021", "2022",
]

# In linux, some file name glitch.
# I'm not sure at this problem also occurs in Windows.
unzip_files = {
  "2022": {
    "▒╣╛ε┐╡┐¬_┬ª╝÷╟ⁿ.pdf": "2022",
    # "▒╣╛ε┐╡┐¬_┬ª╝÷╟ⁿ.pdf": "2022-even",
    # "▒╣╛ε┐╡┐¬_╚ª╝÷╟ⁿ.pdf": "2022-odd",
  },
  "2021": {
    "1▒│╜├_▒╣╛ε┐╡┐¬_┬ª.pdf": "2021",
    # "1▒│╜├_▒╣╛ε┐╡┐¬_┬ª.pdf": "2021-even",
    # "1▒│╜├_▒╣╛ε┐╡┐¬_╚ª.pdf": "2021-odd",
  },
  "2020": {
    "▒╣╛ε_┬ª.pdf": "2020",
    # "▒╣╛ε_┬ª.pdf": "2020-even",
    # "▒╣╛ε_╚ª.pdf": "2020-odd",
  },
  "2019": {
    "▒╣╛ε_┬ª.pdf": "2019",
    # "▒╣╛ε_┬ª.pdf": "2019-odd",
    # "▒╣╛ε_╚ª.pdf": "2019-even",
  },
  "2018": {
    "▒╣╛ε_┬ª.pdf": "2018",
    # "▒╣╛ε_┬ª.pdf": "2018-odd",
    # "▒╣╛ε_╚ª.pdf": "2018-even",
  },
  "2017": {
    "▒╣╛ε_┬ª╝÷.pdf": "2017",
    # "▒╣╛ε_┬ª╝÷.pdf": "2017-odd",
    # "▒╣╛ε_╚ª╝÷.pdf": "2017-even",
  },
}
