import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # ------------------- Widgets -------------------
        # Campo de entrada de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Permitir Enter para añadir tarea

        # Botones
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=5)

        self.btn_add = tk.Button(frame_buttons, text="Añadir Tarea", width=15, command=self.add_task)
        self.btn_add.grid(row=0, column=0, padx=5)

        self.btn_complete = tk.Button(frame_buttons, text="Marcar como Completada", width=20, command=self.complete_task)
        self.btn_complete.grid(row=0, column=1, padx=5)

        self.btn_delete = tk.Button(frame_buttons, text="Eliminar Tarea", width=15, command=self.delete_task)
        self.btn_delete.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=60, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Evento opcional: doble clic para marcar como completada
        self.task_listbox.bind("<Double-1>", self.complete_task)

        # Lista interna para almacenar tareas
        self.tasks = []

    # ------------------- Funciones -------------------
    def add_task(self, event=None):
        """Añade una nueva tarea desde el campo de entrada"""
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"text": task, "done": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Escribe una tarea antes de añadirla.")

    def complete_task(self, event=None):
        """Marca una tarea como completada cambiando su estado"""
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.update_listbox()
        except IndexError:
            messagebox.showinfo("Selección Vacía", "Selecciona una tarea para marcarla como completada.")

    def delete_task(self):
        """Elimina la tarea seleccionada"""
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            messagebox.showinfo("Selección Vacía", "Selecciona una tarea para eliminarla.")

    def update_listbox(self):
        """Refresca la vista de la lista de tareas"""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task["done"]:
                self.task_listbox.insert(tk.END, f"✔ {task['text']}")
            else:
                self.task_listbox.insert(tk.END, task["text"])


# ------------------- Ejecución -------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
