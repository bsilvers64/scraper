import PyPDF2

pdf=open("sample.pdf","rb") #put any pdf file here 
pdata=PyPDF2.PdfFileReader(pdf);
nop=pdata.numPages #no. of pages stored
pob=pdata.getPage(nop-1) #subrtracts one from nop index[0]
text=pob.extractText() #extracts text to text object file

file=open(r"test.text","a"); #writes file in append mode
file.writelines(text)
file.close()