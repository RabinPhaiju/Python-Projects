import docx

d = docx.Document('sample.docx')
print(d.paragraphs[0].text)
