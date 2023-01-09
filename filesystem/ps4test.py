from pyPS4Controller.controller import Controller

class control(Controller):
	def __init__(self, **kwargs):
		Controller.__init__(self, **kwargs)

#	def on_options_press(self):
#		print("x")

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
