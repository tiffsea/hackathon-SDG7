import pandas as pd
import numpy as np
import PyPDF2
import textract

"""
Created on Fri Jul 24 18:32:48 2020

@author: Paula del Castillo
"""

class pdf_extraction():

    def __init__(self, fns):
        self.fileNames = fns
        self.pdfs = []
        self.set_pdfs_as_text()

    def set_pdfs_as_text(self):
        for f in self.fileNames:
            pdf = self.extractText(f)
            self.pdfs.append([pdf])

    def get_pdfs_as_text(self):
#         return [f for f in self.pdfs]
        return self.pdfs

    def extractText(self, filename):
        pdfFileObj = open(filename, 'rb')  # open allows you to read the file
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  # The pdfReader variable is a readable object that will be parsed
        num_pages = pdfReader.numPages  # discerning the number of pages will allow us to parse through all the pages

        count = 0
        text = ""

        while count < num_pages:  # The while loop will read each page
            pageObj = pdfReader.getPage(count)
            count += 1
            text += pageObj.extractText()

        # Below if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.

        if text != "":
            text = text

        # If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text

        else:
            text = textract.process('http://bit.ly/epo_keyword_extraction_document', method='tesseract', language='eng')

            # Now we have a text variable which contains all the text derived from our PDF file.

        return text