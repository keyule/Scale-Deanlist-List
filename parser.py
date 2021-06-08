import PyPDF2
import os
import csv

dirname = os.path.dirname(__file__)
directory = os.path.join (dirname,'PDFS','20202021Sem1')

certID = ["certID"]
name = ["Name"]
major = ["Major"]


for filename in os.listdir(directory):

    #add certID to certID array
    certID.append((filename.partition('.')[0]))

    #grab text
    completePath = os.path.join(directory,filename)
    pdfFileObj = open(completePath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()

    #get name
    textname = text.partition('that')[2]
    textname = textname.partition('has')[0]
    name.append(textname)
    
    #get major
    textmajor = text.partition('2020/2021')[2]
    textmajor = textmajor.partition('Dean')[0]
    major.append(textmajor)


with open('list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(certID)):
        writer.writerow([certID[i], name[i], major[i]])


