from tkinter import *

window = Tk()

window.title("WasOnEnglish")

window.geometry('180x100')
window.resizable(width=False, height=False)

lbl = Label(window, text="הפלט הזה יהפוך למתורגם")

lbl.grid(column=0, row=5)

txt = Entry(window,width=30)

txt.grid(column=0, row=15)

l= []

def processer(txt):
  dictionary = {
      'q': '/',
      'w':"'",
      'e': 'ק',
      'r': 'ר',
      't': 'א', 
      'y': "ט",
      'u': "ו",
      'i': "ן",
      'o': "ם",
      'p': "פ",
      'a': "ש",
      's' : "ד",
      'd': 'ג',
      'f': "כ",
      'g': 'ע',
      'h': 'י',
      'j': 'ח', 
      'k': "ל",
      'l': "ך",
      ';': "ף",
      'z': "ז",
      'x': "ס",
      'c': "ב",
      'v' : "ה",
      'b': 'נ',
      'n':"מ",
      'm': 'צ',
      ',': 'ת',
      '.': 'ץ',
      'Q': '/',
      'W':"'",
      'E': 'ק',
      'R': 'ר',
      'T': 'א', 
      'Y': "ט",
      'U': "ו",
      'I': "ן",
      'O': "ם",
      'P': "פ",
      'A': "ש",
      'S' : "ד",
      'D': 'ג',
      'F': "כ",
      'G': 'ע',
      'H': 'י',
      'J': 'ח', 
      'K': "ל",
      'L': "ך",
      ';': "ף",
      'Z': "ז",
      'X': "ס",
      'C': "ב",
      'V' : "ה",
      'B': 'נ',
      'N':"מ",
      'M': 'צ',
      ',': 'ת',
      '.': 'ץ',
      }
  transTable = txt.maketrans(dictionary)
  txt = txt.translate(transTable)
  a = txt
  print(txt)
  l.append(a)
  

def clicked():

    res =  "" + txt.get()
    a = processer(res)
    b = lbl.configure(text= ""+l[0])
    c2c(l[0])
    l.clear()

    
def c2c(word): #fixed

    window.clipboard_clear()
    window.clipboard_append(word)
    window.update()


    

btn = Button(window, text="תרגום", command=clicked)

btn.grid(column=0, row=0)

lbl2 = Label(window, text="שיט, הייתי על אנגלית")
lbl2.grid(column=0, row=8)




window.mainloop()
