import pyttsx3 #pip install pyttsx3 for installing text to speech files
import PyPDF2  #pip install PyPDF2 for installing PDF related files
book = open('got.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(9,pages):
    page = pdfReader.getPage(9)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
