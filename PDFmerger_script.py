# Merge multiple pdfs together
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from pathlib import Path
import sys
import os
import collections

pdfs = []
# pdfs = collections.OrderedDict()

merger = PdfMerger()

new_name = str(input("Mergered PDF Name: "))
number_pdfs = int(input("# of PDF merging: "))

print("Enter PDFs in wanted order. ")

for i in range(0, number_pdfs):
    pdf = input("Original PDF: ")
    pdfs.append(f"{pdf}.pdf")
    print(f"{pdf} was added. ")
    print("PDFs merging from left to right: ")
    print(*pdfs, sep =" ")

#for file in os.listdir(os.curdir):
    # if file.endswith("pdf"):
        # file_new_name = open(new_name, "wb") 

for file in pdfs:
        merger.append(file)       
merger.write(f"{new_name}.pdf")
pdfs.clear()
merger.close()
exit()