from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

pdfWatermark = PdfFileReader(open('./pdfFiles/wtr.pdf','rb'))
#pdfFile1       = PdfFileReader(open('./pdfFiles/super.pdf','rb'))
output = PdfFileWriter()

def watermarkPDFs(pdfFiles):

    fileNum = 0

    for pdf in pdfFiles:

        pdfFile = PdfFileReader(open(pdf,'rb'))

        for i in range(pdfFile.getNumPages()):
            page = pdfFile.getPage(i)
            page.mergePage(pdfWatermark.getPage(0))
            output.addPage(page)

        with open(f'./pdfFiles/watermarkedPDF{fileNum}.pdf', 'wb') as file:
            output.write(file)
        fileNum += 1

if __name__ == '__main__':
    inputs = sys.argv[1:]
    watermarkPDFs(inputs)

