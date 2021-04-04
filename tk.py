import time
from tkinter import *
import tkinter as tk  
import os
import subprocess
from PIL import ImageTk,Image
 
def check_mute2():
    command = "pactl list | sed -n '/^Source/,/^$/p' | grep Mute"

    YesText ='\tMute: no\n\tMute: yes\n'
    NoText  ='\tMute: no\n\tMute: no\n'

    output = subprocess.check_output(command,shell=True )
    output = output.decode("utf-8")
    #print(output)
    if YesText in output:
        #print ("mute")
        #root.destroy()
        return "mute"
    elif NoText in output :
        return "nomute"
    
    time.sleep(0.5)



def gui():
	def check_mute():
	    command = "pactl list | sed -n '/^Source/,/^$/p' | grep Mute"

	    YesText ='\tMute: no\n\tMute: yes\n'
	    NoText  ='\tMute: no\n\tMute: no\n'

	    output = subprocess.check_output(command,shell=True )
	    output = output.decode("utf-8")
	    #print(output)
	    if YesText in output:
	        print ("mute")
	        root.destroy()
	        #return "mute"
	    elif NoText in output :
	        #print("nomut")
	        pass
	    root.after(2000,check_mute)


	#b = input("--->")
	a = 33#a = int(b)
	root = Tk()  
	root.resizable(0, 0)





	w = a
	h = a
	x = 850
	y = 0

	frame = Frame(root)
	frame.pack()

	canvas = Canvas(frame ,highlightthickness=0, bg = "#232832" , width = w, height = h)  
	canvas.pack()

	img = ImageTk.PhotoImage(Image.open("/home/eby/Dropbox/mute-status-python/micro4.png"))
	canvas.create_image(0, 1, anchor=NW, image=img) 





	root.call('wm', 'attributes', '.', '-topmost', '1')
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))

	root.overrideredirect(1)


	#while 1 == 1 :
	#    time.sleep(1)
	#    if check_mute() == "mute":
	#        root.destroy()
	#        print("areee")
	#    else: 
	#        root.mainloop()

	root.after(2000,check_mute)

	
	root.mainloop()
gui()
while 1 == 1 :
	if check_mute2() == "nomute":
		gui()
