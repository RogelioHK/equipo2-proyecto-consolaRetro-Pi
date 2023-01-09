import os
import time
import threading
import pygame
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import Label, Entry, PhotoImage
from pyPS4Controller.controller import Controller
import mount

window = tk.Tk()	#Comment when using SSH
window['background']='#262626'

#labels and Image control. The parameter change the color, font, backgroud color adn position of the text
lbl0 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl0.place(x=10, y=10, width=1250, height = 50)

lbl1 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl1.place(x=855, y=620, width=400, height = 50)

lbl2 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl2.place(x=10, y=90, width=400, height = 50)

lbl3 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl3.place(x=10, y=140, width=400, height = 50)

lbl4 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl4.place(x=10, y=190, width=400, height = 50)

lbl5 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl5.place(x=10, y=240, width=400, height = 50)

lbl6 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl6.place(x=10, y=290, width=400, height = 50)

lbl7 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl7.place(x=10, y=340, width=400, height = 50)

lbl8 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl8.place(x=10, y=390, width=400, height = 50)

lbl9 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl9.place(x=10, y=440, width=400, height = 50)

lbla = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbla.place(x=10, y=490, width=400, height = 50)

lblb = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lblb.place(x=10, y=540, width=400, height = 50)

lblc = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lblc.place(x=10, y=590, width=400, height = 50)

img = Image.open("/home/equipo2/ROMS/pinguino default.png")
img = img.resize((100,100), Image.ANTIALIAS)

img0 = ImageTk.PhotoImage(img)
lbl_img = Label(window, image = img0, bg = "#333333").place(x = 455, y = 90, width = 800, height = 500)

ROMS_DIR = "/home/equipo2/ROMS/"
roms = []
actual = 0
open_close = 0
countStart = 0
countEnd = 0

#Class necesary for the ps4 control.
class Control(Controller):
	def __init__(self, **kwargs):
		Controller.__init__(self, **kwargs)

	def on_playstation_button_press(self):
		global countStart
		global open_close

		countStart = time.time()
		open_close += 1

	def on_playstation_button_release(self):
		global roms
		global actual
		global open_close
		global actualGame
		global countStart
		global countEnd

		countEnd = time.time()
		totalTime = countEnd - countStart

		#if (totalTime > 3):
		sound("start")
			#closeSystem()
		#else:
		if open_close == 2:
			os.system("sudo pkill bsnes")
			open_close = 0
		else:
			sound0 = threading.Thread(target = sound, args = ["emu"])
			sound0.start()
			defRom = "~/bsnes-plus/bsnes/out/bsnes ~/ROMS/" + "\"" + roms[actual] + "\""
			#defRom = "~/bsnes-plus/bsnes/out/bsnes"
			actualGame = threading.Thread(target=os.system, args=[defRom])
			actualGame.start()

	def on_up_arrow_press(self):
		sound0 = threading.Thread(target = sound, args = ["select"])
		sound0.start()
		updateActualRom(1)

	def on_down_arrow_press(self):
		sound0 = threading.Thread(target = sound, args = ["select"])
		sound0.start()
		updateActualRom(-1)

#	def on_L3_y_up(self, value):
#		sound0 = threading.Thread(target = sound, args = ["select"])
#		sound0.start()
#		updateActualRom(1)
#		time.sleep(0.5)

#	def on_L3_down(self, value):
#		sound0 = threading.Thread(target = sound, args = ["select"])
#		sound0.start()
#		updateActualRom(-1)
#		time.sleep(0.5)

#Functions to create a sequences to input into the Joystick
def konami_callback():
	print("a")

def seq():
	return [{"inputs" : ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right' 'x', 'circle'],
		"callback" : konami_callback}]

#Function to play the sound pack of the system
def sound(snd):
	pygame.mixer.init()
	if(snd == "start"):
		pygame.mixer.music.load("/home/equipo2/filesystem/audios/Soft-delay.mp3")
	elif (snd == "select"):
		pygame.mixer.music.load("/home/equipo2/filesystem/audios/select.mp3")
	elif (snd == "emu"):
		pygame.mixer.music.load("/home/equipo2/filesystem/audios/Slick.mp3")
	elif (snd == "storage"):
		pygame.mixer.music.load("/home/equipo2/filesystem/audios/Positive.mp3")
	elif (snd == "storage-out"):
		pygame.mixer.music.load("/home/equipo2/filesystem/audios/Rhodes.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
    		continue

#Function to change the Image for the image of the actual game (or use the default image if isn't)
#and change the list of games at the left side of the GUI
def updateLabels():
	global roms
	global actual
	global img
	global img0
	global lbl0
	global lbl_img

	lbl0.delete(0, 'end')
	lbl0.insert(0, roms[actual].split(".")[0])
	lbl2.delete(0, 'end')
	lbl2.insert(0, roms[len(roms) - 1 -actual].split(".")[0])
	lbl3.delete(0, 'end')
	lbl3.insert(0, roms[len(roms) - 2 - actual].split(".")[0])
	lbl4.delete(0, 'end')
	lbl4.insert(0, roms[len(roms) - 3 - actual].split(".")[0])
	lbl5.delete(0, 'end')
	lbl5.insert(0, roms[len(roms) - 4 - actual].split(".")[0])
	lbl6.delete(0, 'end')
	lbl6.insert(0, roms[len(roms) - 5 - actual].split(".")[0])
	lbl7.delete(0, 'end')
	lbl7.insert(0, roms[len(roms) - 6 - actual].split(".")[0])
	lbl8.delete(0, 'end')
	lbl8.insert(0, roms[len(roms) - 7 - actual].split(".")[0])
	lbl9.delete(0, 'end')
	lbl9.insert(0, roms[len(roms) - 8 - actual].split(".")[0])
	lbla.delete(0, 'end')
	lbla.insert(0, roms[len(roms) - 9 - actual].split(".")[0])
	lblb.delete(0, 'end')
	lblb.insert(0, roms[len(roms) - 10 - actual].split(".")[0])
	lblc.delete(0, 'end')
	lblc.insert(0, roms[len(roms) - 11 - actual].split(".")[0])

	try:
		print(ROMS_DIR + roms[actual].split(".")[0] + ".png")
		img = Image.open(ROMS_DIR + roms[actual].split(".")[0] + ".png")
		img = img.resize((795,495), Image.ANTIALIAS)
		img0 = ImageTk.PhotoImage(img)
		lbl_img = Label(window, image = img0, bg = "#333333").place(x = 455, y = 90, width = 800, height = 500)
	except:
		img = Image.open("/home/equipo2/ROMS/pinguino default.png")
		img = img.resize((100,100), Image.ANTIALIAS)
		img0 = ImageTk.PhotoImage(img)
		lbl_img = Label(window, image = img0, bg = "#333333").place(x = 455, y = 90, width = 800, height = 500)

#Function wich update the next arg on the global roms list.
# If the arg on the list is > lenght list, return to 0.
# If the arg on the list is < 0, then return to the last arg of the list
def updateActualRom(num):
	global actual
	global roms

	actual += num
	if (actual >= len(roms)):
		actual = 0
	elif (actual < 0):
		actual = len(roms) - 1
	updateLabels()

#Funtion to read the local ROMS directory and initialize de roms global list
def readActualRoms():
	global roms
	actualroms = os.popen("ls ~/ROMS/").readlines()
	for ar in actualroms:
		if ".SMC" in ar or ".smc" in ar or ".SFC" in ar or ".sfc" in ar:
			roms.append(ar.split("\n")[0])
	roms.sort()
	updateLabels()

#Function to read the external ROMS directory
def readRoms():
	global roms
	global lbl1
	data = 0

	while True:
		data =  mount.isAvailableDrive()
		if data :
			sound("storage")
			lbl1.delete(0, 'end')
			lbl1.insert(0, "Storage Detected. Reading...")
			updateRoms(mount.getFiles(data, roms))
			lbl1.delete(0, 'end')
			lbl1.insert(0, "Disconnect the Drive")
			sound("storage-out")
		else:
			lbl1.delete(0, 'end')
			lbl1.insert(0, "No Storage Detected")
		time.sleep(2)

#Function to update the roms global list
def updateRoms(newRoms):
	global roms

	if (len(newRoms) > 0):
		if ("NoROM" in newRoms):
			lbl1.delete(0, 'end')
			lbl1.insert(0, "No ROM directory")
		else:
			lbl1.delete(0, 'end')
			lbl1.insert(0, "New ROMS Detected! Copying...")

			for nr in newRoms:
				if nr not in roms:
					roms.append(nr)
	else:
		lbl1.delete(0, 'end')
		lbl1.insert(0, "No new ROMS")
	roms.sort()
	time.sleep(2)

#Function to start the GUI
def startGui():
	global window
	global roms
	global actual

	window.geometry("1280x1024")
	bt1 = tk.Button(window, text = "Close", command = closeSystem).place(x = 640, y = 650)
	window.mainloop()

#Function to start the joystick driver
def startControl():
	c0 = Control(interface = "/dev/input/js0", connecting_using_ds4drv=False)
	c0.listen(timeout=60)

#Function to stop the thread of the program
def closeSystem():
	global window
	#os.system("sudo shutdown -h now")
	os.system("sudo pkill python")

#Main function wich starts the threads of services necesaries
#for the correct functionality of the program
def main():
	global roms
	sound0 = threading.Thread(target = sound, args = ["start"])
	sound0.start()
	readActualRoms()
	externalDevice = threading.Thread(target = readRoms, args=())
	setControl = threading.Thread(target = startControl, args =())
	externalDevice.start()
	setControl.start()
	startGui()

if __name__ == '__main__':
	main()
