from subprocess import call, check_output, CalledProcessError, STDOUT
import actions as actions


def teste ():
    texto = 'Tarefas'
    #print('Tarefas escolhidas:')
    for tarefas in comando_escolhido: print (tarefas)

comando_escolhido = ['um', 'dois', 'teste']
def gera_comando():
    texto = 'Tarefas escolhidas:\n'
    t = ''
    #print('Tarefas escolhidas:\n')
    for tarefas in comando_escolhido: t += str(tarefas) + ' \n'
    return texto + t


#textoReturned = gera_comando()
#print(textoReturned)