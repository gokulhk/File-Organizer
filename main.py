# -*- coding: utf-8 -*-
#file organiser 
#application to  organise and make subfolder for it
#main page of the application


def main(args):
	
	# get directory path from user
	
	#path = input("Enter directory path : ")
	user_value = page_one_ui() #returns list 
	user_entered_path = user_value[0]
	grouping_category = user_value[2]
	dirs = os.listdir( user_entered_path ) #files in current directory
	 
	#list to store all file types in the current directory
	file_type_list = []
	sub_folder_list = []
	
	# This would load all the files and directories
	for f in dirs:
		temp_file_type = f.split(".")
		if len(temp_file_type) == 1:
			sub_folder_list.append(f)
	
	
	#sub folder action code block [ folder_path, 1, 1 ] 
	
	if user_value[1] == 1 :
		#merge sub folder files to root directory
		if len(sub_folder_list) > 0 :
			#input("Want to merge the sub folder's files too ?:  ")
			cur_dir = ""
			print("path1: "+ user_entered_path +"\npath2: ", user_entered_path)
			
			#creates a merge log file if not present
			test_file_path = os.getcwd() + "/" + "merge_operation_log.txt"
			if os.access(test_file_path, os.F_OK):
				file_object = open(test_file_path, "w") 
			else:
				file_object = open(test_file_path, "a")
			
			file_object.write("------MERGE OPERATION START------\n")
			file_object.write("Destination Path : " + user_entered_path + "\n")
			m = MergeSubFolder(file_object)
			m.merge_sub_folder(cur_dir, user_entered_path, user_entered_path)
			file_object.write("------MERGE OPERATION END------\n")
			file_object.close()
	elif user_value[1] == 2 :
		#os walk the path 
		m = MergeSubFolder()
		m.organize_without_merge(user_entered_path, grouping_category)
		#organise files as per user choice
	else:
		#no action on sub folder
		pass 
		
	#grouping based on user selection
	if user_value[1] != 2:
		if grouping_category == 1 :
			group_by_file_category(user_entered_path, 0) # 0 - without file type sub folder
		elif grouping_category == 2 :
			group_by_file_category(user_entered_path, 1) # 1 - with file type sub folder
		elif grouping_category == 3 :
			group_by_file_type(user_entered_path)
	
	return 0 



if __name__ == '__main__':
	
    import os, sys, shutil, sub_folder_merge, ui_functions, grouping_functions
    from sub_folder_merge import MergeSubFolder
    from ui_functions import page_one_ui
    from grouping_functions import group_by_file_category, group_by_file_type
    
    sys.exit(main(sys.argv))


"""  for separating files and directories 
for i in l:
	if(os.path.isdir(path + "/" + i)):
		dirs.append(i)
	else:
		files.append(i)
"""
