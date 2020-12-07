#client berada di sisi remote, client hanya mmebutuhkan
# dependency kepada library Pyro5

import Pyro5.api


if __name__=='__main__':
    # untuk mengecek service apa yang ada di ns, gunakan pyro5-nsc  -p 9900 list
    #dalam kasus ini namanya adalah phonebook.server
    phonebook = Pyro5.api.Proxy('PYRONAME:phonebook.server')
    # untuk melihat daftar dari phonebook
    print(phonebook.list())
    #create record di phonebook
    phonebook.create(dict(nama='Roberto Carlos',alamat='Jambangan',notelp='67829'))
    # untuk melihat daftar dari phonebook, cek kembali
    print(phonebook.list())

