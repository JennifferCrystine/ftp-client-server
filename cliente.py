from ftplib import FTP
ftp = FTP('')
ftp.connect('localhost',1026) #colocar aqui o endereço do servidor - connect to host
ftp.login() # user anonymous, passwd anonymous@
#ftp.cwd(r'C:\Users\') #replace with your directory
ftp.retrlines('LIST') # list directory contents

def uploadFile():
	filename = input('Digite o endereco do arquivo')
	#filename = 'C:/Users/guilh/Desktop/REDES_I/teste.txt' #replace with your file in your home
	folder
	filenameu = input('Que nome deseja dar ao arquivo?')
	ftp.storbinary('STOR '+filenameu, open(filename, 'rb'))
def downloadFile():
	filename = input('Digite o nome do arquivo que deseja baixar')
	#filename = 'testfile.txt' #replace with your file in the directory ('directory_name')
	filenamed = input('Digite o nome que deseja dar ao arquivo e o local que deseja coloca-lo')
	localfile = open(filenamed, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	localfile.close()
func =0
while(func !='sa'):
	while (func!='up' and func !='do' and func!='sa'):
		func=input('Digite up para fazer upload de um arquivo e do para fazer o download e sa para sair')

		print(func)
		print(func!='do')
	if(func=='up'):
		uploadFile()
		func=0
	if(func=='do'):
		downloadFile()
		func =0
	if(func=='sa'):
		ftp.quit()
