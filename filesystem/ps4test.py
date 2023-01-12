from pyPS4Controller.controller import Controller
import threading
import time


actual = 0
end = 0
release = False

def isUntilPressed():
	global actual
	global end
	global release

	actual = time.time()
	while release == False:
		end = time.time()
		if(end - actual > 3):
			print("Hola")

class control(Controller):
	def __init__(self, **kwargs):
		Controller.__init__(self, **kwargs)

<<<<<<< HEAD
	def on_options_press(self):
		actual = 0
		end = 0
		pressed = threading.Thread(target = isUntilPressed, args = ())
		pressed.start()
		#print(on_options_release())

	def on_options_release(self):
		global release
		global actual, end
		release = True
		print("actual: ", actual)
		print("edn: ", end)
		release = False
=======
#	def on_options_press(self):
#		print("x")

>>>>>>> d96ec68958b10586f2e69c30ccd261bba2e46a03
#	def on_R2_press(self, value):
#		pass

#	def on_R2_release(self):
#		pass

#	def on_L2_press(self, value):
#		pass

#	def on_L2_release(self):
#		pass

def konami_callback():
	print("a")

def ms():
	return [{"inputs": ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'share', 'options'], "callback": konami_callback}]

c0 = control(interface="/dev/input/js0", connecting_using_ds4drv=False)
c0.listen(timeout=60, on_sequence=ms())
