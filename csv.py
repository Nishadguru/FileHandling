import PyPDF2

with open ('b.pdf','rb') as read_file:
	pdf_reader = PyPDF2.PdfFileReader(read_file)
	print(pdf_reader.numPages())
	pageObj=pdf_reader.getpage(0)
	print(pageobj.extractText())
