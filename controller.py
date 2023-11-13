''' Created on Nov 10, 2023

	@author: aalp.kilic
'''

from model import Model
from view  import View

class Controller:
	def __init__(self):
		self.model = Model()
		self.view  = View(self)

	def main(self):
		self.view.main()
		
	def on_button_click(self, caption):
		result = self.model.calculate(caption)
		
		self.view.value_var.set(result)

if __name__ == '__main__':
	calculator = Controller() # Instance of controller is created
	calculator.main()         # Call main method
