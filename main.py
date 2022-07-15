from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
import tkinter
import mod_status as mod_status
import mod_relatorio as mod_rel
import mod_restart as mod_rest
import mod_shutdown as mod_shut
import mod_startup as mod_start
import mod_version as mod_versions
import actions
from subprocess import call, check_output, CalledProcessError, STDOUT
import time


# cores -----------------------------------
co0 = "#f0f3f5" #preta
co1 = "#feffff" #branca
co2 = "#3fb5a3" #verde
co3 = "#38576b" #valor
co4 = "#403d3d" #letra


#criando janela --------------
janela_login =  Tk()
janela_login.title('GDbrix Tool')
janela_login.geometry('700x1000')
janela_login.configure(background=co1)
janela_login.resizable(width=FALSE, height=FALSE)

#dividindo a janela --------------
frame_seis = Frame(janela_login, width=700, height=70, bg=co1, relief='flat')
frame_seis.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_sete = Frame(janela_login, width=700, height=160, bg=co1, relief='flat')
frame_sete.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#configurando o  frame1 --------------
l_nome = Label(frame_seis, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_seis, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
l_linha.place(x=10, y=55)

credenciais = ['1', '1']

# funcao para verificar senha
def verifica_senha():
    nome = e_badge.get()
    senha = e_passw.get()
    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin !!!')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo' + credenciais[0])
        #apagar o que tiver no frame um e dois
        for widget in frame_seis.winfo_children():
            widget.destroy()
        for widget in frame_sete.winfo_children():
            widget.destroy()
        nova_janela()    
    else:
        messagebox.showinfo('Erro', 'Verifique o Bagde ID e a senha')

#funcao apos verificacao
'''def nova_janela():
    l_nome = Label(frame_um, text='USUÁRIO: ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_um, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=10, y=130)

    l_nome = Label(frame_dois, text='Seja bem vindo,  ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)'''

def nova_janela():
    def status():   
        retorno_texto["text"] = mod_status.check_status()

    def start():
        mod_start.startup()

    def kill():
        messagebox.showinfo('Confirmar Shutdown', 'Tem certeza que deseja desligar o servidor?')
        retorno_texto["text"] = "Killing Server!! Please wait..."
        time.spleep(5)
        mod_shut.shutdown()

    def restartup():
        retorno_texto["text"] = "Restarting!! Please wait..."
        time.sleep(5)
        mod_rest.restart()

    def infos():
        info1 = mod_rel.relatorio()
        info2 = mod_rel.relatorio_with_call()
        retorno_texto["text"] = info1 + info2
    
    def version():
        retorno_texto["text"] = mod_versions.versions()

    comando_escolhido = []
    comando_gerado = []
    
    def gera_comando():
        comando = e_comandos.get()
        comando_escolhido.append(comando)
        texto = 'Tarefas escolhidas:\n'
        t = ''
        if 'status' in comando_escolhido:
            comando_gerado.append(mod_status.check_status())
            for tarefas in comando_escolhido: 
                t += str(tarefas) + ' \n'
            retorno_texto['text'] = texto + t
        elif 'versão' in comando_escolhido: 
            comando_gerado.append(mod_versions.versions())
            for tarefas in comando_escolhido: 
                t += str(tarefas) + ' \n'
            retorno_texto['text'] = texto + t   
        else:
            retorno_texto['text'] = "Escolha uma ou mais tarefas"

       
    def executa_comando():
        if len(comando_gerado) != 0:
            retorno_texto['text'] = comando_gerado
            comando_gerado.clear()
            comando_escolhido.clear()
        else:
            messagebox.showinfo('Erro!', 'Lista vazia, insira uma ou mais tarefas!')
    
    def clear():
        messagebox.showinfo('Limpar lista', 'Tem certeza que deseja limpar a lista de tarefas?')
        comando_gerado.clear()
        comando_escolhido.clear()
        messagebox.showinfo('Lista vazia', 'Sua lista de tarefas está vazia!')

    def conecta():
        messagebox.showinfo('Conexão', 'Aguarde, conectando com o servidor.......')
        time.sleep(5)
        retorno_texto['text'] = "Conexão realizada com sucesso!!!"
        




    frame_um_j2 = Frame(janela_login, width=700, height=70, bg=co1, relief='flat')
    frame_um_j2.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frame_dois_j2 = Frame(janela_login, width=70, height=10, bg=co1, relief='flat')
    frame_dois_j2.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

    frame_tres = Frame(janela_login, width=700, height=120, bg=co1  , relief='flat')
    frame_tres.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

    frame_quatro = Frame(janela_login, width=700, height=140, bg=co1, relief='flat')
    frame_quatro.grid(row=3, column=0, pady=1, padx=0, sticky=NSEW)

    frame_cinco = Frame(janela_login, width=700, height=140, bg=co1, relief='flat')
    frame_cinco.grid(row=4, column=0, pady=1, padx=0, sticky=NSEW)

    frame_oito = Frame(janela_login, width=700, height=500, bg=co1, relief='flat')
    frame_oito.grid(row=5, column=0, pady=1, padx=0, sticky=NSEW)



    #configurando o  frame1 --------------
    lista_servidores = ['Fedora', 'Server_02', 'Server03', 'Server04']
    l_servidor = Label(frame_um_j2, text='NOME DO SERVIDOR', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_servidor.place(x=5, y=16)

    e_servidor = ttk.Combobox(frame_um_j2, values=lista_servidores)
    e_servidor.set("Escolha...")
    e_servidor.place(x=150, y=15)

    botao_conectar = Button(frame_um_j2, text="CONECTAR", command=conecta, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=460, y=10, width=120, height=40)
  

    l_linha = Label(frame_um_j2, text='', width=700, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=1, y=65)

    #configurando o  frame2 --------------
    l_comandos = Label(frame_dois_j2, text='COMANDOS', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_comandos.place(x=5, y=16)

    botao_restart = Button(frame_dois_j2, text="RESTART", command=restartup, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=50, y=60, width=100, height=50)
    botao_shutdown = Button(frame_dois_j2, text="SHUTDOWN", command=kill, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=300, y=60, width=100, height=50) 
    botao_status = Button(frame_dois_j2, text="STATUS", command=status, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=560, y=60, width=100, height=50)

    l_linha = Label(frame_dois_j2, text='', width=700, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=1, y=130)

    #configurando o  frame3 --------------
    l_scripts = Label(frame_tres, text='SCRIPTS', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_scripts.place(x=5, y=5)

    lista_comandos = ['versão', 'status']

    e_comandos = ttk.Combobox(frame_tres, values=lista_comandos)
    e_comandos.set("Escolha...")
    e_comandos.place(x=30, y=50)

    botao_inserir = Button(frame_tres, text="INSERIR", command=gera_comando, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=560, y=3, width=100, height=50)
    botao_executar = Button(frame_tres, text="EXECUTAR", command=executa_comando, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=560, y=50, width=100, height=50)
    botao_limpar = Button(frame_tres, text="LIMPAR", command=clear, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=400, y=3, width=100, height=50)

    l_linha = Label(frame_tres, text='', width=700, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=1, y=110)

    #confgurando frame 4 --------------------
    l_updates = Label(frame_quatro, text='UPDATES', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_updates.place(x=5, y=16)

    botao_updatejava = Button(frame_quatro, text="UPDATE JAVA", command=" ", font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=100, y=60, width=150, height=50)
    botao_updatetomcat = Button(frame_quatro, text="UPDATE TOMCAT", command=" ", font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=450, y=60, width=150, height=50) 
    

    l_linha = Label(frame_quatro, text='', width=700, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=1, y=130)

    #configurando frame 5 ---------------------------
    l_infos = Label(frame_cinco, text='INFORMAÇÕES', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    l_infos.place(x=5, y=16)

    botao_relatorio = Button(frame_cinco, text="RELATORIO", command=infos, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=100, y=60, width=150, height=50)
    botao_versao = Button(frame_cinco, text="VERSÕES", command=version , font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE).place(x=450, y=60, width=150, height=50)
    
    l_linha = Label(frame_cinco, text='', width=700, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=1, y=130)

    #configurando frame 8 -------------------------------
    retorno_texto = Label(frame_oito, text="", background="#FFFFFF", justify=LEFT, font=('Ivy 12 bold'))
    retorno_texto.place(x=10, y=10, width=670, height=300)


    ########################################################
    



#configurando o  frame2 --------------
l_badge = Label(frame_sete, text='BADGE ID', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_badge.place(x=10, y=10)
e_badge = Entry(frame_sete, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_badge.place(x=14, y=40)

l_passw = Label(frame_sete, text='PASSWORD', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_passw.place(x=10, y=75)
e_passw = Entry(frame_sete, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_passw.place(x=14, y=110)

b_confirmar = Button(frame_sete, command=verifica_senha, text='ENTRAR', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=400, y=80)


janela_login.mainloop()