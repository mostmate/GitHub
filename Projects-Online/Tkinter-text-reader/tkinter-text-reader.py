#tkinter text reader
from tkinter import *
def TextConvert():
    from gtts import gTTS
    import os
    root1=Tk()
    root1.title("Enter Texts to read")
    root1.iconbitmap('C:/Users/WisdomAllen/Documents/GitHub/Projects-Online/Tkinter-text-reader/textlogo-ico.ico')
    root1.geometry("400x400")
    root1.configure(bg='gray')
    def ReadTexts():
        myText=TextEntry.get()
        result=gTTS(text=myText)
        result.save('speech.mp3')
        os.system('start speech.mp3')
    TextEntry=Entry(root1, bg="cyan", fg="red")
    TextEntry.pack(ipadx=10, ipady=10, pady=50, fill='x')
    TextSubmit_btn=Button(root1, width=10, text="Read Texts", bg="white", fg="purple", command=ReadTexts)
    TextSubmit_btn.pack(ipadx=10, ipady=10, pady=110)
    root1.mainloop()
TextConvert()
#Import all from tkinter.
#import google text to speech.
#import operating system for use.
#calls tkinter and defines it as root1.
#icon can be in same directory with py file, then name.ico only specified. Convert online.
#set window size.
#set background to gray.
#create a function.
#capture Entry texts as myText.
#pass myText to gTTS text as result.
#save result as speech.mp3   .
#system to play the speech.mp3  .
#set Entry in root1, with back/foreground.
#stretch in x and y ipadding with 10 then move y padding down with 50, and expand to entire x.
#set button width, display text, set back/foreground, & run function.
#stretch in x & y ipadding with 10, and move down in y padding with 110.
#run tkinter.
#call function.

