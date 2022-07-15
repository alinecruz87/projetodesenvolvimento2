from subprocess import call, check_output, CalledProcessError, STDOUT
import actions
import sys

def check_status():
    lista = get(actions.status)
    l = lista[1].decode('utf-8')
    retorno = l.split()
    #print("\n")
    #print(retorno[3:10])
    status = retorno[0] + ': ' + retorno[1]
    state = retorno[2] + ' ' + retorno[3]
    jobs = retorno[4] + ' ' + retorno[5]
    failed = retorno[7] + ' ' + retorno[8] + ' ' + retorno[9]
    retorno_sys_ctl = status + '\n' + state + '\n' + jobs + '\n' + failed
    #print(retorno_sys_ctl)
    tamanho = len(retorno_sys_ctl)
   # print(tamanho)
    #print(retorno_sys_ctl[3:tamanho-2])
    return retorno_sys_ctl[3:tamanho-2]
    


def get(status):
    try:
        return 0, check_output(actions.status.split(), stderr=STDOUT)
    except CalledProcessError as e:
        return e.returncode, e.check_output

#check_status()
