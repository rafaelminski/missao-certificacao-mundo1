#----------------------------------------------------------------------------------------------------------------------
# Classes Técnico
#----------------------------------------------------------------------------------------------------------------------
from tkinter import *
from PIL import Image, ImageTk

class TecnicoBD:
    def __init__(self, win):
        #self.objBD = crud.AppBD()

        # Inserindo Logo:
        self.image = Image.open('tecnico.png').resize((70,70))
        self.photo = ImageTk.PhotoImage(self.image)
        self.labelImage = Label(win, image=self.photo)
        self.labelImage.image = self.photo
        self.labelImage.grid(row=0, column=0, columnspan=8, padx=10, pady=20)
        self.frase = Label(win, text='Nesta tela você pode cadastrar, excluir ou atualizar técnicos.',
                           font=('arial', 12)).grid(row=1, column=0, columnspan=8, padx=10, pady=10)

        # Componente Label e Entrada de Dados
        self.lblNome = Label(win, text='Nome').grid(row=3, column=0, padx=5, pady=5)
        self.txtNome = Entry(win, width=40).grid(row=3, column=1, padx=5, pady=5)

        self.lblCpf = Label(win, text='CPF').grid(row=3, column=2, padx=5, pady=5)
        self.txtCpf = Entry(win).grid(row=3, column=3, padx=5, pady=5)

        self.lblCelular = Label(win, text='Celular').grid(row=3, column=4, padx=5, pady=5)
        self.txtCelular = Entry(win).grid(row=3, column=5, padx=5, pady=5)

        self.lblTurno = Label(win, text='Turno').grid(row=3, column=6, padx=5, pady=5)
        self.txtTurno = Entry(win).grid(row=3, column=7, padx=5, pady=5)

        self.lblEquipe = Label(win, text='Equipe').grid(row=4, column=0, padx=5, pady=5)
        self.txtEquipe = Entry(win, width=40).grid(row=4, column=1, padx=5, pady=5)

        self.lblTipo = Label(win, text='Tipo de Usuário').grid(row=4, column=2, padx=5, pady=5)
        self.txtTipo = Entry(win).grid(row=4, column=3, padx=5, pady=5)

        self.lblLogin = Label(win, text='Login').grid(row=4, column=4, padx=5, pady=5)
        self.txtLogin = Entry(win).grid(row=4, column=5, padx=5, pady=5)

        self.lblSenha = Label(win, text='Senha').grid(row=4, column=6, padx=5, pady=5)
        self.txtSenha = Entry(win, show="*").grid(row=4, column=7, padx=5, pady=5)











        # Butões
        # self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        # self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        # self.btnExcluir = tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        # self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela)

        # Posicionamento dos componentes na janela
        # self.imagem.place(x=380, y=10)
        # self.frase.place(x=210, y=100)





if __name__ == "__main__":
    janela = Tk()
    janela.geometry("930x650")
    janela.title('Bem Vindo a Aplicação de Banco de Dados')

    frame_tecnico = Frame(janela, width=930, height=650)
    TecnicoBD(frame_tecnico)

    frame_tecnico.pack()


    janela.mainloop()
