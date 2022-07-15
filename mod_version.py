from subprocess import call, check_output, CalledProcessError, STDOUT
import actions
import sys


def versions():
    lista = get(actions.java_version)
    l = lista[1].decode('utf-8')
    retorno = l.split()
    java_ver = 'JAVA VERSION: ' + retorno[2]
    #print(java_ver)
    return java_ver

def get(java_version):
    try:
        return 0, check_output(actions.java_version.split(), stderr=STDOUT)
    except CalledProcessError as e:
        return e.returncode, e.check_output


#versions()
