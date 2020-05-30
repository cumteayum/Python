from tkinter import *
import webbrowser as wb
import os
#made with love by ishan nagar with Tkinter
def clickbtn1(event):
	wb.open("github.com")

def clickbtn2(event):
	os.startfile("E:\\Videos\\takeaway.mp4")

def clickbtn3(event):
	wb.open("wikipedia.com")

root = Tk()
root.geometry("460x350")
root.title("Code-in task #2")
f = Frame(root, bg="grey")

btn1 = Button(f, text="Open GitHub", font="lucida 30 bold")

f.pack()
root.configure(background="grey")
btn1.pack(padx=20, pady=20)
btn1.bind("<Button-1>", clickbtn1)

f = Frame(root, bg="grey")
btn2 = Button(f, text="Play Video", font="lucida 30 bold")
f.pack()
btn2.pack(padx=20, pady=20)
btn2.bind("<Button-1>", clickbtn2)

f = Frame(root, bg="grey")
btn3 = Button(f, text="Open Wikipedia", font="lucida 30 bold")
f.pack()
btn3.pack(padx=20, pady=20)
btn3.bind("<Button-1>", clickbtn3)


root.mainloop()