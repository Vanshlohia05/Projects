import tkinter as tk
from tkinter import simpledialog
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Habit:
    def __init__(self, name):
        self.name = name
        self.check_ins = []
        self.check_in_count = 0

    def check_in(self):
        self.check_ins.append(True)
        self.check_in_count += 1

class HabitTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Habit Tracker")

        self.create_habit_button = tk.Button(master, text="Create Habit", command=self.create_habit)
        self.create_habit_button.pack()

        self.habit_checkboxes = {}
        self.habits = {}

        self.check_in_button = tk.Button(master, text="Check In", command=self.check_in)
        self.check_in_button.pack()

        self.show_graph_button = tk.Button(master, text="Show Progress", command=self.show_graph)
        self.show_graph_button.pack()

        # Load habits from storage
        self.load_habits(retrieve_data())

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)  # Hook into the window close event

    def create_habit(self):
        habit_name = simpledialog.askstring("New Habit", "Enter habit name:", parent=self.master)
        if habit_name:
            new_habit = Habit(habit_name)
            self.habits[habit_name] = new_habit

            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.master, text=habit_name, variable=var)
            checkbox.pack()

            self.habit_checkboxes[habit_name] = (checkbox, var)

    def check_in(self):
        for habit_name, (checkbox, var) in self.habit_checkboxes.items():
            if var.get():
                habit = self.habits[habit_name]
                habit.check_in()
                print(f"Checked in for habit: {habit_name}, Total Check-ins: {habit.check_in_count}")

    def load_habits(self, habits_data):
        for habit_name, habit_info in habits_data.items():
            new_habit = Habit(habit_name)
            new_habit.__dict__.update(habit_info)
            self.habits[habit_name] = new_habit
            self.create_habit_checkbox(habit_name)

    def create_habit_checkbox(self, habit_name):
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(self.master, text=habit_name, variable=var)
        checkbox.pack()
        self.habit_checkboxes[habit_name] = (checkbox, var)

    def show_graph(self):
        habit_names = []
        check_in_counts = []

        for habit_name, habit in self.habits.items():
            habit_names.append(habit_name)
            check_in_counts.append(habit.check_in_count)

        # Plot the data
        if habit_names:
            plt.figure(figsize=(6, 4))
            plt.bar(habit_names, check_in_counts, color='skyblue')
            plt.xlabel('Habits')
            plt.ylabel('Check-ins')
            plt.title('Habit Progress')

            # Display the graph in the Tkinter window
            canvas = FigureCanvasTkAgg(plt.gcf(), master=self.master)
            canvas.draw()
            canvas.get_tk_widget().pack()

    def on_closing(self):
        # Save data before closing
        store_data(self.habits)
        self.master.destroy()

def store_data(habits):
    with open("habits.json", "w") as f:
        json.dump({name: habit.__dict__ for name, habit in habits.items()}, f)

def retrieve_data():
    try:
        with open("habits.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
    root = tk.Tk()
    app = HabitTrackerApp(root)
    root.mainloop()
