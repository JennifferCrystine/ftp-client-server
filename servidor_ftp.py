import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Instantiate a dummy authorizer for managing 'virtual' users
authorizer = DummyAuthorizer()
# Define a new user having full r/w permissions and
# anonymous use
authorizer.add_user('user', '12345','C:/Users/',perm='elradfmwMT') #para mudar para fazer troca entre pares, coloque um diretório local aqui (diretório do computador)
authorizer.add_anonymous('C:/Users/', perm='elradfmwMT')
# Instantiate FTP handler clas
handler = FTPHandler
handler.authorizer = authorizer
# Define a customized banner (string returned when client connects)
#handler.banner = "pyftpdlib based ftpd ready."
# Instantiate FTP server class and listen on 127.0.0.1:1026 (localhost)
server = FTPServer(('127.0.0.1', 1026), handler) #e coloque aqui o endereço da sua máquina
# start ftp server
server.serve_forever()
