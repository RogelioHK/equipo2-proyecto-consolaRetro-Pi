from pyPS4Controller.controller import Controller

class control(Controller):
	def __init__(self, **kwargs):
		Controller.__init__(self, **kwargs)

	def on_options_press(self):
		print("x")

	def on_R2_press(self, value):
		print("")

c0 = control(interface="/dev/input/js0", connecting_using_ds4drv=False)
c0.listen(timeout=60)
