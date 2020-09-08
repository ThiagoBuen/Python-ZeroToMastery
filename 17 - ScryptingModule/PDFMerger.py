import PyPDF2
import sys


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('./pdfFiles/super.pdf')

if __name__ == "__main__":
    inputs = sys.argv[1:]
    pdf_combiner(inputs)