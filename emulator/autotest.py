import sys

ScriptName = "autotest.py"

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

#Return Data in the order of t
def get_data(fileName,paterns):
	lines = open_file(fileName,'r')
	#print(*lines)
	data = []
	for iL, line in enumerate(lines):
		for patern in paterns:
			ptr = line.find(patern)
			if ptr > -1:
				raw_data = lines[iL +1].split(':')[1].split(',')
				print(raw_data)
				data.append( [raw_data[0].split(" ")[1],raw_data[1].split(" ")[1],
			    raw_data[2].split(" ")[1],raw_data[3].split(" ")[2]])

	if len(paterns) != len(data):
		sys.exit("No paterns found in "+ fileName)
	#print(data)
	return data	

#Recives a list of list with the parameters and return a list with the average
#input:[[a,b,c,d],[a,b,c,d],...] Output: [AVa,AVb,AVc,AVd]
def prom_tests(list_of_data):
	out =[0]*len(list_of_data[0])
	n_samples = len(list_of_data)
	num_per_sample = len(list_of_data[0])
	for row in list_of_data:
		for i,item in enumerate(row):
			out[i] = out[i] + int(item)
	
	for i, item in enumerate(out):
 		out[i] = out[i]/n_samples

	print(out)

	return out

#Recives a list of list with the parameters and return a list with the average
#input:[[[a,b,c,d...],[a,b,c,d...]..],...] Output: [[AVa,AVb,AVc,AVd...],[AVa,AVb,AVc,AVd...]...]
def prom_test_n(list_of_data):
	for line in list_of_data:
		print(line)
	n_samples = len(list_of_data)
	print(n_samples)

	test_Outs = []

	test_size = []

	for j in range(0,4):
		test_size.append(0)

	for i in range(0,2):
		l = test_size[:]		
		test_Outs.append(l)	

	print(test_Outs)
	for row in list_of_data:
		for it,test in enumerate(row):
			for i, item in enumerate(test):
				test_Outs[it][i] = float(test_Outs[it][i]) + float(item)
				#print(test_Outs,it,i, item)			

	for it,test in enumerate(test_Outs):
		for i,item in enumerate(test):
			test_Outs[it][i] = test_Outs[it][i]/n_samples

	print(test_Outs)
	return test_Outs

def export_csv(path,data,protocols,cores, paterns):
	csv_out = []
	line = ""
	for protocol in protocols:
		for ncore in cores:
			for i,patern in enumerate(paterns):
				line = protocol+","+patern+","+ncore+","+list_to_csv(data[protocol][ncore][i])+"\n"
				print(line)
				csv_out.append(line)
	csv_out.insert(0,"Protocol,Test Case,Number of Cores, Cycles, Cycles/iteration, CPI, Number of Instructions\n")

	print(path)
	save_file(path[:-1]+"csv_out.csv",csv_out)




def list_to_csv(lista):
	out = ""
	for i in lista:
		out = out + (str(i) + ',')

	return out[:-1]





args = sys.argv[1:]
len_args = len(args)
paterns = ['Independent','Reuse']
test = {}


if(len_args==1):							 #Single argument instrucions

	if args[0] == "-help":       

		print('\n \t \t \t \t \t *** Python Output Data Parser ***'
			  '\n\nTo get data from output: \n'
			  '\n\t python3 '+ ScriptName + ' <Folder/ForlderWhithNameOfTheTest> <list of cores>  <nIter> <list_of_protocols> <optional output name>'
			  '\n\t\t\t List are coma separed values: 1,2,3,4... MSI,MI,MESI...'

			  '\n\nTo display help: \n'
			  '\n\t python3 '+ ScriptName + ' -help')

	else:
		
		raise Exception(" No " + cmd_args[0] +" comand found: \n \v -For help type:"+ScriptName+" -help")


if len_args >= 4 and len_args <=5:
	ruta       = args[0]
	test_name  = ruta.split('/')[1]
	n_cores    = args[1].split(',')
	n_iters    = args[2]
	coherece_prot = args[3].split(',')
	test_by_ncores = {}

	data_tests = []
	for protocol in coherece_prot:
		for cores in n_cores:
			for i in range(0,int(n_iters)):
				data_tests.append(get_data(ruta+"/"+test_name+"_"+
					        protocol+"-"+cores+"_test-"+str(i)+".txt",paterns))

			test_by_ncores[str(cores)] = prom_test_n(data_tests)
		test[protocol] = test_by_ncores

	print(test)

	if len_args == 5:
		export_csv(ruta.split('/')[0]+"/"+args[4],test,coherece_prot,n_cores,paterns)
		
	else:
		export_csv(ruta,test,coherece_prot,n_cores,paterns)




	

