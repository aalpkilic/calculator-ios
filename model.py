''' Created on Nov 10, 2023

	@author: aalp.kilic
'''

class Model:

	def __init__(self):
		
		self.previous_value = ''
		self.value = ''
		self.operator = ''
	
	def calculate(self, caption):
		if caption == 'C':
			self.previous_value = ''
			self.value = ''
			self.operator = ''
			
		elif caption == '+/-':
			self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value
			
		elif caption == '%':
			pass
			#self.value = (self.value / 100)
			
		elif caption == '=':
			value = self._evaluate()
			if '.0' in str(value):
				value = int(value)

			self.value = str(value)
			
		elif caption == '.':
			if not caption in self.value:
				self.value += caption
		
		elif isinstance(caption, int):
			self.value += str(caption) 
		
		else:
			if self.value:
				if caption == '/' and isinstance(self.previous_value, int) and isinstance(self.value, int):
					self.operator = '//'
				else:
					self.operator = caption
				
				self.previous_value = self.value
				
				self.value = ''
			
		return self.value 
	
	def _evaluate(self):
		return eval(self.previous_value+self.operator+self.value)
			
		
		
		
