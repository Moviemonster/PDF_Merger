import os
from PyPDF2 import PdfReader, PdfWriter
#import PyPDF2

#PDF Basic Merger for HP Printer Staple scan, hard coded

cur_path = os.path.dirname(__file__)
pdf1_path = os.path.relpath("..\\Test_PDF\\Sportmassage Vorderseiten.pdf", cur_path)
pdf2_path = os.path.relpath("..\\Test_PDF\\Sportmassage Rueckseiten.pdf", cur_path)

input1_PDF = PdfReader(pdf1_path)
input2_PDF = PdfReader(pdf2_path)

max_pdf1 = input1_PDF.numPages
max_pdf2 = input2_PDF.numPages


pdf_write_object = PdfWriter()

for i in range(max_pdf1):
    #print(i)
    #print((input2_PDF.numPages)-i)
    #print((input2_PDF.numPages))
    pdf_write_object.addPage(input1_PDF.getPage(i))
    pdf_write_object.addPage(input2_PDF.getPage((max_pdf2-1)-i))


out_path = os.path.relpath("..\\Test_PDF\\Test_Export.pdf",cur_path)
output = open(out_path,"wb")
pdf_write_object.write(output)

output.close()

