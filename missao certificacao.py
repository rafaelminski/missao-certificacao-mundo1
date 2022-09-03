from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import *
import _sqlite3
import os

conexao = _sqlite3.connect('tecnicos.db')

c = conexao.cursor()

c.execute(''' CREATE TABLE tecnicos (
    nome text,
    sobrenome text,
    email text,
    telefone text
    )
''')
conexao.commit()

conexao.close()

def mensagem_alerta(a, b):
    messagebox.showinfo(title=a, message=b)

def janela_login():
    janela_login = Tk()
    janela_login.geometry('410x450')
    janela_login.configure(background='powder blue')

    # inserindo Logo:
    pastaApp = os.path.dirname(__file__)
    imagem_logo = PhotoImage(file=pastaApp + '\\tv.png')
    imagem_logo = imagem_logo.subsample(5, 5)
    imagem = Label(janela_login, image=imagem_logo, background='powder blue')
    imagem.place(x=105, y=0)

    # definindo as escritas:
    janela_login.title('Missão Prática Mundo 1')
    frase = Label(master=janela_login, text='Seja bem-vindo!', background='powder blue', font=('arial', 18))
    frase.pack()
    frase.place(x=120, y=200)

    frase = Label(master=janela_login, text='Realize o login:', background='powder blue', font=('arial', 16))
    frase.pack()
    frase.place(x=140, y=230)

    usuario = Label(master=janela_login, text='Usuário:', background='powder blue', font=('arial', 12))
    usuario.pack()
    usuario.place(x=100, y=270)

    senh_a = Label(master=janela_login, text='Senha:', background='powder blue', font=('arial', 12))
    senh_a.pack()
    senh_a.place(x=100, y=310)

    # definindo caixas de entrada:
    nome = Entry(master=janela_login, background='powder blue')
    nome.get()
    nome.pack()
    nome.place(x=170, y=270)

    senha = Entry(master=janela_login, background='powder blue')
    senha.get()
    senha.pack()
    senha.place(x=170, y=310)

    # função help:
    menu = Menu(janela_login)
    janela_login.config(menu=menu)

    def helpp():
        help(sqlite3)

    subm = Menu(menu)
    menu.add_cascade(label='Help', menu=subm)
    subm.add_command(label='Sqlite3 Docs', command=helpp)

    # botão:
    def fun_botao1():
        if nome.get() == 'jonathan':
            if senha.get() == '123456':
                mensagem_alerta('Sucesso!', 'Login realizado com sucesso')
                janela_login.destroy()
                janela_reserva()
            else:
                mensagem_alerta('Erro', 'Senha incorreta!')
        else:
            mensagem_alerta('Erro!', 'Username incorreto!')

    botao = Button(master=janela_login, text='Entrar', command=fun_botao1)
    botao.pack()
    botao.place(x=210, y=370)

    def fun_botao2():
        janela_login.destroy()
        janela_cad_fun()

    botao2 = Button(master=janela_login, text='Cadastrar', command=fun_botao2)
    botao2.pack()
    botao2.place(x=115, y=370)

    janela_login.mainloop()

def janela_cad_fun():
    janela_cad_fun = Tk()
    janela_cad_fun.geometry('410x450')
    janela_cad_fun.configure(background='powder blue')

    # inserindo Logo:
    pastaApp = os.path.dirname(__file__)
    imagem_logo = PhotoImage(file=pastaApp + '\\tv.png')
    imagem_logo = imagem_logo.subsample(15, 15)
    imagem = Label(janela_cad_fun, image=imagem_logo, background='powder blue')
    imagem.place(x=30, y=30)

    # definindo as escritas:
    janela_cad_fun.title('Missão Prática Mundo 1')
    frase = Label(master=janela_cad_fun, text='Seja bem-vindo! \nPor favor, realize o cadastro abaixo:',
                  background='powder blue', font=('arial', 12))
    frase.pack()
    frase.place(x=130, y=50)

    cpf = Label(master=janela_cad_fun, text='CPF:', background='powder blue',
                          font=('arial', 10))
    cpf.pack()
    cpf.place(x=10, y=140)

    nome_completo = Label(master=janela_cad_fun, text='Nome completo:', background='powder blue', font=('arial', 10))
    nome_completo.pack()
    nome_completo.place(x=10, y=170)

    telefone = Label(master=janela_cad_fun, text='Telefone celular ou rádio:', background='powder blue', font=('arial', 10))
    telefone.pack()
    telefone.place(x=10, y=200)

    turno = Label(master=janela_cad_fun, text='Turno:', background='powder blue', font=('arial', 10))
    turno.pack()
    turno.place(x=10, y=230)

    nome_eqp = Label(master = janela_cad_fun, text = 'Nome da Equipe:', background = 'powder blue', font = ('arial', 10))
    nome_eqp.pack()
    nome_eqp.place(x=10, y=260)

    senh_a = Label(master=janela_cad_fun, text='Senha:', background='powder blue', font=('arial', 10))
    senh_a.pack()
    senh_a.place(x=10, y=290)

    email = Label(master=janela_cad_fun,text='Email:', background='powder blue', font=('arial', 10))
    email.pack()
    email.place(x=10, y=320)

    # definindo caixas de entrada:

    cpf = Entry(master=janela_cad_fun, background='powder blue')
    cpf.get()
    cpf.pack()
    cpf.place(x=170, y=140, relwidth=0.5)

    nome_completo = Entry(master=janela_cad_fun, background='powder blue')
    nome_completo.get()
    nome_completo.pack()
    nome_completo.place(x=170, y=170, relwidth=0.5)

    telefone = Entry(master=janela_cad_fun, background='powder blue')
    telefone.get()
    telefone.pack()
    telefone.place(x=170, y=200, relwidth=0.5)

    turno = Entry(master=janela_cad_fun, background='powder blue')
    turno.get()
    turno.pack()
    turno.place(x=170, y=230, relwidth=0.5)

    nome_eqp = Entry(master=janela_cad_fun, background='powder blue')
    nome_eqp.get()
    nome_eqp.pack()
    nome_eqp.place(x=170, y=260, relwidth=0.5)

    senh_a = Entry(master=janela_cad_fun, background='powder blue')
    senh_a.get()
    senh_a.pack()
    senh_a.place(x=170, y=290, relwidth=0.5)

    email = Entry(master=janela_cad_fun, background='powder blue')
    email.get()
    email.pack()
    email.place(x=170, y=320, relwidth=0.5)

    # função help:
    menu = Menu(janela_cad_fun)
    janela_cad_fun.config(menu=menu)

    def helpp():
        help(sqlite3)

    subm = Menu(menu)
    menu.add_cascade(label='Help', menu=subm)
    subm.add_command(label='Sqlite3 Docs', command=helpp)

    def fun_botao3():
        janela_cad_fun.destroy()
        janela_login()
    botao = Button(master=janela_cad_fun, text='Prosseguir', command=fun_botao3)
    botao.pack()
    botao.place(x=100, y=390, relwidth=0.55)

    janela_cad_fun.mainloop()

def janela_reserva():
    janela_reserva = Tk()
    janela_reserva.geometry('410x450')
    janela_reserva.configure(background='powder blue')

    # inserindo Logo:
    pastaApp = os.path.dirname(__file__)
    imagem_logo = PhotoImage(file=pastaApp + '\\tv.png')
    imagem_logo = imagem_logo.subsample(15, 15)
    imagem = Label(janela_reserva, image=imagem_logo, background='powder blue')
    imagem.place(x=20, y=30)

    # definindo as escritas:
    janela_reserva.title('Missão Prática Mundo 1')
    frase = Label(master=janela_reserva, text='Realize o cadastro de ferramentas abaixo:', background='powder blue',
                  font=('arial', 12))
    frase.pack()
    frase.place(x=100, y=60)

    cod_fer = Label(master=janela_reserva, text='Código da ferramenta:', background='powder blue', font=('arial', 10))
    cod_fer.pack()
    cod_fer.place(x=10, y=140)

    desc = Label(master=janela_reserva, text='Descrição da solicitação:', background='powder blue', font=('arial', 10))
    desc.pack()
    desc.place(x=10, y=170)

    data1 = Label(master=janela_reserva, text='Data de locação:', background='powder blue', font=('arial', 10))
    data1.pack()
    data1.place(x=10, y=230)

    hora1 = Label(master=janela_reserva, text='Horário de locação:', background='powder blue', font=('arial', 10))
    hora1.pack()
    hora1.place(x=10, y=260)

    data2 = Label(master=janela_reserva, text='Data de devolução:', background='powder blue', font=('arial', 10))
    data2.pack()
    data2.place(x=10, y=290)

    hora2 = Label(master=janela_reserva, text='Horário de devolução:', background='powder blue', font=('arial', 10))
    hora2.pack()
    hora2.place(x=10, y=320)

    tecnico = Label(master=janela_reserva, text='Técnico resposável:', background='powder blue', font=('arial', 10))
    tecnico.pack()
    tecnico.place(x=10, y=350)

    # definindo caixas de entrada:
    combo_cod_fer = Combobox(janela_reserva, values=('nenhuma', 1, 2, 3))  # inserir as id ferramentas substituindo os números!
    combo_cod_fer.current(0)
    combo_cod_fer.place(x=180, y=140, relwidth=0.52)
    fer_selecionada = combo_cod_fer.get()  # recupera o item selecionado em um combobox! Importante para interação com banco de dados!

    entry_desc = scrolledtext.ScrolledText(janela_reserva, width=24, height=3) #Coloquei esse Box para ficar mais organizado na hora do usuário escrever.
    entry_desc.pack()                                                          #Porém tem de ser verificacdo se há como puxar os dados de lá para entrar no relatório de locação.
    entry_desc.place(x=180, y=170)                                             #Se não, mudar para "Entry"!

    entry_data1 = Entry(master=janela_reserva, background='powder blue')
    entry_data1.get()
    entry_data1.pack()
    entry_data1.place(x=180, y=230, relwidth=0.52)

    combo_hora1 = Entry(master=janela_reserva, background='powder blue')
    combo_hora1.get()
    combo_hora1.pack()
    combo_hora1.place(x=180, y=260, relwidth=0.52)

    combo_data2 = Entry(master=janela_reserva, background='powder blue')
    combo_data2.get()
    combo_data2.pack()
    combo_data2.place(x=180, y=290, relwidth=0.52)

    combo_hora2 = Entry(master=janela_reserva, background='powder blue')
    combo_hora2.get()
    combo_hora2.pack()
    combo_hora2.place(x=180, y=320, relwidth=0.52)

    combo_tecnico = Combobox(janela_reserva, values=('nenhuma', 7, 8, 9)) # inserir os técnicos substituindo os números!
    combo_tecnico.current(0)
    tec_selecionado = combo_cod_fer.get()  # recupera o técnico selecionado em um combobox! Importante para interação com banco de dados!
    combo_tecnico.place(x=180, y=350, relwidth=0.52)

    # função help:
    menu = Menu(janela_reserva)
    janela_reserva.config(menu=menu)

    def helpp():
        help(sqlite3)

    subm = Menu(menu)
    menu.add_cascade(label='Help', menu=subm)
    subm.add_command(label='Sqlite3 Docs', command=helpp)

    def fun_botao5():
        res = messagebox.askquestion('Sucesso!','Ferramenta(s) reservada(s) com sucesso!\nGostaria de realizar outra reserva?')
        if res == 'yes':
            janela_reserva.destroy()
            janela_login()
        else:
            janela_reserva.destroy()
    botao = Button(master=janela_reserva, text='Concluído', command=fun_botao5)
    botao.pack()
    botao.place(x=50, y=400, relwidth=0.7)

    janela_reserva.mainloop()

def janela_cad_fer():
    janela_cad_fer = Tk()
    janela_cad_fer.geometry('410x450')
    janela_cad_fer.configure(background='powder blue')

    # inserindo Logo:
    pastaApp = os.path.dirname(__file__)
    imagem_logo = PhotoImage(file=pastaApp + '\\tv.png')
    imagem_logo = imagem_logo.subsample(15, 15)
    imagem = Label(janela_cad_fer, image=imagem_logo, background='powder blue')
    imagem.place(x=30, y=30)

    # definindo as escritas:
    janela_cad_fer.title('Missão Prática Mundo 1')
    frase = Label(master=janela_cad_fer, text='Seja bem-vindo! \nPor favor, realize o cadastro abaixo:', background='powder blue', font=('arial', 12))
    frase.pack()
    frase.place(x=130, y=50)

    id_ferramenta = Label(master=janela_cad_fer, text='ID da ferramenta:', background='powder blue', font=('arial', 10))
    id_ferramenta.pack()
    id_ferramenta.place(x=10, y=120)

    desc_ferramenta = Label(master=janela_cad_fer, text='Descrição da ferramenta:', background='powder blue', font=('arial', 10))
    desc_ferramenta.pack()
    desc_ferramenta.place(x=10, y=150)

    fabricante = Label(master=janela_cad_fer, text='Fabricante:', background='powder blue', font=('arial', 10))
    fabricante.pack()
    fabricante.place(x=10, y=180)

    voltagem = Label(master=janela_cad_fer, text='Voltagem de uso:', background='powder blue', font=('arial', 10))
    voltagem.pack()
    voltagem.place(x=10, y=210)

    part_number = Label(master=janela_cad_fer, text='Part number:', background='powder blue', font=('arial', 10))
    part_number.pack()
    part_number.place(x=10, y=240)

    tamanho = Label(master=janela_cad_fer, text='Tamanho:', background='powder blue', font=('arial', 10))
    tamanho.pack()
    tamanho.place(x=10, y=270)

    uni_med = Label(master=janela_cad_fer, text='Unidade de medida:', background='powder blue', font=('arial', 10))
    uni_med.pack()
    uni_med.place(x=10, y=300)

    tipo_fer = Label(master=janela_cad_fer, text='Tipo de ferramenta:', background='powder blue', font=('arial', 10))
    tipo_fer.pack()
    tipo_fer.place(x=10, y=330)

    mat_fer = Label(master=janela_cad_fer, text='Material da ferramenta:', background='powder blue', font=('arial', 10))
    mat_fer.pack()
    mat_fer.place(x=10, y=360)

    temp_max_fer = Label(master=janela_cad_fer, text='Tempo máximo de reserva:', background='powder blue', font=('arial', 10))
    temp_max_fer.pack()
    temp_max_fer.place(x=10, y=390)

    # definindo caixas de entrada:
    id_ferramenta = Entry(master=janela_cad_fer, background='powder blue')
    id_ferramenta.get()
    id_ferramenta.pack()
    id_ferramenta.place(x=170, y=120, relwidth=0.5)

    desc_ferramenta = Entry(master=janela_cad_fer, background='powder blue')
    desc_ferramenta.get()
    desc_ferramenta.pack()
    desc_ferramenta.place(x=170, y=150, relwidth=0.5)

    fabricante = Entry(master=janela_cad_fer, background='powder blue')
    fabricante.get()
    fabricante.pack()
    fabricante.place(x=170, y=180, relwidth=0.5)

    voltagem = Entry(master=janela_cad_fer, background='powder blue')
    voltagem.get()
    voltagem.pack()
    voltagem.place(x=170, y=210, relwidth=0.5)

    part_number = Entry(master=janela_cad_fer, background='powder blue')
    part_number.get()
    part_number.pack()
    part_number.place(x=170, y=240, relwidth=0.5)

    tamanho = Entry(master=janela_cad_fer, background='powder blue')
    tamanho.get()
    tamanho.pack()
    tamanho.place(x=170, y=270, relwidth=0.5)

    uni_med = Entry(master=janela_cad_fer, background='powder blue')
    uni_med.get()
    uni_med.pack()
    uni_med.place(x=170, y=300, relwidth=0.5)

    tipo_fer = Entry(master=janela_cad_fer, background='powder blue')
    tipo_fer.get()
    tipo_fer.pack()
    tipo_fer.place(x=170, y=330, relwidth=0.5)

    mat_fer = Entry(master=janela_cad_fer, background='powder blue')
    mat_fer.get()
    mat_fer.pack()
    mat_fer.place(x=170, y=360, relwidth=0.5)

    temp_max_fer = Entry(master=janela_cad_fer, background='powder blue')
    temp_max_fer.get()
    temp_max_fer.pack()
    temp_max_fer.place(x=170, y=390, relwidth=0.5)

    # função help:
    menu = Menu(janela_cad_fer)
    janela_cad_fer.config(menu=menu)

    def helpp():
        help(sqlite3)

    subm = Menu(menu)
    menu.add_cascade(label='Help', menu=subm)
    subm.add_command(label='Sqlite3 Docs', command=helpp)

    # botão:
    def fun_botao4():
        janela_cad_fer.destroy()
        janela_login()
    botao = Button(master=janela_cad_fer, text='Concluído', command=fun_botao4)
    botao.pack()
    botao.place(x=50, y=420, relwidth=0.7)

    janela_cad_fer.mainloop()

janela_login()
