from easyocr import Reader

def ocr(location, langs):
	print("starting ocr...")
	reader = Reader(langs)
	results = reader.readtext(location)
	print("ocr done...")
	res = ""
	for (bbox, text, prob) in results:
		res = res + text + "\n"

	return res

