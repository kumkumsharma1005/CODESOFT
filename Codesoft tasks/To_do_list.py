import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self.task_var = tk.StringVar()

        self.create_widgets()
        self.update_listbox()

    def create_widgets(self):
        tk.Label(self.root, text="To-Do List", font=("Helvetica", 18)).pack(pady=10)

        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=5)

        tk.Entry(entry_frame, textvariable=self.task_var, width=25, font=("Arial", 12)).grid(row=0, column=0, padx=5)
        tk.Button(entry_frame, text="Add Task", command=self.add_task).grid(row=0, column=1)

        self.listbox = tk.Listbox(self.root, width=45, height=15, font=("Arial", 12))
        self.listbox.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        tk.Button(button_frame, text="Mark as Done", command=self.mark_done).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Save & Exit", command=self.save_and_exit).grid(row=0, column=2, padx=5)

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.task_var.set("")
            self.update_listbox()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = True
            self.update_listbox()
        else:
            messagebox.showinfo("Select Task", "Please select a task to mark as done.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showinfo("Select Task", "Please select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✅" if task["done"] else "❌"
            self.listbox.insert(tk.END, f"{status} {task['task']}")

    def save_and_exit(self):
        with open(FILE_NAME, "w") as f:
            json.dump(self.tasks, f, indent=4)
        self.root.destroy()

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                self.tasks = json.load(f)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
