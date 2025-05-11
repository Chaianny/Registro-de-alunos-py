import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('student.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            tel TEXT NOT NULL,
            sexo TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            endereco TEXT NOT NULL,
            curso TEXT NOT NULL,
            picture TEXT NOT NULL
        )''')

    def register_student(self, student):
        self.c.execute("INSERT INTO students(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?,?,?,?,?,?,?,?)",
                       student)
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Registrado com sucesso!')

    def view_all_students(self):
        self.c.execute("SELECT * FROM students")
        alunos = self.c.fetchall()
        for aluno in alunos:
            print(f'ID: {aluno[0]} | Nome: {aluno[1]} | Email: {aluno[2]} | Tel: {aluno[3]} | Sexo: {aluno[4]} | Data de nascimento: {aluno[5]} | Endereço: {aluno[6]} | Curso: {aluno[7]} | Imagem: {aluno[8]}')

    def search_student(self, id):
        self.c.execute("SELECT * FROM students WHERE id=?", (id,))
        dados = self.c.fetchone()
        if dados:
            print(f'ID: {dados[0]} | Nome: {dados[1]} | Email: {dados[2]} | Tel: {dados[3]} | Sexo: {dados[4]} | Data de nascimento: {dados[5]} | Endereço: {dados[6]} | Curso: {dados[7]} | Imagem: {dados[8]}')
        else:
            print(f"Estudante com ID {id} não encontrado.")

    def update_student(self, novo_valores):
        query = "UPDATE students SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=?"
        self.c.execute(query, novo_valores)
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Estudante com ID: {novo_valores[8]} foi atualizado!')

    def delete_student(self, id):
        self.c.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Estudante com ID: {id} foi deletado!')


# CRIANDO UMA INSTÂNCIA DO SISTEMA
sistema_de_registro = SistemaDeRegistro()

# EXEMPLO DE REGISTRO
# estudante = ('Jayle', 'bolinha@gmail.com', '7842', 'F', '13/11/2000', 'Brasil, Rio Grande do Norte', 'Arquiteto', 'imagem2.png')
# sistema_de_registro.register_student(estudante)

# VER TODOS OS ESTUDANTES
# sistema_de_registro.view_all_students()

# PROCURAR ALUNO
# aluno = sistema_de_registro.search_student(2)

# ATUALIZAR ALUNO
# estudante = ('Jayle', 'bolinha@gmail.com', '7842', 'F', '13/11/2000', 'Brasil, Rio Grande do Norte', 'Jogadora de Futebol', 'imagem2.png', '2')
# aluno = sistema_de_registro.update_student(estudante)

# deletar 
# sistema_de_registro.delete_student(2)

# VER TODOS OS ESTUDANTES
todos_alunos = sistema_de_registro.view_all_students()