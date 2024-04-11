from tkinter import *
import customtkinter as CTk
import platform
import json
import threading
import datetime

# Open the JSON file
with open("variables.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("thursday_programming_time" not in data):
    data = {
            "thursday_programming_time": 0,
            "friday_programming_time": 0,
            "saturday_programming_time": 0,
            "sunday_programming_time": 0,
            "monday_programming_time": 0,
            "tuesday_programming_time": 0,
            "wednesday_programming_time": 0,
            "total_programming_time": 0
            }

thursday_programming_time = data["thursday_programming_time"]
friday_programming_time = data["friday_programming_time"]
saturday_programming_time = data["saturday_programming_time"]
sunday_programming_time = data["sunday_programming_time"]
monday_programming_time = data["monday_programming_time"]
tuesday_programming_time = data["tuesday_programming_time"]
wednesday_programming_time = data["wednesday_programming_time"]
total_programming_time = data["total_programming_time"]

# Open the JSON file
with open("punches.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("thursday_punches" not in data):
    data = {
            "thursday_punches": ["None"],
            "friday_punches": ["None"],
            "saturday_punches": ["None"],
            "sunday_punches": ["None"],
            "monday_punches": ["None"],
            "tuesday_punches": ["None"],
            "wednesday_punches": ["None"],
            }

thursday_punches = data["thursday_punches"]
friday_punches = data["friday_punches"]
saturday_punches = data["saturday_punches"]
sunday_punches = data["sunday_punches"]
monday_punches = data["monday_punches"]
tuesday_punches = data["tuesday_punches"]
wednesday_punches = data["wednesday_punches"]

# Open the JSON file
with open("description.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("description" not in data):
    data = {
        "description": ""
    }

description = data["description"]

# Open the JSON file
with open("walking.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("thursday_walking_time" not in data):
    data = {
            "thursday_weight": 0,
            "friday_weight": 0,
            "saturday_weight": 0,
            "sunday_weight": 0,
            "monday_weight": 0,
            "tuesday_weight": 0,
            "wednesday_weight": 0,
            "total_weight_lost": 0,

            "thursday_walking_time": 0,
            "friday_walking_time": 0,
            "saturday_walking_time": 0,
            "sunday_walking_time": 0,
            "monday_walking_time": 0,
            "tuesday_walking_time": 0,
            "wednesday_walking_time": 0,
            "total_walking_time": 0,

            "thursday_walking_distance": 0,
            "friday_walking_distance": 0,
            "saturday_walking_distance": 0,
            "sunday_walking_distance": 0,
            "monday_walking_distance": 0,
            "tuesday_walking_distance": 0,
            "wednesday_walking_distance": 0,
            "total_walking_distance": 0,

            "thursday_walking_steps": 0,
            "friday_walking_steps": 0,
            "saturday_walking_steps": 0,
            "sunday_walking_steps": 0,
            "monday_walking_steps": 0,
            "tuesday_walking_steps": 0,
            "wednesday_walking_steps": 0,
            "total_walking_steps": 0,

            "thursday_calories": 0,
            "friday_calories": 0,
            "saturday_calories": 0,
            "sunday_calories": 0,
            "monday_calories": 0,
            "tuesday_calories": 0,
            "wednesday_calories": 0,
            "total_calories": 0
            }

thursday_weight = data["thursday_weight"]
friday_weight = data["friday_weight"]
saturday_weight = data["saturday_weight"]
sunday_weight = data["sunday_weight"]
monday_weight = data["monday_weight"]
tuesday_weight = data["tuesday_weight"]
wednesday_weight = data["wednesday_weight"]
total_weight_lost = data["total_weight_lost"]

thursday_walking_time = data["thursday_walking_time"]
friday_walking_time = data["friday_walking_time"]
saturday_walking_time = data["saturday_walking_time"]
sunday_walking_time = data["sunday_walking_time"]
monday_walking_time = data["monday_walking_time"]
tuesday_walking_time = data["tuesday_walking_time"]
wednesday_walking_time = data["wednesday_walking_time"]
total_walking_time = data["total_walking_time"]

thursday_walking_distance = data["thursday_walking_distance"]
friday_walking_distance = data["friday_walking_distance"]
saturday_walking_distance = data["saturday_walking_distance"]
sunday_walking_distance = data["sunday_walking_distance"]
monday_walking_distance = data["monday_walking_distance"]
tuesday_walking_distance = data["tuesday_walking_distance"]
wednesday_walking_distance = data["wednesday_walking_distance"]
total_walking_distance = data["total_walking_distance"]

thursday_walking_steps = data["thursday_walking_steps"]
friday_walking_steps = data["friday_walking_steps"]
saturday_walking_steps = data["saturday_walking_steps"]
sunday_walking_steps = data["sunday_walking_steps"]
monday_walking_steps = data["monday_walking_steps"]
tuesday_walking_steps = data["tuesday_walking_steps"]
wednesday_walking_steps = data["wednesday_walking_steps"]
total_walking_steps = data["total_walking_steps"]

thursday_calories = data["thursday_calories"]
friday_calories = data["friday_calories"]
saturday_calories = data["saturday_calories"]
sunday_calories = data["sunday_calories"]
monday_calories = data["monday_calories"]
tuesday_calories = data["tuesday_calories"]
wednesday_calories = data["wednesday_calories"]
total_calories = data["total_calories"]

def save_description(event):
    data = {
        "description": app.weekly_daily_tabs.weekly_tab.programming_frame.description_textbox.get("1.0", "end-1c")
        }
    write_description_to_file(data)
    global description
    description = data["description"]

def write_description_to_file(data):
    try:
        with open("description.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_description_to_file(data)

# Determine operating system being used
operating_system = ""
if (platform.system() == "Linux"):
    operating_system = "Linux"
else:
    operating_system = "Windows"

def center_window(window, window_width, window_height):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")

saturday_weight_as_float = 0
def validate_float(event):
    global saturday_weight_as_float
    global saturday_weight
    try:
        if (app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get() == ""):
            app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.delete(0, "end")
            app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.insert(0, "0")

        if (app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get().startswith("0") and not app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get().endswith(".")):
            app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.delete(0)

        saturday_weight_as_float = float(app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get())
        saturday_weight = saturday_weight_as_float
        data = {
        "thursday_weight": thursday_weight,
        "friday_weight": friday_weight,
        "saturday_weight": saturday_weight,
        "sunday_weight": sunday_weight,
        "monday_weight": monday_weight,
        "tuesday_weight": tuesday_weight,
        "wednesday_weight": wednesday_weight,
        "total_weight_lost": total_weight_lost,

        "thursday_walking_time": thursday_walking_time,
        "friday_walking_time": friday_walking_time,
        "saturday_walking_time": saturday_walking_time,
        "sunday_walking_time": sunday_walking_time,
        "monday_walking_time": monday_walking_time,
        "tuesday_walking_time": tuesday_walking_time,
        "wednesday_walking_time": wednesday_walking_time,
        "total_walking_time": total_walking_time,

        "thursday_walking_distance": thursday_walking_distance,
        "friday_walking_distance": friday_walking_distance,
        "saturday_walking_distance": saturday_walking_distance,
        "sunday_walking_distance": sunday_walking_distance,
        "monday_walking_distance": monday_walking_distance,
        "tuesday_walking_distance": tuesday_walking_distance,
        "wednesday_walking_distance": wednesday_walking_distance,
        "total_walking_distance": total_walking_distance,

        "thursday_walking_steps": thursday_walking_steps,
        "friday_walking_steps": friday_walking_steps,
        "saturday_walking_steps": saturday_walking_steps,
        "sunday_walking_steps": sunday_walking_steps,
        "monday_walking_steps": monday_walking_steps,
        "tuesday_walking_steps": tuesday_walking_steps,
        "wednesday_walking_steps": wednesday_walking_steps,
        "total_walking_steps": total_walking_steps,

        "thursday_calories": thursday_calories,
        "friday_calories": friday_calories,
        "saturday_calories": saturday_calories,
        "sunday_calories": sunday_calories,
        "monday_calories": monday_calories,
        "tuesday_calories": tuesday_calories,
        "wednesday_calories": wednesday_calories,
        "total_calories": total_calories
        }

        threading.Thread(target=write_walking_variables_to_file, args=(data,)).start()

    except ValueError:
        if (app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get() == ""):
            app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.delete(0, "end")
            app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.insert(0, "0")
            saturday_weight_as_float = float(app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.get())
            saturday_weight = saturday_weight_as_float
            data = {
            "thursday_weight": thursday_weight,
            "friday_weight": friday_weight,
            "saturday_weight": saturday_weight,
            "sunday_weight": sunday_weight,
            "monday_weight": monday_weight,
            "tuesday_weight": tuesday_weight,
            "wednesday_weight": wednesday_weight,
            "total_weight_lost": total_weight_lost,

            "thursday_walking_time": thursday_walking_time,
            "friday_walking_time": friday_walking_time,
            "saturday_walking_time": saturday_walking_time,
            "sunday_walking_time": sunday_walking_time,
            "monday_walking_time": monday_walking_time,
            "tuesday_walking_time": tuesday_walking_time,
            "wednesday_walking_time": wednesday_walking_time,
            "total_walking_time": total_walking_time,

            "thursday_walking_distance": thursday_walking_distance,
            "friday_walking_distance": friday_walking_distance,
            "saturday_walking_distance": saturday_walking_distance,
            "sunday_walking_distance": sunday_walking_distance,
            "monday_walking_distance": monday_walking_distance,
            "tuesday_walking_distance": tuesday_walking_distance,
            "wednesday_walking_distance": wednesday_walking_distance,
            "total_walking_distance": total_walking_distance,

            "thursday_walking_steps": thursday_walking_steps,
            "friday_walking_steps": friday_walking_steps,
            "saturday_walking_steps": saturday_walking_steps,
            "sunday_walking_steps": sunday_walking_steps,
            "monday_walking_steps": monday_walking_steps,
            "tuesday_walking_steps": tuesday_walking_steps,
            "wednesday_walking_steps": wednesday_walking_steps,
            "total_walking_steps": total_walking_steps,

            "thursday_calories": thursday_calories,
            "friday_calories": friday_calories,
            "saturday_calories": saturday_calories,
            "sunday_calories": sunday_calories,
            "monday_calories": monday_calories,
            "tuesday_calories": tuesday_calories,
            "wednesday_calories": wednesday_calories,
            "total_calories": total_calories
            }

            threading.Thread(target=write_walking_variables_to_file, args=(data,)).start()
        else:
            app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.delete(0, "end")
            app.weekly_daily_tabs.weekly_tab.exercise_frame.saturday_weight_entry.insert(0, str(saturday_weight))

def write_walking_variables_to_file(data):
    try:
        with open("walking.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_walking_variables_to_file(data)

class ProgrammingFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        # Title Label
        self.title = CTk.CTkLabel(self, text="Programming", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=4, sticky="ew")
        
        # Category Labels
        category_labels = ["Time Programming", "Time Punches", "Description of Weekly Work Completed"]
        category_labels_column_start = 1
        for i in range(3):
            label = CTk.CTkLabel(self, text=category_labels[i])
            label.grid(row=1, column=(i + category_labels_column_start))
        
        content_row_start = 2
        # Weekday Labels
        left_right_padding = 0
        if (operating_system == "Linux"):
            left_right_padding = 10
        else:
            left_right_padding = 12

        days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i in range(7):
            label = CTk.CTkLabel(self, text=days_of_the_week[i])
            label.grid(row=(i + content_row_start), column=0, padx=(left_right_padding, 5), sticky="w")
        
        # Weekday Hour Entries
        programming_times = [sunday_programming_time, monday_programming_time, tuesday_programming_time, wednesday_programming_time, thursday_programming_time, friday_programming_time, saturday_programming_time]
        self.programming_time_entries = []
        for i in range(7):
            entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
            entry.configure(state="disabled")
            entry.grid(row=(i + content_row_start), column=1, padx=(5, 5))

            if (programming_times[i] != 0):
                hours = programming_times[i] // 3600
                minutes = (programming_times[i] % 3600) // 60
                seconds = programming_times[i] % 60
                programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                entry.configure(state="normal")
                entry.insert(0, programming_time_string)
                entry.configure(state="disabled")

            self.programming_time_entries.append(entry)
        
        # Weekday Punches Option Menus
        daily_punches = [sunday_punches, monday_punches, tuesday_punches, wednesday_punches, thursday_punches, friday_punches, saturday_punches]
        self.daily_punches_option_menus = []
        for i in range(7):
            option_menu = CTk.CTkOptionMenu(self, values=daily_punches[i])
            option_menu.set("Punches")
            option_menu.grid(row=(i + content_row_start), column=2, padx=(5, 5), pady=(5,5))
            # Taking out selected_option causes this to break. It may be a bug with customtkinter
            option_menu.configure(command=lambda selected_option="Punches", option_menu=option_menu: self.reset_option_menu(option_menu, selected_option))
            self.daily_punches_option_menus.append(option_menu)

        # Description Text Box
        self.description_textbox = CTk.CTkTextbox(self, width=440, height=258, wrap="word")
        self.description_textbox.grid(row=2, column=3, rowspan=7, padx=(5, left_right_padding))
        # Calls function to save description to json on each key press.
        self.description_textbox.bind("<KeyRelease>", save_description)

        # If description hasn't been edited, display instructions, else display edited text.
        placeholder_string = "INSTRUCTIONS:\n\n- Edit the .env file in the dist folder to include any discord webhooks that you want to send data to.\n\n- Use the Start Button in the Daily Tracker Tab to clock in.\n\n- Once you clock in, you'll have the option to pause or resume your session.\n\n- End your session by clicking the End Button\n\n- When you aren't in a session, you'll have the ability to Send Weekly Data and Clear Weekly Data.\n\n- Sending weekly data sends your data to the discord by using webhooks. Your data will be automatically formatted to be readable and will show what dates the week covered.\n\n- Clearing Weekly Data will erase everything and set it all back to default. This will mostly be used when you want to start a new week. Be sure to send your data before doing this.\n\n- The Walking and Pomodoro switches are options that you can add to your session.\n\n- Walking assumes you are walking on a treadmill at 2mph and tracks your distance, steps, and calories burned. Calories burned are determined by the weight that you enter in the Weekly Log Exercising Tab. \n\n- Pomodoro pauses and gives a notification everytime the timer runs out. The timers go as follows: 25, 5, 25, 5, 25, 5, 25, 15\n\n- You'll only be able to type in this text box when you're not in a session. Erasing these instructions and typing a new message will save your new message."        
        if (description != ""):
            self.description_textbox.insert(1.0, description)
        else:
            self.description_textbox.insert(0.0, placeholder_string)

    # Sets Option Menus back to "Punches" after they've been changed. Taking out selected option causes this to break. It may be a bug with customtkinter.
    def reset_option_menu(self, option_menu, selected_option):
        option_menu.set("Punches")

class ExerciseFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        left_right_padding = 0
        if (operating_system == "Linux"):
            left_right_padding = 10
        else:
            left_right_padding = 12
        
        # Title Label
        self.title = CTk.CTkLabel(self, text="Exercising", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Category Labels
        category_labels = ["Weight", "Time Walked", "Distance", "Steps", "Calories Burned"]
        category_labels_column_start = 1
        for i in range(5):
            label = CTk.CTkLabel(self, text=category_labels[i])
            label.grid(row=1, column=(i + category_labels_column_start))
        
        # Weekday Labels
        content_row_start = 2
        days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i in range(7):
            label = CTk.CTkLabel(self, text=days_of_the_week[i])
            label.grid(row=(i + content_row_start), column=0, padx=(left_right_padding, 5), sticky="w")
        
        # Weight Entries
        day = (datetime.datetime.now().weekday() + 1) % 7
        daily_weights = [sunday_weight, monday_weight, tuesday_weight, wednesday_weight, thursday_weight, friday_weight, saturday_weight]
        for i in range(7):
            entry = CTk.CTkEntry(self, placeholder_text="Enter Weight", justify="center")
            entry.grid(row=(i + content_row_start), column=1, padx=(5, 5), pady=(5,5))
            entry.bind("<KeyRelease>", validate_float)

            if (daily_weights[i] != 0):
                weight_string = str(thursday_weight)
                entry.insert(0, weight_string)

            if (i == day):
                entry.configure(state="normal")
            else:
                entry.configure(placeholder_text="NONE")
                entry.configure(state="disabled")

        # Time Walked Entries
        self.thursday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.thursday_time_walked_entry.configure(state="disabled")
        self.thursday_time_walked_entry.grid(row=6, column=2, padx=(5, 5))

        if (thursday_walking_time != 0):
            hours = thursday_walking_time // 3600
            minutes = (thursday_walking_time % 3600) // 60
            seconds = thursday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.thursday_time_walked_entry.configure(state="normal")
            self.thursday_time_walked_entry.insert(0, walking_time_string)
            self.thursday_time_walked_entry.configure(state="disabled")

        self.friday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.friday_time_walked_entry.configure(state="disabled")
        self.friday_time_walked_entry.grid(row=7, column=2, padx=(5, 5))

        if (friday_walking_time != 0):
            hours = friday_walking_time // 3600
            minutes = (friday_walking_time % 3600) // 60
            seconds = friday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.friday_time_walked_entry.configure(state="normal")
            self.friday_time_walked_entry.insert(0, walking_time_string)
            self.friday_time_walked_entry.configure(state="disabled")

        self.saturday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.saturday_time_walked_entry.configure(state="disabled")
        self.saturday_time_walked_entry.grid(row=8, column=2, padx=(5, 5))

        if (saturday_walking_time != 0):
            hours = saturday_walking_time // 3600
            minutes = (saturday_walking_time % 3600) // 60
            seconds = saturday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.saturday_time_walked_entry.configure(state="normal")
            self.saturday_time_walked_entry.insert(0, walking_time_string)
            self.saturday_time_walked_entry.configure(state="disabled")

        self.sunday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.sunday_time_walked_entry.configure(state="disabled")
        self.sunday_time_walked_entry.grid(row=2, column=2, padx=(5, 5))

        if (sunday_walking_time != 0):
            hours = sunday_walking_time // 3600
            minutes = (sunday_walking_time % 3600) // 60
            seconds = sunday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.sunday_time_walked_entry.configure(state="normal")
            self.sunday_time_walked_entry.insert(0, walking_time_string)
            self.sunday_time_walked_entry.configure(state="disabled")

        self.monday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.monday_time_walked_entry.configure(state="disabled")
        self.monday_time_walked_entry.grid(row=3, column=2, padx=(5, 5))

        if (monday_walking_time != 0):
            hours = monday_walking_time // 3600
            minutes = (monday_walking_time % 3600) // 60
            seconds = monday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.monday_time_walked_entry.configure(state="normal")
            self.monday_time_walked_entry.insert(0, walking_time_string)
            self.monday_time_walked_entry.configure(state="disabled")

        self.tuesday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.tuesday_time_walked_entry.configure(state="disabled")
        self.tuesday_time_walked_entry.grid(row=4, column=2, padx=(5, 5))

        if (tuesday_walking_time != 0):
            hours = tuesday_walking_time // 3600
            minutes = (tuesday_walking_time % 3600) // 60
            seconds = tuesday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.tuesday_time_walked_entry.configure(state="normal")
            self.tuesday_time_walked_entry.insert(0, walking_time_string)
            self.tuesday_time_walked_entry.configure(state="disabled")

        self.wednesday_time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.wednesday_time_walked_entry.configure(state="disabled")
        self.wednesday_time_walked_entry.grid(row=5, column=2, padx=(5, 5))

        if (wednesday_walking_time != 0):
            hours = wednesday_walking_time // 3600
            minutes = (wednesday_walking_time % 3600) // 60
            seconds = wednesday_walking_time % 60
            walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
            self.wednesday_time_walked_entry.configure(state="normal")
            self.wednesday_time_walked_entry.insert(0, walking_time_string)
            self.wednesday_time_walked_entry.configure(state="disabled")

        # Distance Entries
        self.thursday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.thursday_distance_entry.configure(state="disabled")
        self.thursday_distance_entry.grid(row=6, column=3, padx=(5, 5))

        if (thursday_walking_distance != 0):
            walking_distance_string = str(thursday_walking_distance)
            self.thursday_distance_entry.configure(state="normal")
            self.thursday_distance_entry.insert(0, walking_distance_string)
            self.thursday_distance_entry.configure(state="disabled")

        self.friday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.friday_distance_entry.configure(state="disabled")
        self.friday_distance_entry.grid(row=7, column=3, padx=(5, 5))

        if (friday_walking_distance != 0):
            walking_distance_string = str(friday_walking_distance)
            self.friday_distance_entry.configure(state="normal")
            self.friday_distance_entry.insert(0, walking_distance_string)
            self.friday_distance_entry.configure(state="disabled")

        self.saturday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.saturday_distance_entry.configure(state="disabled")
        self.saturday_distance_entry.grid(row=8, column=3, padx=(5, 5))

        if (saturday_walking_distance != 0):
            walking_distance_string = str(saturday_walking_distance)
            self.saturday_distance_entry.configure(state="normal")
            self.saturday_distance_entry.insert(0, walking_distance_string)
            self.saturday_distance_entry.configure(state="disabled")

        self.sunday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.sunday_distance_entry.configure(state="disabled")
        self.sunday_distance_entry.grid(row=2, column=3, padx=(5, 5))

        if (sunday_walking_distance != 0):
            walking_distance_string = str(sunday_walking_distance)
            self.sunday_distance_entry.configure(state="normal")
            self.sunday_distance_entry.insert(0, walking_distance_string)
            self.sunday_distance_entry.configure(state="disabled")

        self.monday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.monday_distance_entry.configure(state="disabled")
        self.monday_distance_entry.grid(row=3, column=3, padx=(5, 5))

        if (monday_walking_distance != 0):
            walking_distance_string = str(monday_walking_distance)
            self.monday_distance_entry.configure(state="normal")
            self.monday_distance_entry.insert(0, walking_distance_string)
            self.monday_distance_entry.configure(state="disabled")

        self.tuesday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.tuesday_distance_entry.configure(state="disabled")
        self.tuesday_distance_entry.grid(row=4, column=3, padx=(5, 5))

        if (tuesday_walking_distance != 0):
            walking_distance_string = str(tuesday_walking_distance)
            self.tuesday_distance_entry.configure(state="normal")
            self.tuesday_distance_entry.insert(0, walking_distance_string)
            self.tuesday_distance_entry.configure(state="disabled")

        self.wednesday_distance_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.wednesday_distance_entry.configure(state="disabled")
        self.wednesday_distance_entry.grid(row=5, column=3, padx=(5, 5))

        if (wednesday_walking_distance != 0):
            walking_distance_string = str(wednesday_walking_distance)
            self.wednesday_distance_entry.configure(state="normal")
            self.wednesday_distance_entry.insert(0, walking_distance_string)
            self.wednesday_distance_entry.configure(state="disabled")

        #Steps Entries
        self.thursday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.thursday_steps_entry.configure(state="disabled")
        self.thursday_steps_entry.grid(row=6, column=4, padx=(5, 5))

        if (thursday_walking_steps != 0):
            walking_steps_string = str(thursday_walking_steps)
            self.thursday_steps_entry.configure(state="normal")
            self.thursday_steps_entry.insert(0, walking_steps_string)
            self.thursday_steps_entry.configure(state="disabled")

        self.friday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.friday_steps_entry.configure(state="disabled")
        self.friday_steps_entry.grid(row=7, column=4, padx=(5, 5))

        if (friday_walking_steps != 0):
            walking_steps_string = str(friday_walking_steps)
            self.friday_steps_entry.configure(state="normal")
            self.friday_steps_entry.insert(0, walking_steps_string)
            self.friday_steps_entry.configure(state="disabled")

        self.saturday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.saturday_steps_entry.configure(state="disabled")
        self.saturday_steps_entry.grid(row=8, column=4, padx=(5, 5))

        if (saturday_walking_steps != 0):
            walking_steps_string = str(saturday_walking_steps)
            self.saturday_steps_entry.configure(state="normal")
            self.saturday_steps_entry.insert(0, walking_steps_string)
            self.saturday_steps_entry.configure(state="disabled")

        self.sunday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.sunday_steps_entry.configure(state="disabled")
        self.sunday_steps_entry.grid(row=2, column=4, padx=(5, 5))

        if (sunday_walking_steps != 0):
            walking_steps_string = str(sunday_walking_steps)
            self.sunday_steps_entry.configure(state="normal")
            self.sunday_steps_entry.insert(0, walking_steps_string)
            self.sunday_steps_entry.configure(state="disabled")

        self.monday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.monday_steps_entry.configure(state="disabled")
        self.monday_steps_entry.grid(row=3, column=4, padx=(5, 5))

        if (monday_walking_steps != 0):
            walking_steps_string = str(monday_walking_steps)
            self.monday_steps_entry.configure(state="normal")
            self.monday_steps_entry.insert(0, walking_steps_string)
            self.monday_steps_entry.configure(state="disabled")

        self.tuesday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.tuesday_steps_entry.configure(state="disabled")
        self.tuesday_steps_entry.grid(row=4, column=4, padx=(5, 5))

        if (tuesday_walking_steps != 0):
            walking_steps_string = str(tuesday_walking_steps)
            self.tuesday_steps_entry.configure(state="normal")
            self.tuesday_steps_entry.insert(0, walking_steps_string)
            self.tuesday_steps_entry.configure(state="disabled")

        self.wednesday_steps_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.wednesday_steps_entry.configure(state="disabled")
        self.wednesday_steps_entry.grid(row=5, column=4, padx=(5, 5))

        if (wednesday_walking_steps != 0):
            walking_steps_string = str(wednesday_walking_steps)
            self.wednesday_steps_entry.configure(state="normal")
            self.wednesday_steps_entry.insert(0, walking_steps_string)
            self.wednesday_steps_entry.configure(state="disabled")

        #Colories Entries
        self.thursday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.thursday_calories_entry.configure(state="disabled")
        self.thursday_calories_entry.grid(row=6, column=5, padx=(5, left_right_padding))

        if (thursday_calories != 0):
            walking_calories_string = str(thursday_calories)
            self.thursday_calories_entry.configure(state="normal")
            self.thursday_calories_entry.insert(0, walking_calories_string)
            self.thursday_calories_entry.configure(state="disabled")

        self.friday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.friday_calories_entry.configure(state="disabled")
        self.friday_calories_entry.grid(row=7, column=5, padx=(5, left_right_padding))

        if (friday_calories != 0):
            walking_calories_string = str(friday_calories)
            self.friday_calories_entry.configure(state="normal")
            self.friday_calories_entry.insert(0, walking_calories_string)
            self.friday_calories_entry.configure(state="disabled")

        self.saturday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.saturday_calories_entry.configure(state="disabled")
        self.saturday_calories_entry.grid(row=8, column=5, padx=(5, left_right_padding))

        if (saturday_calories != 0):
            walking_calories_string = str(saturday_calories)
            self.saturday_calories_entry.configure(state="normal")
            self.saturday_calories_entry.insert(0, walking_calories_string)
            self.saturday_calories_entry.configure(state="disabled")

        self.sunday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.sunday_calories_entry.configure(state="disabled")
        self.sunday_calories_entry.grid(row=2, column=5, padx=(5, left_right_padding))

        if (sunday_calories != 0):
            walking_calories_string = str(sunday_calories)
            self.sunday_calories_entry.configure(state="normal")
            self.sunday_calories_entry.insert(0, walking_calories_string)
            self.sunday_calories_entry.configure(state="disabled")

        self.monday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.monday_calories_entry.configure(state="disabled")
        self.monday_calories_entry.grid(row=3, column=5, padx=(5, left_right_padding))

        if (monday_calories != 0):
            walking_calories_string = str(monday_calories)
            self.monday_calories_entry.configure(state="normal")
            self.monday_calories_entry.insert(0, walking_calories_string)
            self.monday_calories_entry.configure(state="disabled")

        self.tuesday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.tuesday_calories_entry.configure(state="disabled")
        self.tuesday_calories_entry.grid(row=4, column=5, padx=(5, left_right_padding))

        if (tuesday_calories != 0):
            walking_calories_string = str(tuesday_calories)
            self.tuesday_calories_entry.configure(state="normal")
            self.tuesday_calories_entry.insert(0, walking_calories_string)
            self.tuesday_calories_entry.configure(state="disabled")

        self.wednesday_calories_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.wednesday_calories_entry.configure(state="disabled")
        self.wednesday_calories_entry.grid(row=5, column=5, padx=(5, left_right_padding))

        if (wednesday_calories != 0):
            walking_calories_string = str(wednesday_calories)
            self.wednesday_calories_entry.configure(state="normal")
            self.wednesday_calories_entry.insert(0, walking_calories_string)
            self.wednesday_calories_entry.configure(state="disabled")

class WeeklyLogTabs(CTk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Programming")
        self.add("Exercising")

        # Add Frames to tabs
        self.programming_frame = ProgrammingFrame(self.tab("Programming"))
        self.programming_frame.grid(row=0, column=0, pady=(10, 0))
        
        self.exercise_frame = ExerciseFrame(self.tab("Exercising"))
        self.exercise_frame.grid(row=1, column=0, pady=(10, 0))

class WeeklyDailyTabs(CTk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Weekly Log")
        self.add("Daily Tracker")

        # Add Frames to tabs
        self.weekly_tab = WeeklyLogTabs(self.tab("Weekly Log"), fg_color="transparent")
        self.weekly_tab.grid(row=0, column=0, padx=20)

        # self.daily_tab = DailyFrame(self.tab("Daily Tracker"))
        # self.daily_tab.grid(row=0, column=0, pady=(53,5))

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        # region Window Settings
        self.title("Productivity Tracker")

        # Use different method to set icon based on operating system
        if (operating_system == "Linux"):
            self.iconphoto(False, PhotoImage(file='icon4-2.png'))
        else:
            self.iconbitmap("icon4.ico")
        
        # Define Window Size and Behavior
        window_width = 920
        window_height = 635
        self.geometry(f"{window_width}x{window_height}")
        center_window(self, window_width, window_height)
        self.grid_columnconfigure(0, weight=1)
        #endregion 

        # Add Content for weekly and daily tabs
        self.weekly_daily_tabs = WeeklyDailyTabs(self, fg_color="transparent")
        self.weekly_daily_tabs.grid(row=0, column=0)

        # # Add Content for weekly totals
        # self.totals_frame = TotalsFrame(self)
        # self.totals_frame.grid(row=1, column=0, padx=10)

        # #Add Buttons
        # self.buttons_frame = ButtonsFrame(self)
        # self.buttons_frame.grid(row=2, column=0)

app = App()
app.mainloop()