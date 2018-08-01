import sys
import os

def get_filename():
	if len(sys.argv)>1:
		fname = sys.argv[1]
		return  fname
	else:
		print("Usage: pyhton<scriptname> <filename>")
		sys.exit()

def open_file(fname):
	try:
		r_file = open(fname)
		return	r_file
	except IOError:
		print("File not present",fname)
		sys.exit()

def file_read(f_dis):
	print(f_dis.read())

def file_readline(f_dis):
	
		line= f_dis.readline()
		if not line:
			pass
		else:
			print(line)

def file_readlines(f_dis):
	for line in f_dis.readlines():
		print(line)

def file_close(f_dis):
	f_dis.close()

def testcode():
	fname= get_filename()
	fd = open_file(fname)
	file_read(fd)
	#file_readline(fd)
	file_readlines(fd)
	file_close(fd)

if __name__=='__main__':
	testcode()



