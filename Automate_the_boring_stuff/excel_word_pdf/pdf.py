import PyPDF2

pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages) # get total pages

# ------------- text from page 0 ------------
page1 = reader.getPage(0)
# print(page1.extractText())

# ------------- all text from pdf --------------
for pageNum in range(reader.numPages):
    pass
    # print(reader.getPage(pageNum).extractText())
pdfFile.close()


# PyPDF2 has some limitation, cant edit the text, pic
# it can reorder , remove pages, add pages


# merge two pdf
# pdf1File = open('meetingminutes1.pdf', 'rb')
# pdf2File = open('meetingminutes1.pdf', 'rb')
#
# reader1 = PyPDF2.PdfFileReader(pdf1File)
# reader2 = PyPDF2.PdfFileReader(pdf2File)
#
# writer = PyPDF2.PdfFileWriter()
# for pageNum in range(reader1.numPages):
#     page = reader1.getPage(pageNum)
#     writer.addPage(page)
#
# for pageNum in range(reader2.numPages):
#     page = reader2.getPage(pageNum)
#     writer.addPage(page)
#
# outputfile = open('combine.pdf', 'wb')
# writer.write(outputfile)
#
# outputfile.close()
# pdf1File.close()
# pdf2File.close()