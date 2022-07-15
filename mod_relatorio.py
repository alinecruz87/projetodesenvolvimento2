from ast import literal_eval
from subprocess import *

from regex import P
import actions
import subprocess

itens_rel = [actions.hostname, actions.ip, actions.linux_version]
itens_pipe = [actions.disk_space, actions.cpu_number, actions.cpu_model, actions.ram]

def execute(itens):
    return call(itens.split())

def get(itens):
    try:
        return 0, check_output(itens.split(), stderr=STDOUT)
    except CalledProcessError as e:
        return e.returncode, e.check_output


def relatorio_with_call():
    lista = []
    retorno = []
    for i in itens_pipe:
        result = subprocess.run(
    [i], capture_output=True, text=True, shell=True
)
        t = result.stdout
        lista.append(t)
    disk_space = "Disk Space: " + lista[0] +"%"
    cpu_number = "CPUs: " + lista[1]
    cpu_model = lista[2]
    ram = "Ram: " +lista[3]
    retorno_relatorio2 = disk_space + cpu_number + cpu_model + ram
    #print (retorno_relatorio2)
    return (retorno_relatorio2)

def relatorio():
    lista = []
    retorno = []
    for i in itens_rel:
        lista = get(i)
        l = lista[1].decode('utf-8')
        retorno.append(l)
    hostname =  "Hostname: " + retorno[0]
    ip = "IP: " + retorno [1]
    release = "Linux Version: " + retorno[2]
    retorno_relatorio = hostname + ip + release
    #print(retorno_relatorio)
    return retorno_relatorio


#relatorio()
#relatorio_with_call()



        