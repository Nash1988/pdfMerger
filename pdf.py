import PyPDF2
import sys


inputs = sys.argv[1:] 

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    output = PyPDF2.PdfWriter()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)

    #merger.write('super.pdf')
    #merger.close()
    with open("result.pdf", "wb") as result:
        output.write(result)

pdf_combiner(inputs)