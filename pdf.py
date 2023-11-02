import PyPDF2

cv = PyPDF2.PdfReader(open('CV Silvio.pdf','rb'))
print(cv)