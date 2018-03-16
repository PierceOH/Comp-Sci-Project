from tkinter import *
import time
root = Tk()
root.title("Road map project")# labels the window popup.
root.geometry("1600x800")#dimensions of gui.

Tops = Frame(root,width = 1600,height = 100, bg = "powder blue", relief = SUNKEN)
Tops.pack(side = TOP)
F2 = Frame(root,width = 1600,height = 200, bg = "red", relief = SUNKEN)
F2.pack(side = BOTTOM)
F1 = Frame(root,width = 1600,height = 700, bg = "red", relief = SUNKEN)
F1.pack(side = LEFT)





lblInfo = Label(Tops,font = ('webdings',50,'bold'),text = "cheese anQQQQQd crackers ",fg = "Steel Blue",bd = 10,anchor = 'w')
lblInfo.grid(row = 0,column = 0)


localtime = time.asctime(time.localtime(time.time()))
curr_time = Label(F2,font = ('wingdings',30,'bold'),text = "        Made by Pierce O'Hara-Wild 2018" ,fg = "Steel Blue",bd = 10,anchor = 'w')
curr_time.grid(row = 0,column = 0)
root.mainloop()
