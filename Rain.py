#Making rain python

import tkinter
import random




class rainDrop:
    #raindrop object starting position
    def __init__(self, canvas, x, y, vertspeed, horizspeed,colour):
        self.x = x
        self.y = y
        self.vertspeed = vertspeed
        self.horizspeed = horizspeed
        self.vertresetspeed = vertspeed
        self.horizresetspeed = horizspeed
        self.colour = colour
        self.canvas = canvas
        coord = self.x, self.y, (self.x + horizspeed*3), (self.y + vertspeed*3)
        self.rdrop = canvas.create_line(coord, fill = colour)

    def fall(self):
        #raindrop fall
        deltay = self.vertspeed
        self.vertspeed = self.vertspeed 
        deltax = self.horizspeed 
        self.horizspeed = self.horizspeed 
        self.canvas.move(self.rdrop, deltax, deltay)
        self.canvas.after(30, self.fall)
        if self.canvas.coords(self.rdrop)[3]>= canvas.winfo_height() and self.vertspeed>=0 or self.canvas.coords(self.rdrop)[1]<= 0 and self.vertspeed<=0:
            # print(self.canvas.coords(self.rdrop))
            self.vertspeed = -random.uniform(0.1,1.5)*self.vertspeed
        if self.canvas.coords(self.rdrop)[0] >= canvas.winfo_width() and self.horizspeed >= 0 or self.canvas.coords(self.rdrop)[0] <=0 and self.horizspeed <= 0:
            self.horizspeed = -random.uniform(0.1,1.5)*self.horizspeed
            # self.canvas.coords(self.rdrop, self.x, 0, self.x, 30)




#tkinter canvas info
root = tkinter.Tk()
root.title("Rain")
bgcolour = "Black"
H = 450
W = 900
canvas = tkinter.Canvas(root, bg=bgcolour, height=H, width=W)
canvas.pack()

#rainDrop1 = rainDrop(canvas, 400, 0, 1 , "red")
#rainDrop1.fall()

def pick_color():
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
    random.shuffle(colors)
    return colors[0]

dropamount = 100
for drops in range(0,dropamount):
    #drops = rainDrop(canvas, W/2, H/2, random.uniform(-5,5), random.uniform(-5,5), pick_color())
    drops = rainDrop(canvas, random.uniform(0,900), 0, random.uniform(3,5),random.uniform(-5,5), pick_color())
    drops.fall()

root.mainloop()