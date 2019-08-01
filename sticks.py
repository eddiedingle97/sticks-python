import tkinter as tk
import random
import math

global amount
amount = 0
random.seed()

class Dialog(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.dialog = tk.Label(self)
        self.dialog["text"] = "How many sticks would you like to drop?"
        self.dialog.pack(side="top")
        self.textfield = tk.Entry(self)
        self.textfield.pack()
        self.button = tk.Button(self, text="start", fg="blue", command=self.drop)
        self.button.pack()

    def drop(self):
        global amount
        amount = self.textfield.get()
        amount = int(amount)
        if(isinstance(amount, int)):
            self.new = tk.Toplevel(self.master)
            self.mat = Mat(self.new)

class Mat(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createFrame()
        self.draw()

    def createFrame(self):
        self.frame = tk.Canvas(self.master, width=512, height=512)
        self.frame.pack()

    def draw(self):
        self.drawLines()
        count = 0
        for i in range(amount):
            angle = random.uniform(2,0) * math.pi
            x = random.randint(32, 480)
            y = random.randint(32, 480)
            x1 = x + round(math.cos(angle) * 14)
            x2 = x - round(math.cos(angle) * 14)
            y1 = y + round(math.sin(angle) * 14)
            y2 = y - round(math.sin(angle) * 14)
            self.frame.create_line(x1, y1, x2, y2)
            if(isIntersecting(x1, x2)):
                count += 1
        result = 2 * 14 * amount
        result /= 32 * count
        print(str(result))

    def drawLines(self):
        for i in range(16, 512, 32): 
            self.frame.create_line(i, 0 , i, 512)

def isIntersecting(x1, x2):
    for i in range(x1, x2):
        if(i % 32 == 0):
            return True

root = tk.Tk()
app = Dialog(master=root)
app.mainloop()


