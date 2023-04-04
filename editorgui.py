import tkinter as tk,tkinter
guiwindow=tkinter.Tk()
guiwindow.title("代码编辑器")
guiwindow.geometry('1200x700')
maintext=tkinter.Text(guiwindow,height=20)
maintext.place(x=0,y=0)
menubar=tk.Menu(guiwindow)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
guiwindow.config(menu=menubar)

guiwindow.mainloop()
