# thanks to: http://www.daniweb.com/forums/thread65288.html
from tkinter import *  # order seems to matter: import Tkinter first
#import Image, ImageTk  # then import ImageTk
from PIL import Image,ImageTk
class MyFrame(Frame):
    def __init__(self, master, im):
        Frame.__init__(self, master)
        self.caption = Label(self, text="Is this the map you would like to run the script on.")
        self.caption.grid()
        self.image = ImageTk.PhotoImage(im) # <--- results of PhotoImage() must be stored
        self.image_label = Label(self, image=self.image, bd=0) # <--- will not work if 'image = ImageTk.PhotoImage(im)'
        self.image_label.grid()
        self.grid()

im = Image.open("map.png") # read map from disk

# or you could use the PIL image you created directly via option 2 from the URL request ...
mainw = Tk()
mainw.frame = MyFrame(mainw, im)
mainw.mainloop()