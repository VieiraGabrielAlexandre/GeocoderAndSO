import platform
import getpass
from datetime import datetime

# print("Nome maquina: ", platform.node())
# print("Arquitetura: ", platform.architecture())
# print("Sistem Operacional: ", platform.system())
# print("Versão do SO: ", platform.release())
# print("Processador: ", platform.processor())
# print("Versão do Python: ", platform.python_version())
#
# print(datetime.now().hour)
usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha: ")

if usuario == "Bax" and senha == "teste":
    print("Bem vindo")
else:
    print("Você não tem acesso")