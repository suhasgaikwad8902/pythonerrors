from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_input = r"/home/suhas/Desktop/mech.pdf"
sample = open(pdf_input, mode = 'rb')  # PATH OF PDF FILE -->> C:\comp.pdf
pdfdoc = PdfFileReader(sample)
num = pdfdoc.numPages
print(num)
path = r"/home/suhas/Desktop/new/dff"

for i in range(0,num-1,2):
    page = pdfdoc.getPage(i)
    page_content = page.extract_text()
    new = page_content[:page_content.find("CONFIDENTIAL")]
    new1 = page_content[page_content.find("CONFIDENTIAL"):] + "\n" + pdfdoc.getPage(i+1).extract_text()
    with open(path+"{}".format(i), 'w') as t:
        t.write(new)
    with open(path+"{}".format(i+1), 'w') as t:
        t.write(new1)
