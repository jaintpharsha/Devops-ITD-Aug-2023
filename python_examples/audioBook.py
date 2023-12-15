import os

import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfReader(open(os.getcwd()+'/Data Science - Day 1.pdf', 'rb'))
speaker = pyttsx3.init()
for page_num in range(len(pdfReader.pages)):
    text = pdfReader.pages[page_num].extract_text()
    speaker.say(text)
    speaker.runAndWait()
    speaker.save_to_file(text, 'audio.mp3')
    speaker.runAndWait()
speaker.stop()

