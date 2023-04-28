import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Daily Tasks")

# Create a label
label = tk.Label(window, text="Enter your daily tasks:")
label.pack()

# Create a text input field
task_entry = tk.Entry(window)
task_entry.pack()

# Create a listbox to display tasks
task_listbox = tk.Listbox(window)
task_listbox.pack()

# Create a counter to keep track of completed tasks
completed_counter = 0

# Function to add task to the listbox
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, "- " + task)
        task_entry.delete(0, tk.END)

# Create a button to add task
add_button = tk.Button(window, text="Add task", command=add_task)
add_button.pack()

# Function to delete selected task from the listbox
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_text = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)
        # If the task was completed, decrement the counter
        if task_text.startswith("✓ "):
            global completed_counter
            completed_counter -= 1

# Create a button to delete task
delete_button = tk.Button(window, text="Delete task", command=delete_task)
delete_button.pack()

# Function to mark selected task as completed
def complete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_text = task_listbox.get(selected_task)
        # If the task was not completed, mark it as completed and increment the counter
        if not task_text.startswith("✓ "):
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, "✓ " + task_text[2:])
            task_listbox.itemconfig(selected_task, bg="light green")
            global completed_counter
            completed_counter += 1

def progress_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_text = task_listbox.get(selected_task)
        # If the task was not completed, mark it as completed and increment the counter
        if not task_text.startswith("? "):
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, "? " + task_text[2:])
            task_listbox.itemconfig(selected_task, bg="light yellow")

def late_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_text = task_listbox.get(selected_task)
        # If the task was not completed, mark it as completed and increment the counter
        if not task_text.startswith("X "):
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, "X " + task_text[2:])
            task_listbox.itemconfig(selected_task, bg="red")

# Create a button to mark task as completed
complete_button = tk.Button(window, text="Mark as completed", command=complete_task)
complete_button.pack()

progress_button = tk.Button(window, text="Mark as in progress", command=progress_task)
progress_button.pack()

late_button = tk.Button(window, text="Mark as late", command=late_task)
late_button.pack()


# Function to undo the last action (completion or deletion) on the selected task
def undo_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_text = task_listbox.get(selected_task)
        if task_text.startswith("✓ "):
            # If the task was completed, mark it as uncompleted and decrement the counter
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, "- " + task_text[2:])
            global completed_counter
            completed_counter -= 1
        else:
            # If the task was not completed, undelete it
            task_listbox.insert(selected_task, task_text)

# Create a button to undo task completion or deletion
undo_button = tk.Button(window, text="Undo", command=undo_task)
undo_button.pack()


# Run the window
window.mainloop()
