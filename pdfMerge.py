import PyPDF2

pdfMerge = PyPDF2.PdfMerger()
pdfFiles = [] #Provide the paths for the pdf files you want to combine
for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    pdfMerge.append(pdfReader)
    pdfFile.close()
pdfMerge.write('merged.pdf')