from tkinter import *
from tkinter.messagebox import * 
import sys
import os


font = ('Verdana',15,'bold')
font2 = ('Verdana',45,'bold')

#fun
point=True
def btn_clk(event):
    global point
    clk = event.widget
    
    
    

    if point == True and clk['text']!="x" and clk['text']!="o":
        clk["text"] = "x"
        st = clk.grid_info()['row'],clk.grid_info()['column']
        point = False
        processx(st)
    elif point==False and clk['text']!="x" and clk['text']!="o":
        clk["text"] = "o"
        st = clk.grid_info()['row'],clk.grid_info()['column']
        point=True
        processo(st)
    

    return
click  = []
def processx(got):
    gota = assign(got)
    click.append(gota)
    click.sort()
    
    
   
    a = [1,2,3]
    b = [4,5,6]
    c = [7,8,9]
    d = [1,4,7]
    e = [2,5,8]
    f = [3,6,9]
    alpha = [a,b,c,d,e,f]
    if len(click)==3:
        for al in alpha:
            if al == click:
                showinfo("Player1 won","player1 won")
    if len(click)==4:
        for al in alpha:
            for i in range(1,10):
                if i not in al:
                    al.insert(3,i)
                    alp=al[:4]
                    alp.sort()
                    
                    if alp == click:
                        showinfo("Player1 won","player1 won")
                    
clic  = []
def processo(got):
    gota = assign(got)
    clic.append(gota)
    clic.sort()
    
    
   
    g = [1,2,3]
    h = [4,5,6]
    k = [7,8,9]
    l = [1,4,7]
    m = [2,5,8]
    n = [3,6,9]
    alph = [g,h,k,l,m,n]
    if len(clic)==3:
        for al in alph:
            if al == clic:
                showinfo("Player2  won","player2  won")
    if len(clic)==4:
        for al in alph:
            for i in range(1,10):
                if i not in al:
                    al.insert(3,i)
                    alp=al[:4]
                    alp.sort()
                    
                    if alp == clic:
                        showinfo("Player2 won","player2  won")



                
               
                

                


def assign(gote):
    if gote == (0,0):
        return 1
    if gote == (0,1):
        return 2
    if gote == (0,2):
        return 3
    if gote == (1,0):
        return 4
    if gote == (1,1):
        return 5
    if gote == (1,2):
        return 6
    if gote == (2,0):
        return 7
    if gote == (2,1):
        return 8
    if gote == (2,2):
        return 9

    


def clr():
    python = sys.executable
    os.execl(python, python, * sys.argv)



    

window = Tk()
window.title("Tic Tac Toe")
window.geometry("500x500")

frame = Frame(window)
frame.pack(side=TOP)

onebtn = Button(frame,font=font,width=5,relief="ridge",activebackground='orange',activeforeground='white')
onebtn.grid(row=0,column=0)

twobtn = Button(frame,font=font,width=5,relief="ridge",activebackground='orange',activeforeground='white')
twobtn.grid(row=0,column=1)

threebtn = Button(frame,font=font,width=5,relief="ridge",activebackground='orange',activeforeground='white')
threebtn.grid(row=0,column=2)

fourbtn = Button(frame,font=font,width=5,relief="ridge",activebackground='orange',activeforeground='white')
fourbtn.grid(row=1,column=0)

fivebtn = Button(frame,font=font,width=5,relief="ridge",activebackground='orange',activeforeground='white')
fivebtn.grid(row=1,column=1)

sixbtn = Button(frame,font=font,width=5,relief="ridge",activebackground='orange',activeforeground='white')
sixbtn.grid(row=1,column=2)

sevenbtn = Button(frame,font=font,width=5,relief="ridge",activebackground='orange',activeforeground='white')
sevenbtn.grid(row=2,column=0)

eightbtn = Button(frame,font=font,width=5,relief="ridge",activebackground='orange',activeforeground='white')
eightbtn.grid(row=2,column=1)
ninebtn = Button(frame,font=font,width=5,relief="ridge",activebackground='orange',activeforeground='white')
ninebtn.grid(row=2,column=2)

clrbtn = Button(window,font=font,text="clear",width=5,relief="ridge",activebackground='orange',activeforeground='white',command=clr)
clrbtn.pack(side=TOP)

        
#bind

onebtn.bind('<Button-1>',btn_clk) 
twobtn.bind('<Button-1>',btn_clk) 
threebtn.bind('<Button-1>',btn_clk) 
fourbtn.bind('<Button-1>',btn_clk) 
fivebtn.bind('<Button-1>',btn_clk) 
sixbtn.bind('<Button-1>',btn_clk) 
sevenbtn.bind('<Button-1>',btn_clk) 
eightbtn.bind('<Button-1>',btn_clk) 
ninebtn.bind('<Button-1>',btn_clk) 



        
  

window.mainloop()
