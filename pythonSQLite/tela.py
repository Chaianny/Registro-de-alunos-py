import contextlib
from ast import Delete
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from turtle import goto
from faker import Faker
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime
from tkinter.constants import NW
import sqlite3

fake = Faker('pt_BR')

# Cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"  # letra
co6 = "#146C94"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('808x540')
janela.configure(background=co1)
janela.resizable(width=False, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando frames
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
    frame = Frame(janela, width=800, height=230, bg=co1, relief=SOLID)
    frame.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)
    return frame
frame_details = setFrameDetails()

def setFrameTable():
    frame = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
    frame.grid(row=3, column=0, pady=0, padx=(10,0), sticky="NSEW", columnspan=5)
    return frame
frame_table = setFrameTable()

# Logo
app_lg = Image.open('Logo.png').resize((50, 50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Registro de Alunos", width=850, compound=LEFT, anchor=CENTER, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

# Campos de entrada
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
e_endereco = Entry(frame_details, width=25, justify='left', relief='solid')
e_endereco.place(x=224, y=100)

l_sexo = Label(frame_details, text="Genero *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_details, width=13, font=('Ivy 8 bold'), justify='center')
c_sexo['values'] = ('Mulher Cis', 'Homem Cis', 'Mulher Trans', 'Homem Trans', 'Não Binário')
c_sexo.place(x=110, y=160)

curso_falsos = [fake.job() for _ in range(100)]

l_curso = Label(frame_details, text="Curso *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_curso.place(x=220, y=130)
c_curso = ttk.Combobox(frame_details, width=24, font=('Ivy 8 bold'), justify='center')
c_curso['values'] = curso_falsos
c_curso.place(x=224, y=160)

def filtrar_cursos(event):
    texto = c_curso.get().lower()
    filtrados = [curso for curso in curso_falsos if texto in curso.lower()]
    c_curso['values'] = filtrados or curso_falsos
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
    global imagem, imagem_string
    if imagem_path := fd.askopenfilename():
        imagem_string = imagem_path
        nova_imagem = Image.open(imagem_string).resize((130, 130))
        imagem = ImageTk.PhotoImage(nova_imagem)
        l_imagem.configure(image=imagem)
        l_imagem.image = imagem
        botao_carregar.config(text="Trocar de Foto", width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)

imagem = Image.open('Foto.png').resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co6)
l_imagem.place(x=420, y=10)  

botao_carregar = Button(frame_details, command=escolher_imagem, text='CARREGAR FOTO', width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_carregar.place(x=425 + (130 - 140) // 2, y=150)

# Classe para o banco de dados
class RegistrationSystem:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")  # Ajuste o nome conforme seu banco
        self.c = self.conn.cursor()
        self.create_table()

    def search_student(self):
        return self._extracted_from_view_all_students_2("SELECT * FROM student_id")
    
    def search_student_by_id(self, student_id):
        self.c.execute("SELECT *FROM students WHERE id = ?",(student_id))
        return self.c.fetchone
    
    def procurar_aluno():
        student_id = e_procurar.get()
        if not student_id.isdigit():
            messagebox.showerror("Error", "Digite um ID {student_id} válido.")
            return
        if resultado := registration_system.search_student_by_id(student_id):
            _, name, email, phone, gender, birth, address, course, picture = resultado
            

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            gender TEXT NOT NULL,
            birth TEXT NOT NULL,
            address TEXT NOT NULL,
            course TEXT NOT NULL,
            picture TEXT NOT NULL)''')
        self.conn.commit()

    def register_student(self, student):
        self.c.execute("INSERT INTO students(name, email, phone, gender, birth, address, course, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", student)
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Registro realizado com sucesso!')

    def view_all_students(self):
        return self.c.execute("SELECT * FROM students")



    def delete_student(self, student_id):
        self.c.execute("DELETE FROM students WHERE id = ?", (student_id))
        self.conn.commit()
        messagebox.showinfo("Sucesso", f"Aluno com ID {student_id} deletado com sucesso!")

registration_system = RegistrationSystem()

def deletar_aluno():
    student_id = e_procurar.get()
    registration_system.delete_student(student_id=student_id) 
    mostrar_alunos()

def atualizar_aluno():
    aluno_id = e_procurar.get().strip()
    if not aluno_id.isdigit():
        messagebox.showwarning("ID inválido", "Digite um ID válido para atualizar.")
        return

    dados = {
        "id": int(aluno_id),
        "name": e_nome.get(),
        "email": e_email.get(),
        "phone": e_tel.get(),
        "gender": c_sexo.get(),
        "birth": data_nascimento.get_date().strftime('%d/%m/%Y'),
        "address": e_endereco.get(),
        "course": c_curso.get(),
        "picture": imagem_string if 'imagem_string' in globals() else ""
    }
    registration_system.update_student(dados)
    messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")


def update_student(self, dados):
    cursor = self.conn.cursor()
    cursor.execute("""
        UPDATE students SET
        name = ?,
        email = ?,
        phone = ?,  
        gender = ?,
        birth = ?,
        address = ?,
        course = ?,
        picture = ?
        WHERE id = ?
    """, (
        dados["name"],
        dados["email"],
        dados["phone"],
        dados["gender"],
        dados["birth"],
        dados["address"],   
        dados["course"],
        dados["picture"],
        dados["id"]
    ))
    self.conn.commit()  
            

def procurar_aluno():
    aluno_id = e_procurar.get()

    if not aluno_id:
        messagebox.showwarning("Aviso", "Digite um ID para procurar.")
        return

    if resultado := registration_system.buscar_por_id(aluno_id):
        _extracted_from_procurar_aluno(resultado)
    else:
        messagebox.showinfo("Não encontrado", f"Nenhum aluno com ID {aluno_id} foi encontrado.")


# TODO Rename this here and in `procurar_aluno`
def _extracted_from_procurar_aluno(resultado):
    # Desempacotar os dados retornados
    name, email, phone, gender, birth, address, course, picture = resultado

    # Preencher os campos da interface
    e_nome.delete(0, Tk.END)
    e_nome.insert(0, name)

    e_email.delete(0, Tk.END)
    e_email.insert(0, email)

    _extracted_from_procurar_aluno(e_tel, phone, c_sexo, gender)
    # Converter string da data para o formato aceito pelo DateEntry
    data_formatada = datetime.strptime(birth, '%d/%m/%Y')
    data_nascimento.set_date(data_formatada)

    _extracted_from_procurar_aluno(e_endereco, address, c_curso, course)
    # Se quiser lidar com imagem, você pode carregar aqui
    global imagem_string
    imagem_string = imagem


# TODO Rename this here and in `procurar_aluno`
def _extracted_from_procurar_aluno(arg0, arg1, arg2, arg3):
    arg0.delete(0, Tk.END)
    arg0.insert(0, arg1)

    arg2.set(arg3)

def buscar_por_id(self, aluno_id):
    cursor = self.conn.cursor()
    cursor.execute("""
        SELECT name, email, phone, gender, birth, address, course, picture 
        FROM students 
        WHERE id = ?
    """, (aluno_id,))
    return cursor.fetchone()


def adicionar_aluno():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_tel.get()
    genero = c_sexo.get()
    data = data_nascimento.get_date().strftime('%d/%m/%Y')
    endereco = e_endereco.get()
    curso = c_curso.get()
    foto = imagem_string if 'imagem_string' in globals() else ""
    if nome and email and telefone:
        dados = (nome, email, telefone, genero, data, endereco, curso, foto)
        registration_system.register_student(dados)
        mostrar_alunos()
    else:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha os campos obrigatórios (*).")

def mostrar_alunos():
    list_header = ['id', 'Nome', 'email', 'Telefone', 'Genero', 'Data', 'Endereço', 'Curso']
    df_list = registration_system.view_all_students()

    for widget in frame_table.winfo_children():
        widget.destroy()

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
        tree_aluno.insert('', 'end', iid=str(idx), values=item)

mostrar_alunos()

frame_procurar = Frame(frame_botoes, width=40, height=55, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text= " Procurar aluno [Entra ID]", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='left', relief='solid', font=('Ivy 10'))
e_procurar.grid(row=1, column=0, padx=0, sticky=NSEW)
e_procurar.insert(END, "123")

botao_alterar = Button(frame_procurar, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_alterar.grid(row=1, column=1, padx=0, sticky=NSEW)

frame_botoes.columnconfigure(0, weight=1)

imagem_add = Image.open('Add.png').resize((25, 25))
imagem_add = ImageTk.PhotoImage(imagem_add)

botao_adicionar = Button(frame_botoes, image=imagem_add, text='Adicionar', compound=LEFT, font=('Ivy 11'), bg=co1, fg=co0, anchor=CENTER, relief=GROOVE, overrelief=RIDGE, padx=5, command=adicionar_aluno)
botao_adicionar.image = imagem_add
botao_adicionar.grid(row=2, column=0, padx=10, pady=5, sticky='we')

app_img_atualizar = Image.open('Atualizar.png').resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)

botao_atualizar = Button(frame_botoes, image=app_img_atualizar, text='Atualizar', compound=LEFT, font=("Ivy 11"), bg=co1, fg=co0, anchor=CENTER, relief=GROOVE, overrelief=RIDGE, padx=5, command=atualizar_aluno)
botao_atualizar.image = app_img_atualizar
botao_atualizar.grid(row=3, column=0, padx=10, pady=5, sticky='we')

app_img_deletar = Image.open('Deletar.png').resize((25,25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)

botao_deletar = Button(frame_botoes, image=app_img_deletar, text='Deletar', compound=LEFT, font=("Ivy 11"), bg=co1, fg=co0, anchor=CENTER, relief=GROOVE, overrelief=RIDGE, padx=5, command=deletar_aluno)
botao_deletar.image = app_img_deletar
botao_deletar.grid(row=4, column=0, padx=10, pady=5, sticky='we')

janela.mainloop()

