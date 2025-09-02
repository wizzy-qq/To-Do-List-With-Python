import tkinter as tk
from tkinter import messagebox
import random
import time
import threading

# ---------- Data ----------
quotes = [
    "💡 Every great achievement starts with a small step!",
    "🌟 Today is the best day to start something!",
    "🚀 Small steps make a big difference!"
]

tedx_news = [
    "🎤 TEDx: Future of Technology and Life",
    "🎤 TEDx: The Power of Creativity",
    "🎤 TEDx: Success and Motivation",
    "🎤 TEDx: Creativity in Education",
    "🎤 TEDx: Future of Business",
    "🎤 TEDx: Power of Art",
    "🎤 TEDx: Science and Life",
    "🎤 TEDx: Psychology and Motivation",
    "🎤 TEDx: Social Media and Society",
    "🎤 TEDx: Sustainability and Future"
]

important_news = [
    "⚡ WHO released a new health guideline.",
    "⚡ Water traces found on Mars!",
    "⚡ AI-based education system tested."
]

tasks = []

# ---------- Add/Delete Task ----------
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        idx = listbox.curselection()[0]
        tasks.pop(idx)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task_list():
    listbox.delete(0, tk.END)
    if not tasks:
        listbox.insert(tk.END, "🌟 Add a task and be productive! 🌟")
    else:
        for i, task in enumerate(tasks, 1):
            listbox.insert(tk.END, f"{i}. {task}")

# ---------- Pomodoro Timer ----------
def start_pomodoro():
    try:
        t = int(pomodoro_entry.get()) * 60
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number!")
        return

    def countdown(t):
        while t > 0:
            mins, secs = divmod(t, 60)
            timer_label.config(text=f"{mins:02d}:{secs:02d}")
            root.update()
            time.sleep(1)
            t -= 1
        messagebox.showinfo("Pomodoro", "Focus time ended! Take a 5-minute break.")
        timer_label.config(text=f"{pomodoro_entry.get()}:00")
    
    threading.Thread(target=countdown, args=(t,), daemon=True).start()

# ---------- Background Animation ----------
bg_colors = ["#6A5ACD", "#8A2BE2", "#7B68EE", "#9370DB"]
color_index = 0
def animate_bg():
    global color_index
    root.configure(bg=bg_colors[color_index])
    login_frame.configure(bg=bg_colors[color_index])
    main_frame.configure(bg=bg_colors[color_index])
    color_index = (color_index + 1) % len(bg_colors)
    root.after(3000, animate_bg)

# ---------- Main App ----------
def main_app(username, purpose):
    login_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

    # Header
    welcome_label = tk.Label(main_frame, text=f"Welcome {username}! 🌈\nPurpose: {purpose}", 
                             fg="white", bg=main_frame["bg"], font=("Comic Sans MS", 24, "bold"), justify="center")
    welcome_label.pack(pady=20)
    
    quote_label = tk.Label(main_frame, text=random.choice(quotes), fg="#FFD700", bg=main_frame["bg"], font=("Comic Sans MS", 18, "italic"))
    quote_label.pack(pady=10)
    
    frame = tk.Frame(main_frame, bg=main_frame["bg"])
    frame.pack(pady=10, fill="both", expand=True)
    
    # Left: Tasks
    global task_entry, listbox
    left_frame = tk.Frame(frame, bg=main_frame["bg"])
    left_frame.pack(side="left", padx=20, fill="y")
    
    task_entry = tk.Entry(left_frame, width=30, font=("Comic Sans MS", 16))
    task_entry.pack(pady=5)
    
    add_button = tk.Button(left_frame, text="➕ Add Task", width=20, bg="#FFD966", fg="#2E4057", font=("Comic Sans MS", 14), command=add_task)
    add_button.pack(pady=3)
    
    delete_button = tk.Button(left_frame, text="🗑 Delete Task", width=20, bg="#FF6F61", fg="white", font=("Comic Sans MS", 14), command=delete_task)
    delete_button.pack(pady=3)
    
    listbox = tk.Listbox(left_frame, width=50, height=20, bg="#EEE8AA", fg="#2E4057", selectbackground="#FFB347", font=("Comic Sans MS", 14))
    listbox.pack(pady=10)
    update_task_list()
    
    # Right: TEDx News & Pomodoro
    right_frame = tk.Frame(frame, bg=main_frame["bg"])
    right_frame.pack(side="right", padx=20, fill="both", expand=True)
    
    news_label = tk.Label(right_frame, text="🎤 TEDx News", fg="#FF4500", bg=main_frame["bg"], font=("Comic Sans MS", 20, "bold"))
    news_label.pack(pady=5)
    
    news_list = tk.Listbox(right_frame, width=60, height=15, bg="#E6E6FA", fg="#2E4057", font=("Comic Sans MS", 16))
    news_list.pack(pady=10)
    for news in tedx_news:
        news_list.insert(tk.END, news)
    
    # Pomodoro settings
    global pomodoro_entry, timer_label
    tk.Label(right_frame, text="Pomodoro duration (minutes):", bg=main_frame["bg"], fg="white", font=("Comic Sans MS", 16)).pack(pady=5)
    pomodoro_entry = tk.Entry(right_frame, width=10, font=("Comic Sans MS", 16))
    pomodoro_entry.insert(0, "25")  # default 25 min
    pomodoro_entry.pack(pady=5)
    
    timer_label = tk.Label(right_frame, text=f"{pomodoro_entry.get()}:00", fg="white", bg=main_frame["bg"], font=("Comic Sans MS", 24))
    timer_label.pack(pady=10)
    
    pomodoro_button = tk.Button(right_frame, text="⏱ Start Pomodoro", bg="#8BC34A", fg="white", font=("Comic Sans MS", 16), command=start_pomodoro)
    pomodoro_button.pack(pady=5)

# ---------- Login Screen ----------
def start_app():
    username = username_entry.get()
    purpose = purpose_var.get()
    if not username or purpose == "Select":
        messagebox.showwarning("Warning", "Please enter username and purpose!")
        return
    login_frame.pack_forget()
    main_app(username, purpose)
    animate_bg()

root = tk.Tk()
root.title("Fun & Colorful To-Do App")
root.state('zoomed')  # fullscreen
root.configure(bg="#6A5ACD")

login_frame = tk.Frame(root, bg=root["bg"])
login_frame.pack(pady=20, fill="both", expand=True)

main_frame = tk.Frame(root, bg=root["bg"])

# Username
tk.Label(login_frame, text="Username:", fg="white", bg=root["bg"], font=("Comic Sans MS", 18)).pack(pady=10)
username_entry = tk.Entry(login_frame, width=30, font=("Comic Sans MS", 16))
username_entry.pack(pady=5)

# Purpose
tk.Label(login_frame, text="What will you use it for?", fg="white", bg=root["bg"], font=("Comic Sans MS", 18)).pack(pady=10)
purpose_var = tk.StringVar(value="Select")
purpose_menu = tk.OptionMenu(login_frame, purpose_var, "Learning", "Planning", "Projects", "Motivation")
purpose_menu.config(width=20, bg="#FFD966", fg="#2E4057", font=("Comic Sans MS", 14))
purpose_menu.pack(pady=5)

# Important news
tk.Label(login_frame, text="⚡ Important News:", fg="#FF4500", bg=root["bg"], font=("Comic Sans MS", 18, "bold")).pack(pady=10)
news_listbox = tk.Listbox(login_frame, width=100, height=5, bg="#E6E6FA", fg="#2E4057", font=("Comic Sans MS", 14))
news_listbox.pack(pady=5)
for news in important_news:
    news_listbox.insert(tk.END, news)

# Start button
start_button = tk.Button(login_frame, text="🚀 Start", width=20, bg="#8BC34A", fg="white", font=("Comic Sans MS", 16), command=start_app)
start_button.pack(pady=20)

root.mainloop()
