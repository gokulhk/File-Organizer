import tkinter 
import os
from tkinter import *
from tkinter import messagebox


def page_one_ui():
	page_one_ui.path = ""
	page_one_ui.grouping_type = ""
	page_one_ui.subfolder_action = ""
	root = Tk()
	page_one_ui.temp = root
	root.geometry("300x300")
	#Adding a label
	l1 = Label(root, text = "Enter Directory path : ")  
	l1.place(x = 10, y = 10)

	#adding a input box to get the directory path 
	page_one_ui.e1 = Entry(root)         
	page_one_ui.e1.place(x = 10, y = 30)

	page_one_ui.var = IntVar() #general grouping selection 
	page_one_ui.folder_var = IntVar() #for subfolder option selection
	selected = IntVar() #default don't merge subfolders is selected 
	
	page_one_ui.correct = False

	#display option label
	opt_msg = StringVar()
	opt_msg.set("choose a grouping type: ")
	option_label = Label(root, textvariable = opt_msg)
	option_label.place(x = 10, y = 50)

	#display list of options 
		
	r1 = Radiobutton(root, text = "File Category",  variable = page_one_ui.var, value = 1, command = sel)
	r1.place(x = 20, y = 70)

	r2 = Radiobutton(root, text = "File Category with File type sub folders",  variable = page_one_ui.var, value = 2, command = sel)
	r2.place(x = 20, y = 90)
	
	r3 = Radiobutton(root, text = "File Type", variable = page_one_ui.var, value = 3, command = sel)
	r3.place(x = 20, y = 110) 

	#c1 = Checkbutton(root, text = "Merge sub folders", variable = selected, onvalue = 1, offvalue = 2)
	#c1.place(x = 10, y = 110)

	sub_folder_label = Label(root, text = "Action on sub folders:(ignore if none)")
	sub_folder_label.place(x = 10, y = 130)

	k1 = Radiobutton(root, text = "Merge files to root folder and organise",  variable = page_one_ui.folder_var, value = 1)
	k1.place(x = 20, y = 150)

	k2 = Radiobutton(root, text = "Organize files in their respective folders with selected grouping type",  variable = page_one_ui.folder_var, value = 2)
	k2.place(x = 20, y = 170)
	
	k3 = Radiobutton(root, text = "No Action", variable = page_one_ui.folder_var, value = 3)
	k3.place(x = 20, y = 190)
	
	#add next button at the bottom
	next_button  =  Button(root, text = "Next", command = disp_entry)
	next_button.place(x = 10, y = 240)
	
	root.mainloop() #display window
	
	if page_one_ui.correct is True :
		p = []
		p.append(page_one_ui.path)
		p.append(page_one_ui.subfolder_action)
		p.append(page_one_ui.grouping_type)
		
		return p
#a = page_one_ui()
#print(a)

#action to perform when a button is selected
def sel():  
	pass
	#selection = "You selected option " + str(var.get())
	#label.config(text = selection)
	
#msg display function
def disp_entry():
		entered_value = page_one_ui.e1.get()
		
		if len(entered_value) == 0 :
			page_one_ui.e1.config(highlightcolor = "red")
		elif(not(os.access(entered_value, os.F_OK))):  #check for existence of the entered path 
			msg_value = "Enter a Valid Path \n The Path : \n\"" + entered_value + "\" doesn't exit" 
			messagebox.showinfo("Warning!",msg_value) 
			page_one_ui.e1.delete(0, len(msg_value) -1)
			page_one_ui.e1.config(highlightcolor = "red")
		else:
			a = {1:"File Category", 2:"Category with type", 3:"File Type" }
			b = {1:"Merge to root" , 2:"organise without merging", 3:"No Action"}
			s1 = "Path: " + entered_value + "\nGrouping type : " + a[page_one_ui.var.get()] + "\nMerge sub folders : " + b[page_one_ui.folder_var.get()] 
			messagebox.showinfo("Details", s1)
			page_one_ui.path = entered_value
			page_one_ui.grouping_type = page_one_ui.var.get()
			page_one_ui.subfolder_action = page_one_ui.folder_var.get()
			page_one_ui.correct = True
			page_one_ui.temp.destroy()