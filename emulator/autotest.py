import sys

def open_file(path_of_file,mode):
	#Try to open File 
	if mode == 'w':
		try:
			with open(path_of_file,'r') as doc:
				read_data = doc.readlines()
				#doc.close()
			return read_data	

		except FileNotFoundError as fnf_error:
			print(fnf_error)
			
			print('File ' + path_of_file + ' will be created.')
			with open(path_of_file,'w+') as doc:
				read_data = doc.readlines()
				#doc.close()
			return read_data	
	elif mode == 'r':
		try:
			with open(path_of_file,'r') as doc:
				read_data = doc.readlines()
				#doc.close()
			return read_data	

		except FileNotFoundError as fnf_error:
			print(fnf_error)			
			sys.exit('Read input file ' + path_of_file + ' does not exits.')
			
			

def save_file(path_of_file,text_list):
	#Try to open File 
	try:
		with open(path_of_file,'w') as doc:
			doc.writelines(text_list)
			doc.close()

	except FileNotFoundError as fnf_error:
		print(fnf_error)

def get_data(fileName,paterns):
	lines = open_file(fileName,'r')
	data = []
	for iL, line in enumerate(lines):
		for partern in paterns:
			ptr = line.find(patern)
			if ptr > -1:
				raw_data = lines[iL +1][ptr:].split(',')
				data.append( [raw_data[0].split(" ")[2],raw_data[1].split(" ")[2],
			    raw_data[2].split(" ")[2],raw_data[3].split(" ")[2]])

	print(data)
	return data		

args = sys.argv[1:]
len_args = len(args)
coherece_prot = ['MESI','MSI','MI']
paterns = ['Inpendent','Reuse']
test = {}


if len_args == 3:
	ruta       = args[0]
	test_name  = ruta.split('/')
	n_cores    = args[1].split(',')
	n_iters    = args[2]

	for protocol in coherece_prot:
		for cores in n_cores:
			for i in range(1,int(n_iters)):
				data_test = get_data(ruta+"/"+test_name+"_"+
					        protocol+"-"+cores+"_test-"+str(i)+".txt",paterns)
				





	

