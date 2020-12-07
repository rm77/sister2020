# saved as greeting-server.py
import Pyro5.api
import os
from PhoneBookModel import *

def start_with_ns(hostname="localhost",port=9090):
    #name server harus di start dulu dengan  pyro5-ns
    #gunakan URI untuk referensi name server yang akan digunakan
    #untuk mengecek service apa yang ada di ns, gunakan pyro5-nsc list
    daemon = Pyro5.server.Daemon()
    ns = Pyro5.api.locate_ns(host=hostname,port=port,broadcast=True)
    phonebook = Pyro5.api.expose(PhoneBook) #Phonebook adalah nama class dari model phonebookDB
    uri = daemon.register(phonebook)
    print("URI: ", uri)
    ns.register("phonebook.server", uri) # phonebook.server merupakan nama yang nantinya dapat diakses oleh client
    daemon.requestLoop()


if __name__ == '__main__':
    servername=os.getenv('PYROSERVERNAME') or 'localhost'
    serverport=os.getenv('PYROSERVERPORT') or 9090
    start_with_ns(hostname=servername,port=serverport)



