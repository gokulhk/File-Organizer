import os, shutil, main
from os import path


def group_by_file_type(folder_path):
	#create folder for respective file types 
	dirs = os.listdir( folder_path ) #files in current directory
	file_type_list = []
	
	for f in dirs:
			
		temp_file_type = f.split(".")
		if len(temp_file_type) != 1:
			if temp_file_type[1] not in file_type_list :
				file_type_list.append(temp_file_type[1])
		
	if len(file_type_list) == 1: 
		#only one file type exists in current folder so no file type grouping
		return
				
	for file_type in file_type_list:
		temp_path = folder_path + "/" + file_type + "_files"
		os.mkdir(temp_path)
		
		
	#move all the files into respective folder [ Advanced Grouping ]
	for f in dirs:
		if(len(f.split(".")) == 2):
			from_path = folder_path+"/"+ f
			to_path = folder_path + "/" + f.split(".")[1] + "_files"
			shutil.move(from_path, to_path)


def group_by_file_category(user_entered_path, include_file_type): 

	p = user_entered_path
	dirs = []
	files = []
	types = []
	file_count = 0
	l = os.listdir(p)

	#appends all files,folders and file types into respective list objects
	for i in l:
		if(os.path.isdir(p + "/" + i)):
			dirs.append(i)
		else:
			file_count += 1
			temp = i.split(".")[-1]
			types.append(temp)
			files.append(i)
			
	#no general grouping if only one file exists
	if file_count == 1 :
		return

	#removing duplicate file types
	types = list(set(types))
	
	#common files types list 
	text_file_types = [ "Text_files", "doc", "docx", "log", "msg", "odt", "pages", "rft", "tex", "txt", "wpd", "wps" ] 
	data_file_types = [ "Data_files", "csv", "dat", "ged", "key", "keychain", "pps", "ppt", "pptx", "sdf", "tar", "tax2016", "tax2017", "vcf", "xml" ]
	audio_file_types = [ 'Audio_files', 'aif', 'iif', 'm3u', 'm4a', 'mid', 'mp3', 'mpa', 'wav', 'wma' ]
	video_file_types = [ 'Video_files', '3gp', 'asf', 'avi', 'flv', 'm4v', 'mov', 'mp4', 'mpg', 'mkv', 'rm', 'srt', 'swf', 'vob', 'wmv', 'webm' ]
	image_3d_file_types = [ 'Image_3d_files', '3dm', '3ds', 'max', 'obj' ]
	image_raster_file_types =  [ 'Raster_Images', 'bmp', 'dds', 'gif', 'jpg', 'png', 'psd', 'pspimage', 'tga', 'thm', 'tif', 'tiff', 'yuv' ] 
	image_vector_file_types = [ 'Vector_Images', 'ai', 'eps', 'ps', 'svg' ]
	page_layout_file_types = [ 'Page_Layouts', 'innd', 'pct', 'pdf' ]
	spreadsheet_file_types = [ 'Spread_sheets', 'xlr', 'xls', 'xlsx' ]
	database_file_types = [ 'DB_Files', 'accdb', 'db', 'dbf', 'mdb', 'pdb', 'sql' ]
	executable_file_types = [ 'Executables', 'apk', 'app', 'bat', 'cgi', 'com', 'exe', 'gadget', 'jar', 'wsf' ]
	game_file_types = [ 'Game_Files', 'b', 'dem', 'gam', 'nes', 'rom', 'sav' ]
	cad_file_types = [ 'CAD_Files', 'dwg', 'dxf' ]
	gis_file_types = [ 'GIS_Files', 'gpx', 'kml', 'kmz' ]
	web_file_types = [ 'Web_Files', 'asp', 'aspx', 'cer', 'cfm', 'csr', 'css', 'dcr', 'htm', 'html', 'js', 'jsp', 'php', 'rss', 'xhtml' ]
	plugin_file_types = [ 'Plugins', 'crx', 'plugin' ]
	font_file_types = [ 'Font_Files', 'fnt', 'fon', 'otf', 'ttf' ]
	system_file_types = [ 'System_Files', 'cab', 'cpl', 'cur', 'deskthemepack', 'dll', 'dmp', 'drv', 'icns', 'ico', 'lnk', 'sys']
	settings_file_types = [ 'Setting_Files', 'cfg', 'ini', 'prf' ]
	encoded_file_types = [ 'Encoded_Files', 'hqx', 'mim', 'uue' ]
	compressed_file_types = [ 'Compressed_Files', '7z', 'cbr', 'deb', 'gz', 'pkg', 'rar', 'rpm', 'sitx', 'tar.gz', 'zip', 'zipx']
	disk_image_file_types = [ 'Disk_Image_Files', 'bin', 'cue', 'dmg', 'iso', 'mdf', 'toast', 'vcd' ]
	developer_file_types = [ 'Developer_Files', 'c', 'class', 'cpp', 'cs', 'dtd', 'fla', 'h', 'java', 'lua', 'm', 'pl', 'py', 'sh', 'sln', 'swift', 'vb', 'vcxproj', 'xcodeproj' ]
	backup_file_types = [ 'BackUp_Files', 'bak', 'tmp' ]
	misc_file_types = [ 'Misc_Files', 'crdownload', 'ics', 'msi', 'part', 'torrent' ]
	 
	#adding file type objects into a list 
	file_categories = [text_file_types ,data_file_types,audio_file_types,video_file_types,image_3d_file_types,\
		image_raster_file_types ,image_vector_file_types,page_layout_file_types,spreadsheet_file_types,database_file_types ,\
		executable_file_types,game_file_types ,cad_file_types ,gis_file_types,web_file_types,plugin_file_types,font_file_types,\
		system_file_types,settings_file_types,encoded_file_types,compressed_file_types,disk_image_file_types,developer_file_types,\
		backup_file_types,misc_file_types] 

	#appends directories to  be created for existing file types
	directory_list = []
	file_category_dict = {}
	for t in types:
		for f in range(len(file_categories)-1):
			
			if t in file_categories[f] :
				if file_categories[f][0] not in file_category_dict.keys():
					file_category_dict[file_categories[f][0]] = [] 
				file_category_dict[file_categories[f][0]].append(t)
				directory_list.append(file_categories[f][0])
				print(file_categories[f][0] + "-->" + t )

	#removing duplicate file types
	#and not(file_categories[f][0] in directory_list) 
	directory_list = list(set(directory_list))

	print(directory_list)
	#creating directories for existing files
	for i in directory_list:
		temp_path = p + "/" + i
		print(temp_path)
		os.mkdir(temp_path)

	#moving files into respective folders
	print(l)
	print(file_category_dict)
	for i in l :
		temp_path = p + "/" + i
		if os.path.isfile(temp_path):
			temp_type = i.split(".")[-1]
			for t in file_category_dict.keys():
				if temp_type in file_category_dict[t] :
					from_path = p + "/" + i
					to_path = p + "/" + t
					shutil.move(from_path, to_path)
					print("from: " + from_path)
					print("to: " + to_path)

	#groups files in new folders by type
	if include_file_type == 1 :
		for i in  directory_list:
			temp_path = p + "/" + i
			group_by_file_type(temp_path)

def custom_grouping():
	#create directories
	user_path = "/home/gokulnath/Temporary/test_folder"
	#function params
	file_names = ["Files", "Images", "Videos", "Documents", "Papers", "Presentations"]
	parent_id = [0, 1, 1, 1, 4, 4 ]
	file_types = ["None", "png,jpg", "mp4,mkv", "docx,pdf", "pptx"]
	ref_file_names = []
	ref_file_types = []
	relative_path = [root_path]
	
	#
	#for i in file_names :
		
	
	#merge sub folder files if mentioned 
		#merge_sub_folder_files(user_path)
	
	#create user mentioned directories
	l = len(file_names)
	for i in range(l):
		if parent_id[i] == 0 :
			temp_relative_path = "/" + file_names[i]
		else:
			temp_relative_path = relative_path[parent_id[i]] + "/" + file_names[i]
			
		obsolute_path = user_path + temp_relative_path
		relative_path.append(temp_relative_path)
		print(obsolute_path)
		#os.mkdir(obsolute_path)
	
	#get all the files in the current folder and organize
	file_list = os.listdir(user_path)
	
	for i in range(len(file_list)):
		temp_type = i.split(".")[-1]
		
	

		


def merge_sub_folder_files(user_path):
	
	#move files from sub folders to user mentioned folders
	for root, dirs, files in os.walk(user_path, topdown=False):
		if root != user_path :
			for name in files:
				from_path = os.path.join(root, name)
				to_path = user_path
				shutil.move(from_path, to_path)
				print("from : " + from_path + "\nto : " + to_path)
		for name in dirs:
			print("Remove : " + os.path.join(root, name))
			os.rmdir(os.path.join(root, name))
	#move files 

#custom_grouping()
merge_sub_folder_files("/home/gokulnath/Temporary/test_folder")

"""
temp = "aif, iif, m3u, m4a, mid, mp3, mpa, wav, wma"
new_temp = []
temp_list = temp.split(", ")
for i in temp_list:
	new_temp.append(i)
print(new_temp)
"""
