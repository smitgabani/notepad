import tkinter 
import os	 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Codepad: 

	__root = Tk() 

	__thisWidth = 700
	__thisHeight = 700
	__thisTextArea = Text(__root, bg="#000", fg="#fff", font = (10)) 
	__thisMenuBar = Menu(__root) 
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0)
	#__thisFindMenu = Menu(__thisMenuBar, tearoff=0)
	#__thisViewMenu = Menu(__thisMenuBar, tearoff=0)
	__thisThemeMenu = Menu(__thisMenuBar, tearoff=0)
	__thisDrawMenu = Menu(__thisMenuBar, tearoff=0)
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
	 
	__thisScrollBar = Scrollbar(__thisTextArea)	 
	__file = None

	def __init__(self,**kwargs): 

		try: 
				self.__root.wm_iconbitmap("Notepad.ico") 
		except: 
				pass

		try: 
			self.__thisWidth = kwargs['width'] 
		except KeyError: 
			pass

		try: 
			self.__thisHeight = kwargs['height'] 
		except KeyError: 
			pass

		self.__root.title("Untitled - Codepad") 

		screenWidth = self.__root.winfo_screenwidth() 
		screenHeight = self.__root.winfo_screenheight() 
	
		left = (screenWidth / 2) - (self.__thisWidth / 2) 
		
		top = (screenHeight / 2) - (self.__thisHeight /2) 
		
		
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
											self.__thisHeight, 
											left, top)) 

		
		self.__root.grid_rowconfigure(0, weight=1) 
		self.__root.grid_columnconfigure(0, weight=1) 

		
		self.__thisTextArea.grid(sticky = N + E + S + W) 
		
		
		self.__thisFileMenu.add_command(label="New", command=self.__newFile)	 
		self.__thisFileMenu.add_command(label="Open", command=self.__openFile) 
		self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)	 
		self.__thisFileMenu.add_separator()										 
		self.__thisFileMenu.add_command(label="Exit                    ", command=self.__quitApplication) 
		self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)	 
		
		
		self.__thisEditMenu.add_command(label="Cut", command=self.__cut)			 
		self.__thisEditMenu.add_command(label="Copy", command=self.__copy)		 
		self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
		self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

		"""
		self.__thisFindMenu.add_command(label="Find",)		 
		self.__thisFindMenu.add_command(label="Find Next",)
		self.__thisFindMenu.add_command(label="Find Previous",)
		self.__thisFindMenu.add_separator()
		self.__thisFindMenu.add_command(label="Replace",)
		self.__thisFindMenu.add_command(label="Replace Next",)
		self.__thisMenuBar.add_cascade(label="Find", menu=self.__thisFindMenu)	 

		
		self.__thisViewMenu.add_command(label="Zoom In",)
		self.__thisViewMenu.add_command(label="Zoom Out",)
		self.__thisMenuBar.add_cascade(label="View", menu=self.__thisViewMenu)
		"""

		
		self.__thisThemeMenu.add_command(label="Dark",)
		self.__thisThemeMenu.add_command(label="Light",)
		self.__thisMenuBar.add_cascade(label="Theme", menu=self.__thisThemeMenu)

		
		self.__thisDrawMenu.add_command(label="White",)
		self.__thisDrawMenu.add_command(label="Black",)
		self.__thisMenuBar.add_cascade(label="Draw", menu=self.__thisDrawMenu)

		
		self.__thisHelpMenu.add_command(label="About Codepad", command=self.__showAbout) 
		self.__thisHelpMenu.add_command(label="Shortcut Keys", command=self.__showShke) 
		self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu) 

		self.__root.config(menu=self.__thisMenuBar) 

		self.__thisScrollBar.pack(side=RIGHT,fill=Y)					 
		
			 
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	 
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
	
		
	def __quitApplication(self): 
		self.__root.destroy() 
		

	def __showAbout(self): 
		showinfo("Codepad","\tBy\n\tSmit Gabani   \t\n\n")

	def __showShke(self):
		showinfo("Shortcut Keys","           ")

	def __openFile(self): 
		
		self.__file = askopenfilename(defaultextension=".txt", 
									filetypes=[("All Files","*.*"), 
										("Text Documents","*.txt")]) 

		if self.__file == "": 
			
			# no file to open 
			self.__file = None
      
		else: 
			
			# Try to open the file 
			# set the window title 
			self.__root.title(os.path.basename(self.__file) + " - Codepad") 
			self.__thisTextArea.delete(1.0,END) 

			file = open(self.__file,"r") 

			self.__thisTextArea.insert(1.0,file.read()) 

			file.close() 

		
	def __newFile(self): 
		self.__root.title("Untitled - Codepad") 
		self.__file = None
		self.__thisTextArea.delete(1.0,END) 

	def __saveFile(self): 

		if self.__file == None: 
			# Save as new file 
			self.__file = asksaveasfilename(initialfile='Untitled.txt', 
											defaultextension=".txt", 
											filetypes=[("All Files","*.*"), 
												("Text Documents","*.txt")]) 

			if self.__file == "": 
				self.__file = None
			else: 
				
				# Try to save the file 
				file = open(self.__file,"w") 
				file.write(self.__thisTextArea.get(1.0,END)) 
				file.close() 
				
				# Change the window title 
				self.__root.title(os.path.basename(self.__file) + " - Codepad") 
				
			
		else: 
			file = open(self.__file,"w") 
			file.write(self.__thisTextArea.get(1.0,END)) 
			file.close() 

	def __cut(self): 
		self.__thisTextArea.event_generate("<<Cut>>") 

	def __copy(self): 
		self.__thisTextArea.event_generate("<<Copy>>") 

	def __paste(self): 
		self.__thisTextArea.event_generate("<<Paste>>") 



	def run(self): 
		self.__root.mainloop() 


codepad = Codepad(width=1000,height=600) 
codepad.run() 
