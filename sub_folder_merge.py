import os, sys, shutil, grouping_functions
from grouping_functions import group_by_file_category, group_by_file_type

class MergeSubFolder:
	
	def __init__(self, file_object = None):
		self.__file_object = file_object
		self.__log_string = ""
		self.__from_path = ""
		self.__to_path = ""
		self.__recursion_count = 0
		
	def merge_sub_folder(self, cur_dir, from_path, to_path):
		
		if cur_dir != "":
			from_path += "/" + cur_dir
		
		#check for existence of subfolder in the current directory 
		dir_list = os.listdir(from_path) 
		
		file_list = []
		file_count = 0
		sub_folder_list = []
		
		#loading files and sub folders into respective lists 
		for temp_file in dir_list:
			temp_file_type = temp_file.split(".")
			if len(temp_file_type) != 1:
				file_list.append(temp_file)
				file_count += 1
			else:
				sub_folder_list.append(temp_file)
		
		
		if len(sub_folder_list) == 0: #no subfolder, i.e reached the leaf folder
			#move all the files to root directory if exists 
			if file_count > 0:
				print("recursion depth reached")
				print("from: "+from_path+"\nto: ",to_path)
				for temp_file in file_list:
					t_from = from_path + "/"+ temp_file
					self.__file_object.write(t_from + "\n")
					print("from: "+t_from+"\nto: ",to_path)
					shutil.move(t_from, to_path)
				self.__recursion_count += 1
			return 
		else:
			#call recursion
			for temp_sub_folder in sub_folder_list:
				#temp_from_path  = from_path + "/" + temp_sub_folder
				self.merge_sub_folder(temp_sub_folder, from_path, to_path)
				self.__recursion_count += 1
			print("recusrion count : ", self.__recursion_count)
			#remove child direc
			for sub_folder in sub_folder_list:
				remove_path = from_path + "/" + sub_folder
				os.rmdir(remove_path)
			#move files to root
			if from_path != to_path :
				for temp_file in file_list:
					t_from = from_path + "/"+ temp_file
					self.__file_object.write(t_from + "\n")
					print("from: "+t_from+"\nto: ",to_path)
					shutil.move(t_from,to_path)
			
			return 
			
	def organize_without_merge(self, user_entered_path, grouping_category):
		
		if grouping_category == 1 :
			for root,dirs,files in os.walk(user_entered_path):
				group_by_file_category(root, 0) # 0 - without file type sub folder
		elif grouping_category == 2 :
			for root,dirs,files in os.walk(user_entered_path):
				group_by_file_category(root, 1) # 1 - with file type sub folder
		elif grouping_category == 3 :
			for root,dirs,files in os.walk(user_entered_path):
				group_by_file_type(root)

def recover_last_changes():
	f = open("merge_operation_log.txt", "r")
	f.readline()
	f.readline()
	path_list = []
	file_list = []
	from_path = "/home/gokulnath/yt"
	move_path = []
	for i in range(7):
		temp_str = f.readline().rstrip()
		move_path.append(temp_str)
		fl = temp_str.split("/")[-1]
		file_list.append(fl)
		s = len(fl)
		temp_str = temp_str[:len(temp_str) - s]
		path_list.append(temp_str)
	dir_list = list(set(path_list))
	dir_list.sort()
	for i in dir_list:
		print(i)
		os.mkdir(i)
		
	for i in move_path:
		file_name = i.split("/")[-1]
		print(file_name)
		temp_path = from_path + file_name
		print(temp_path)
		to_path = i
		shutil.move(temp_path, to_path)


