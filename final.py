from tkinter import *
from tkinter import ttk
import random
import time
import math
import threading

'''

topTimer = False

def timer():
  milisecs = 0
  while stopTimer == False:
    print("Miliseconds: "+str(milisecs))
    milisecs += 1
    time.sleep(0.1)

def keyboardChecker():
  global stopTimer
  input("Press enter to stop timer")
  stopTimer = True 

y = threading.Thread(target=keyboardChecker)
y.start()

x = threading.Thread(target=timer)
x.start()
'''


def prob(chance):
    #rolls a chance. Percentage for it to suceed & return true is chance
    chn = random.randint(1,100)
    if chn <= chance:
        return True
    else:
        return False
def chklist(x,y,xrng,yrng):
    #Returns false if the x & y coordinate pairs are both in the given range via range()
    if (x in list(xrng)) and (y in list(yrng)):
        return False
    else:
        return True
def findinlist(tofind,atrb,list):
    #Finds a obj in a list, by comparing a value to every objects atribute within list, where atrb is the atribute such as obj.(X)
    for i in list:
        val = getattr(i,atrb)
        if val == tofind:
            return i
def getcordtile(x,y,tiles):
    #Finds a specific tile with the given X & Y Cords
    for i in tiles:
        if (i.X == x) and (i.Y == y):
            return i

class Tile:
    """Coordinate-Based tile system"""
    def __init__(self,Xpos,Ypos,State,Frm):
        self.X = Xpos
        self.Y = Ypos
        self.State = State
        self.Frame = Frm

root = Tk()
root.title("Test1")
tiles = []

Wall = ttk.Style()
Wall.configure('Wall.TFrame', background='grey', borderwidth=0, relief='raised')

Pla = ttk.Style()
Pla.configure("Player.TFrame",background="blue",borderwith=0,relief="sunken")

Spawnbad = ttk.Style()
Spawnbad.configure("Spawnbad.TFrame",background="red",borderwith=0,relief="sunken")

Empty = ttk.Style()
Empty.configure("Empty.TFrame",background="white",borderwith=0,relief="flat")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.geometry("1000x1000")
root.rowconfigure(0, weight=1)
root.update()
w = root.winfo_width()
h = root.winfo_height()
# print(w,h)
spacingx = w / 50
spacingy = h / 50
for y in range(50):
    for x in range(50):
        frame = ttk.Frame(mainframe,width=spacingx,height=spacingy,style="Empty.TFrame")
        tile = Tile(x,y,"empty",frame)
        frame.grid(column=x,row=y,sticky="NWES")
        frame['borderwidth'] = 0
        frame['relief'] = 'flat'
        if(prob(20) and (chklist(x,y,range(23,28),range(23,28))) and (chklist(x,y,range(9,12),range(39,42)))):
            frame["style"]="Wall.TFrame"
            tile.State = "wall"
        if(y == 25 and x == 25):
            frame["style"]="Player.TFrame"
            tile.State = "playerfrm"
        if(y == 40 and x == 10):
            frame["style"]="Spawnbad.TFrame"
            tile.State = "spawnbad"
        tiles.append(tile)



img = PhotoImage(file="C:/Users/thackssp23be/Downloads/together/grass.png")
#my_image = frame.create_image(25,25, image=img)
#badimg = 
#root.iconbitmap('c:/This PC/Downloads/together/grass.png')
#root.geometry("1000x1000")
#alien = 
#player = 
#ply = Player(25,25,tiles,root)
#ayy = hunter(40,10,tiles,root)
#for i in range(15):
#    root.after(100,ayy.move(ayy.hunt(ply)))

root.mainloop()