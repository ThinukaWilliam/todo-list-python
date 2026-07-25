import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager - Mini Project")
        self.root.geometry("400x450")

        # 1. DATA STRUCTURES
        self.tasks_list = []      # List to store task dictionaries 
        self.unique_tasks = set() # Set to prevent duplicates 
        self.headers = ("Task", "Status") # Tuple for fixed info 

        # 2. GUI COMPONENTS
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.label = tk.Label(self.frame, text="Enter Task:")
        self.label.pack(side=tk.LEFT)

        self.task_entry = tk.Entry(self.frame)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_btn = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_btn.pack(pady=5)

        self.tasks_display = tk.Listbox(self.root, width=50, height=10)
        self.tasks_display.pack(pady=10, padx=10)

        self.save_btn = tk.Button(self.root, text="Save & Exit", command=self.save_and_close)
        self.save_btn.pack(pady=5)

        # Load existing data on startup
        self.load_data()

    # FUNCTION 1: Add Task and Check
    def add_task(self):
        task_name = self.task_entry.get().strip()
        
        if not task_name:
            messagebox.showwarning("Input Error", "Task cannot be empty!")
            return

        if task_name in self.unique_tasks:
            messagebox.showwarning("Duplicate", "This task already exists!")
            return

        # Use Dictionary for structured data 
        task_data = {"name": task_name, "status": "Pending"}
        self.tasks_list.append(task_data)
        self.unique_tasks.add(task_name)
        
        self.update_listbox()
        self.task_entry.delete(0, tk.END)

    # FUNCTION 2: Update Display
    def update_listbox(self):
        self.tasks_display.delete(0, tk.END)
        for task in self.tasks_list:
            self.tasks_display.insert(tk.END, f"{task['name']} - [{task['status']}]")

    # FUNCTION 3: Load Data from File
    def load_data(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    name = line.strip()
                    if name:
                        self.tasks_list.append({"name": name, "status": "Pending"})
                        self.unique_tasks.add(name)
            self.update_listbox()
        except FileNotFoundError:
            pass # First time running, no file exists yet

    # FUNCTION 4: Save Data to File
    def save_data(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks_list:
                f.write(task['name'] + "\n")

    # FUNCTION 5: Exit Protocol
    def save_and_close(self):
        self.save_data()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
