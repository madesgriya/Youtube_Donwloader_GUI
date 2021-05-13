from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x350')
root.title('Youtube Video Downloader')

def download():
    try:
        myVar.set('Downloading...')
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set('Video downloaded successfully')
    except Exception as e:
        myVar.set('Error, incorrect Link')
        root.update()
        link.set('Enter correct link')

Label(root, text="Welcome to Matt's YouTube Downloader", font="Consolas 15 bold").pack()
myVar = StringVar()

myVar.set('Enter the link under the line below')
Entry(root, textvariable=myVar, width=40).pack(pady=10)

link = StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)

Button(root, text='Download Now', command=download).pack()

root.mainloop()