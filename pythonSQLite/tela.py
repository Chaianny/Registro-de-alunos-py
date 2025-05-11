from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from faker import Faker
fake = Faker('pt_BR')
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
from datetime import date

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"  # letra
co6 = "#146C94"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde

# criando janela
janela = Tk()
janela.title("")
janela.geometry('810x535')
janela.configure(background=co1)
janela.resizable(width=False, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# CRIANDO FRAMES
def setFrame(width, height, bg):
    frame = Frame(janela, width=width, height=height, bg=bg )
    frame.grid(row=0, column=0, pady=0, sticky=NSEW, columnspan=5)
    return frame
frame_logo = setFrame(850, 52, co6)

def setFrameBotoes(width, height, bg):
    frame = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
    frame.grid(row=1, column=0, pady=1, sticky=NSEW)
    return frame
frame_botoes = setFrameBotoes(100, 200, co1)

def setFrameDetails():
    frame = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
    frame.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)
    return frame
frame_details = setFrameDetails()

def setFrameTable():
    frame = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
    frame.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)
    return frame
frame_table = setFrameTable()

# Logo
global imagem, imagem_string, l_imagem

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Registro de Alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)


# CAMPOS DE ENTRADA

l_nome = Label(frame_details, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=40)

l_email = Label(frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_tel = Label(frame_details, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_tel.place(x=4, y=130)
e_tel = Entry(frame_details, width=15, justify='left', relief='solid')
e_tel.place(x=7, y=160)

l_data_nascimento = Label(frame_details, text="Data de Nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_data_nascimento.place(x=220, y=10)
data_nascimento = DateEntry(frame_details, width=18, justify='center', bg='darkblue', foreground='white', borderwidth=2, year=2025)
data_nascimento.place(x=224, y=40)

l_endereco = Label(frame_details, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_endereco.place(x=220, y=70)
e_endereco = Entry(frame_details, width=15, justify='left', relief='solid')
e_endereco.place(x=224, y=100)

l_sexo = Label(frame_details, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify='center')
c_sexo['values'] = ('Mulher cis', 'Homem cis', 'Mulher Trans', 'Homem Trans', 'Não Binário')
c_sexo.place(x=130, y=160)

curso_falsos = [fake.job() for _ in range(100)]

l_curso = Label(frame_details, text="Curso *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_curso.place(x=220, y=130)
c_curso = ttk.Combobox(frame_details, width=24, font=('Ivy 8 bold'), justify='center')
c_curso['values'] = curso_falsos
c_curso.place(x=224, y=160)

def filtrar_cursos(event):
    texto = c_curso.get().lower()
    filtrados = [curso for curso in curso_falsos if texto in curso.lower()]
    c_curso['values'] = filtrados if filtrados else curso_falsos
    c_curso.event_generate('<Down>')

c_curso.bind("<KeyRelease>", filtrar_cursos)

def preencher_dados_falsos():
    e_nome.delete(0, END)
    e_nome.insert(0, fake.name())
    e_email.delete(0, END)
    e_email.insert(0, fake.email())
    e_tel.delete(0, END)
    e_tel.insert(0, fake.phone_number())
    e_endereco.delete(0, END)
    e_endereco.insert(0, fake.address())
    c_sexo.set(fake.random_element(elements=c_sexo['values']))
    data = fake.date_of_birth(minimum_age=18, maximum_age=60)
    data_nascimento.set_date(data)
    c_curso.set(fake.random_element(elements=curso_falsos))

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem_path = fd.askopenfilename()
    if imagem_path:
        imagem_string = imagem_path
        nova_imagem = Image.open(imagem_string)
        nova_imagem = nova_imagem.resize((130, 130))
        imagem = ImageTk.PhotoImage(nova_imagem)
        l_imagem.configure(image=imagem)
        l_imagem.image = imagem  
        botao_carregar.config(text="Trocar de Foto".upper())

imagem = Image.open('Foto.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co6)
l_imagem.place(x=495, y=10)  

botao_carregar = Button(
    frame_details,
    command=escolher_imagem,
    text='Carregar Foto'.upper(),
    width=20,
    compound=CENTER,
    anchor=CENTER,
    overrelief=RIDGE,
    font=('Ivy 7 bold'),
    bg=co1,
    fg=co0
)

botao_carregar.place(x=500 + (130 - 140) // 2, y=150)


class RegistrationSystem:
    def __init__(self):
        self.students = []

    def view_all_students(self):
        return self.students

    def add_student(self, student_data):
        self.students.append(student_data)

registration_system = RegistrationSystem()

# Adicionando aluno fictício só pra teste visual
registration_system.add_student((
    "João da Silva", "joao@email.com", "99999-9999", "Homem cis", "10/05/1990", "Rua das Flores, 123", "Engenheiro de Software"
))

def mostrar_alunos():
    list_header = ['id', 'Nome', 'email', 'Telefone', 'sexo', 'Data', 'Endereço', 'Curso']

    df_list = registration_system.view_all_students()

    tree_aluno = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree_aluno.yview)
    hsb = ttk.Scrollbar(frame_table, orient='horizontal', command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_table.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center"]
    h = [40, 150, 150, 70, 70, 70, 120, 100]
    
    for n, col in enumerate(list_header):
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        tree_aluno.column(col, width=h[n], anchor=hd[n])

    for idx, item in enumerate(df_list):
        tree_aluno.insert('', 'end', values=[idx+1] + list(item))


# Chamando a Tabela
mostrar_alunos()

# Procurando Aluno
frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text= " Procurar aluno [Entra ID]", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='left', relief='solid', font=('Ivy 10'))
e_procurar.grid(row=1, column=0, padx=0, sticky=NSEW)

botao_alterar = Button(frame_procurar, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_alterar.grid(row=1, column=1, padx=0, sticky=NSEW)


# Configura o frame para expandir a coluna 0
frame_botoes.columnconfigure(0, weight=1)

# Botão Adicionar
imagem_add = Image.open('Add.png')
imagem_add = imagem_add.resize((25, 25))
imagem_add = ImageTk.PhotoImage(imagem_add)

botao_adicionar = Button(
    frame_botoes, 
    image=imagem_add, 
    text='Adicionar', 
    compound=LEFT,
    font=('Ivy 11'), 
    bg=co1, 
    fg=co0,
    anchor=CENTER,
    relief=GROOVE,
    overrelief=RIDGE,
    padx=5
)
botao_adicionar.image = imagem_add
botao_adicionar.grid(row=2, column=0, padx=10, pady=5, sticky='we')


# Botão Atualizar
app_img_atualizar = Image.open('Atualizar.png')
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)

botao_atualizar = Button(
    frame_botoes, 
    image=app_img_atualizar, 
    text='Atualizar', 
    compound=LEFT, 
    font=("Ivy 11"), 
    bg=co1, 
    fg=co0,
    anchor=CENTER,
    relief=GROOVE,
    overrelief=RIDGE,
    padx=5
)
botao_atualizar.image = app_img_atualizar
botao_atualizar.grid(row=3, column=0, padx=10, pady=5, sticky='we')


# Botão Deletar
app_img_deletar = Image.open('Deletar.png')
app_img_deletar = app_img_deletar.resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)

botao_deletar = Button(
    frame_botoes, 
    image=app_img_deletar, 
    text='Deletar', 
    compound=LEFT, 
    font=("Ivy 11"), 
    bg=co1, 
    fg=co0,
    anchor=CENTER,
    relief=GROOVE,
    overrelief=RIDGE,
    padx=5
)
botao_deletar.image = app_img_deletar
botao_deletar.grid(row=3, column=0, padx=10, pady=5, sticky='we')


janela.mainloop()
