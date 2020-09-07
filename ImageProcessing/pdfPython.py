#PyPDF2

import PyPDF2

with open('./pdfFiles/dummy.pdf', 'rb') as file:
    #rb -> Converts from a file stream object to a binary mode
    reader = PyPDF2.PdfFileReader(file)
    #print(reader.numPages)

    page = reader.getPage(0)
    print(page.rotateClockwise(180))
    writer  = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./pdfFiles/tilt.pdf', 'wb') as newFile:
        writer.write(newFile)
    


