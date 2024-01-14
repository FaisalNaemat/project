import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Create and set up GUI elements
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)

        save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        save_button.pack(pady=5)

        load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        load_button.pack(pady=5)

        # Load tasks from file on startup
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        try:
            with open("tasks.txt", "w") as file:
                for task in tasks:
                    file.write(task + "\n")
            messagebox.showinfo("Success", "Tasks save successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving tasks: {str(e)}")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = [line.strip() for line in file.readlines()]
            self.task_listbox.delete(0, tk.END)
            for task in tasks:
                self.task_listbox.insert(tk.END, task)
            messagebox.showinfo("Success", "Tasks loaded successfully.")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No saved tasks found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading tasks: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()