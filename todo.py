import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(self.master, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_frame = tk.Frame(self.master)
        self.tasks_frame.pack(pady=20)

        self.display_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self, task_index):
        del self.tasks[task_index]
        self.display_tasks()

    def display_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.tasks, start=1):
            task_label = tk.Label(self.tasks_frame, text=f"{index}. {task}")
            task_label.grid(row=index - 1, column=0, sticky="w")

            remove_button = tk.Button(self.tasks_frame, text="Remove", command=lambda idx=index-1: self.remove_task(idx))
            remove_button.grid(row=index - 1, column=1)

def main():
    root = tk.Tk()
    todo_app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
