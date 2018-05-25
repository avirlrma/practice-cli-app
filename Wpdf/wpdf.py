import PyPDF2
import sys

def getPages():
	fileName = sys.argv[1]
	f = open(fileName,'rb')
	pdfObj = PyPDF2.PdfFileReader(f)
	print(pdfObj.getNumPages())
