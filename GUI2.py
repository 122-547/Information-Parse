from tkinter import *
from main2 import ParseInformation
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def main():
       global root
       url = custom_url.get()
       if custom_url.get() == " Url":
              url = "https://ru.wikipedia.org/wiki/"
       
       ps = ParseInformation(ent_word.get(), url)
       
       if scr.get("1.0", END) != "":
              scr.delete("1.0", END)
       
       for i in ps.Parse():
              scr.insert(END, f"{i}\n\n")
       if text_errors != "":
              text_errors.delete("1.0", END)
       text_errors.insert("1.0", ps.result_status + ps.result_status2)

def sch_word_focus_out(*args):
       if ent_word.get() == "":
              ent_word["fg"] = "grey"
              ent_word.insert("0", " Search Word")

def sch_word_focus_in(*args):
       ent_word.delete("0", "end")
       ent_word["fg"] = "black"

def custom_url_focus_out(*args):
       if custom_url.get() == "":
              custom_url["fg"] = "grey"
              custom_url.insert("0", " Url")

def custom_url_focus_in(*args):
       custom_url.delete("0", "end")
       custom_url["fg"] = "black"

root = Tk()
root.title("")

trys = 0
result_persent = 0
persent = 0
error = ""
root.resizable(0, 0)
root.geometry("900x500")
root["bg"] = "#CACACA"

image = PhotoImage(file="image.png")
root.iconphoto(False, image)

text = Text(wrap="word")
text.pack(anchor=NW, padx=10, pady=10)

text_errors = Text(wrap="word", width=990)
text_errors.pack(anchor=SW, padx=10, pady=10)

ent_word = Entry(root)
ent_word.place(height=20, width=200, x=688, y=10)
ent_word.bind("<FocusIn>", sch_word_focus_in)
ent_word.bind("<FocusOut>", sch_word_focus_out)

custom_url = Entry(root)
custom_url.place(height=20, width=200, x=688, y=40)
custom_url.bind("<FocusIn>", custom_url_focus_in)
custom_url.bind("<FocusOut>", custom_url_focus_out)

main_but = ttk.Button(root, command=main, text="Start Search")
main_but.place(height=25, width=200, x=688, y=70)


scr = ScrolledText(text, wrap=WORD)
scr.pack(fill="both", expand=True)

sch_word_focus_out()
custom_url_focus_out()

root.mainloop()