''' Created on Nov 10, 2023

	@author: aalp.kilic
'''
import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

	PAD = 10
	
	MAX_BUTTONS_PER_ROW = 4
	
	button_captions = [
		'C', '+/-', '%', '/',
		7  , 8    , 9  , '*',
		4  , 5    , 6  , '-',
		1  , 2    , 3  , '+',
		0  , '.'  , '='
		]

	def __init__(self, controller):
		'''
		Constructor
		'''
		super().__init__()

		self.controller = controller

		self.value_var = tk.StringVar()

		self.title('PyCalc1.0')

		self.config(bg = 'black')

		self._config_button_styles()

		self.maxsize(500, 500)

		self._make_main_frame()
		self._make_label()
		self._make_buttons()
		self._center_window()

	def _config_button_styles(self):
		style = ttk.Style()

		style.theme_use('alt')

		# style for number buttons
		style.configure(
			'N.TButton', foreground = 'white', background = 'gray'
			)

		#style for operator buttons
		style.configure(
			'O.TButton', foreground = 'white', background = 'orange'
			)

		#style for miscallenaous buttons
		style.configure(
			'M.TButton', background = 'white'
			)

		'''print(style.theme_names())
		print(style.theme_use())'''

	def main(self):
		self.mainloop()

	def _make_main_frame(self):    
		self.main_frm = ttk.Frame(self)
		self.main_frm.pack(padx=self.PAD, pady=self.PAD)

	def _make_label(self):            
		lbl = tk.Label(
			self.main_frm, anchor = 'e', textvariable=self.value_var,
			bg = 'black', fg = 'white', font = ('Arial', 30)
			)
		lbl.pack(fill='x')
		
	def _make_buttons(self):
		outer_frm = ttk.Frame(self.main_frm)
		outer_frm.pack()

		is_first_row = True
		buttons_in_row = 0
		
		for caption in self.button_captions:
			if is_first_row or buttons_in_row == self.MAX_BUTTONS_PER_ROW:
				is_first_row = False

				frm = ttk.Frame(outer_frm)
				frm.pack(fill='x')
				
				buttons_in_row = 0

			if isinstance(caption, int):
				style_prefix = 'N'
			elif self._is_operator(caption):
				style_prefix = 'O'
			else:
				style_prefix = 'M'

			style_name = f'{style_prefix}.TButton'
				
			btn = ttk.Button(
				frm, text=caption, command=(
					lambda button=caption: self.controller.on_button_click(button)
					), width = 20, style = style_name
				)

			if caption == 0:
				fill = 'x'
				expand = 1
			else:
				fill = 'none'
				expand = 0

			btn.pack(fill = fill, expand = expand, side='left')
			
			buttons_in_row += 1

	def _is_operator(self, button_caption):
		return button_caption in ['/', '*', '-', '+', '=']

	def _center_window(self):
		self.update()

		width  = self.winfo_width()
		height = self.winfo_height()

		x_offset = (self.winfo_screenwidth() - width)   // 2
		y_offset = (self.winfo_screenheight() - height) // 2

		print(width, height)
		self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	