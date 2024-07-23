from usuario import Usuarios
from tkinter import *

class Application:
    def __init__(self):
        # DISPLAY
        self.window = Tk()
        self.window.title("Informe os DADOS")
        self.window.configure(bg="#4F4F4F")
        self.window.geometry("700x600")
        self.window.resizable(True, True)
        self.window.maxsize(width=1000, height=700)
        self.window.minsize(width=500, height=400)
#----------------------------------------------------------------------------------------------------------------------
# BLOCO Do LOGO
        self.imgLogo = PhotoImage(file="back.png")
        self.frameLogo = Frame(self.window, bg="black")
        self.frameLogo.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.13)
        self.logo = Label(self.frameLogo, image=self.imgLogo, bg="black")
        self.logo.pack(side="left")
#----------------------------------------------------------------------------------------------------------------------
#FRAME 1
        self.frame1 = Frame(self.window, bd=4, bg="#363636")  # , highlightbackground="#808080", highlightthickness=5)
        self.frame1.place(relx=0.02, rely=0.17, relwidth=0.96, relheight=0.79)
#----------------------------------------------------------------------------------------------------------------------
#BOTÕES
        #buscar
        self.bntBuscar = Button(self.frame1, text=" Buscar ", bg="#FA8072", font="arial 10 bold", fg="white",
                                 command=self.buscarUsuario)
        self.bntBuscar.place(relx=0.22, rely=0.02, relwidth=0.10, relheight=0.1)


#----------------------------------------------------------------------------------------------------------
# ID DO USUARIO
        self.lblidusuario = Label(self.frame1, text=" idUsuario", bg="#363636", font="arial 10 bold", fg="silver")
        self.lblidusuario.place(relx=0.05, rely=0.02)
        self.txtidusuario = Entry(self.frame1, bg="#4F4F4F", fg="silver", font="arial 10 bold")
        self.txtidusuario.place(relx=0.05, rely=0.08, relwidth=0.14)

#NOME
        self.lblnome = Label(self.frame1, text="Nome", bg="#363636", font="arial 10 bold", fg="silver")
        self.lblnome.place(relx=0.05, rely=0.14)
        self.txtnome = Entry(self.frame1, bg="#4F4F4F", fg="silver", font="arial 10 bold")
        self.txtnome.place(relx=0.05, rely=0.20, relwidth=0.80)

#TELEFONE
        self.lbltelefone = Label(self.frame1, text="Telefone:", bg="#363636", font="arial 10 bold", fg="silver")
        self.lbltelefone.place(relx=0.05, rely=0.27)
        self.txttelefone = Entry(self.frame1, bg="#4F4F4F", fg="silver", font="arial 10 bold")
        self.txttelefone.place(relx=0.05, rely=0.33, relwidth=0.30)

#EMAIL
        self.lblemail = Label(self.frame1, text="email:", bg="#363636", font="arial 10 bold", fg="silver")
        self.lblemail.place(relx=0.38, rely=0.27)
        self.txtemail = Entry(self.frame1, bg="#4F4F4F", fg="silver", font="arial 10 bold")
        self.txtemail.place(relx=0.38, rely=0.33, relwidth=0.50)

#USUARIO
        self.lblusuario = Label(self.frame1, text="Usuario: ", bg="#363636", font="arial 10 bold", fg="silver")
        self.lblusuario.place(relx=0.05, rely=0.40)
        self.txtusuario = Entry(self.frame1, bg="#4F4F4F", fg="silver", font="arial 10 bold")
        self.txtusuario.place(relx=0.05, rely=0.47, relwidth=0.30)

#SENHA
        self.lblsenha = Label(self.frame1, text="Senha:", bg="#363636", font="arial 10 bold", fg="silver")
        self.lblsenha.place(relx=0.05, rely=0.53)
        self.txtsenha = Entry(self.frame1, bg="#4F4F4F", fg="silver",show="*", font="arial 10 bold")
        self.txtsenha.place(relx=0.05, rely=0.6, relwidth=0.30)

        # inserir
        self.bntInsert = Button(self.frame1, text=" Inserir ", bg="#32CD32", font="arial 10 bold", fg="white",command=self.inserirUsuario)
        self.bntInsert.place(relx=0.09, rely=0.7, relwidth=0.10, relheight=0.1)

        # alterar
        self.bntAlterar = Button(self.frame1, text=" Alterar ", bg="#FFA500", font="arial 10 bold", fg="white",command=self.alterarUsuario)
        self.bntAlterar.place(relx=0.20, rely=0.7, relwidth=0.10, relheight=0.1)

        # excluir
        self.bntExcluir = Button(self.frame1, text=" Excluir ", bg="#D2691E", font="arial 10 bold", fg="white",command=self.excluirUsuario)
        self.bntExcluir.place(relx=0.31, rely=0.7, relwidth=0.10, relheight=0.1)

        #MENSAGENS
        self.lblmsg = Label(self.frame1, text=" ", bg="#363636", fg="silver", font="System 16 bold")
        self.lblmsg.place(relx=0.38, rely=0.50, relwidth=0.60, relheight=0.10)

        self.window.mainloop()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.selectUser(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, user.telefone)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)

        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, user.senha)


Application()