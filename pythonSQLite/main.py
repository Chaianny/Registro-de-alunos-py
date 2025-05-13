import sqlite3
from tkinter import messagebox

class RegistrationSystem:
    def __init__(self):
        self.conn = sqlite3.connect('students.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS students
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        self.c.execute("INSERT INTO students(name, email,phone, gender, birth, address, course, picture) VALUES (?,?,?,?,?,?,?,?)", 
                        (student))
        self.conn.commit()
        # Mostrando mesnsagem de sucesso
        messagebox.showinfo('Sucesso', 'Registo com sucesso!')
        print("Registration successful!")

    def view_all_students(self):
        self.c.execute("SELECT * FROM students")
        data = self.c.fetchall()
        return data

    def search_student(self, id):
        self.c.execute("SELECT * FROM students WHERE id=?", (id,))
        if data := self.c.fetchone():
            return data
        else:
            messagebox.showerror('Erro', f'No student with ID {id} found.')

    def update_student(self, new_values):
        if data := new_values:
            query = "UPDATE students SET name=?, email=?, phone=?, gender=?, birth=?, address=?, course=?, picture=? WHERE id=?"
            self.c.execute(query,new_values)
            self.conn.commit()
            messagebox.showinfo('Sucesso', f'Student with ID {new_values[8]} has been updated.')
        else:
            messagebox.showerror('Erro', f"No student with ID {new_values[8]} found.")
            print(f"No student with ID '{new_values[8]}' found.")

    def delete_student(self, id):
        self.c.execute("SELECT * FROM students WHERE id=?", (id,))
        if data := self.c.fetchone():
            self.c.execute("DELETE FROM students WHERE id=?", (id,))
            self.conn.commit()
            messagebox.showinfo('Sucesso', f"Student with ID {id} has been deleted.")
            print(f"Student with ID '{id}' has been deleted.")
        else:
            messagebox.showerror('Erro', f"No student with ID {id} found.")
            print(f"No student with ID '{id}' found.")


# create a registration system instance
registration_system = RegistrationSystem()