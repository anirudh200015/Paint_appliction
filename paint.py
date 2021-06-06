#importing modules
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import *
from tkinter.colorchooser import askcolor
class Paint(object):

    pen_size = 5.0
    ink_color = 'black'

    def __init__(self):
        self.root = Tk()#initializing the Tkinter
        #pen
        self.pen = Button(self.root, text='pen', command=self.use_pen)#setup the Button for PEN
        self.pen.grid(row=0, column=0)#set up button grid
        #brush
        self.brush = Button(self.root, text='brush', command=self.use_brush)#setup Brush button
        self.brush.grid(row=0, column=1)#set up button grid
        #color-chooser
        self.color_button = Button(self.root, text='color', command=self.choose_color)#setup Color button
        self.color_button.grid(row=0, column=2)#set up button grid
        #eraser
        self.eraser = Button(self.root, text='eraser', command=self.use_eraser)#setup eraser button        
        self.eraser.grid(row=0, column=3)  #set up button grid
        #choose-size
        self.choose_size = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)#setup size scale
        self.choose_size.grid(row=0, column=4)#set up button grid
        #paint window
        self.draw_canvas = Canvas(self.root, bg='white', width=600, height=600)#setup canvas
        self.draw_canvas.grid(row=1, columnspan=5)#set up button grid



        self.setup()
        self.root.mainloop()

    def setup(self):   
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size.get()
        self.color = self.ink_color
        self.eraser_on = True
        self.active_button = self.pen
        self.draw_canvas.bind('<B1-Motion>', self.paint)
        self.draw_canvas.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self): 
        self.activate_button(self.pen)

    def use_brush(self): 
        self.activate_button(self.brush)

    def choose_color(self): 
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self): 
        self.activate_button(self.eraser, eraser_mode=True)

    def activate_button(self, button, eraser_mode=False): 
        self.active_button.config(relief=RAISED)
        button.config(relief=SUNKEN)
        self.active_button = button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.draw_canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event): 
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()        
