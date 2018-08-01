import os 
print(os.getcwd())
print(os.path.abspath('./..'))
print(os.path.abspath('.'))
print(os.path.abspath('osprogramsbyshreyank.py'))
print(os.listdir('.'))
print(os.listdir('/home'))
#os.rename('osprogramsbyshreyank.py','osprogramsnotbyshreyank.py')
print(os.path.getsize('osprogramsnotbyshreyank.py'))
dir_list = []
file_list = []
for files in os.listdir('.'):
	#print(files.split('.')[1]=='pdf')
	#if(files[-1:-4]=='.pdf'):
	#	print(files)
	if(files.endswith('pdf')):
		print(files)
	if os.path.isdir(files):
		dir_list.append(files)
	else:
		file_list.append(files)
print(len(file_list))
print(len(dir_list))






