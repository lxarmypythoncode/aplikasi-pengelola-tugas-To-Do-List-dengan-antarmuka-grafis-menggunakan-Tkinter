import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame,
            width=50,
            height=10,
            selectmode=tk.SINGLE,
            font=('Helvetica', 14)
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, font=('Helvetica', 14))
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_task_button = tk.Button(
            self.button_frame,
            text='Add Task',
            command=self.add_task,
            font=('Helvetica', 14)
        )
        self.add_task_button.pack(side=tk.LEFT, padx=10)

        self.delete_task_button = tk.Button(
            self.button_frame,
            text='Delete Task',
            command=self.delete_task,
            font=('Helvetica', 14)
        )
        self.delete_task_button.pack(side=tk.LEFT, padx=10)

        self.clear_task_button = tk.Button(
            self.button_frame,
            text='Clear Tasks',
            command=self.clear_tasks,
            font=('Helvetica', 14)
        )
        self.clear_task_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_tasks(self):
        self.tasks = []
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
