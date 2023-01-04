import os
import time
import tkinter as tk
from tkinter import Label, Entry
import threading
from pyPS4Controller.controller import Controller
#from pyPS4Controller.event_mapping.DefaultMapping import DefaultMapping
import mount

window = tk.Tk()	#Comment when using SSH
lbl0 = Entry(window, bg="grey", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl0.place(x=10, y=10, width=1280, height = 50)

ROMS_DIR = "~/ROMS/"
roms = []
actual = 0
open_close = 0

class Control(Controller):
	def __init__(self, **kwargs):
		Controller.__init__(self, **kwargs)

	def on_playstation_button_press(self):
		global roms
		global actual
		global open_close
		global actualGame

		open_close += 1
		print(open_close)
		if open_close == 2:
			os.system("sudo pkill bsnes")
			open_close = 0
		else:
			defRom = "~/bsnes-plus/bsnes/out/bsnes ~/ROMS/" + "\"" + roms[actual] + "\""
			actualGame = threading.Thread(target=os.system, args=[defRom])
			actualGame.start()
			#os.system("~/bsnes-plus/bsnes/out/bsnes ~/ROMS/" + "\"" + roms[actual] + "\"")

	def on_playstation_button_release(self):
		print("")

	def on_up_arrow_press(self):
		updateActualRom(1)

	def on_up_arrow_release(self):
		print("")

	def on_up_down_arrow_release(self):
		print("")

	def on_down_arrow_press(self):
		updateActualRom(-1)

	def on_down_arrow_release(self):
		print("")

	def on_share_press(self):
		os.system("ps T")
	def on_share_release(self):
		os.system("ps T")

def updateActualRom(num):
	global actual
	global roms
	global window

	actual += num
	if (actual >= len(roms)):
		actual = 0
	elif (actual < 0):
		actual = len(roms) - 1
	print(roms[actual])
	lbl0.delete(0, 'end')
	lbl0.insert(0,roms[actual].split(".")[0])

#Funtion to read the local ROMS directory and initialize de roms global list
def readActualRoms():
	global roms
	actualroms = os.popen("ls ~/ROMS/").readlines()
	for ar in actualroms:
		roms.append(ar.split("\n")[0])
	roms.sort()

#Function to read the external ROMS directory
def readRoms():
	global roms
	data = 0
	while True:
		data =  mount.isAvailableDrive()
		if data :
			updateRoms(mount.getFiles(data, roms))
		time.sleep(2)

#Function to update the roms global list
def updateRoms(newRoms):
	global roms
	if (len(newRoms) > 0):
		for nr in newRoms:
			if nr not in roms:
				roms.append(nr)
	else:
		print("No new ROMS")
	roms.sort()

#Function to start the GUI
def startGui():
	global window
	global roms
	global actual

	window.geometry("1280x1024")
	bt1 = tk.Button(window, text = "Close", command = closeSystem)
	bt1.pack()

	window.mainloop()

def startControl():
	c0 = Control(interface = "/dev/input/js0", connecting_using_ds4drv=False)
	c0.listen(timeout=60)

def closeSystem():
	global window
	os.system("sudo pkill python")

def main():
	global roms
	readActualRoms()
	externalDevice = threading.Thread(target = readRoms, args=())
	setControl = threading.Thread(target = startControl, args =())
	externalDevice.start()
	setControl.start()
	startGui()
#	print("Reading ROMS...")
#	actualRoms = os.popen("ls ~/ROMS/").readlines()
#	if(len(actualRoms) == 0):
#		print("No ROMS found. Reading ROMS from a external device...")
#		readRoms()
#	actualRoms = os.popen("ls ~/ROMS/").readlines()
#	print("actualRoms: ", actualRoms)
#	print("1. Metroid")
#	print("2. Super Mario World")
#	print("3. Contra III")
#	print("4. Arkanoid")
#	print("5. Super Mario All Stars")
#	print("6. Copy a external device")
#	print("7. Exit")

#	select= input("\n-> ")
#	print(select)

#	if(select == "1"):
#		os.system("~/bsnes-plus/bsnes/out/bsnes ~/ROMS/SuperMetroid.sfc")

if __name__ == '__main__':
	main()
