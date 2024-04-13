from tkinter import *
import customtkinter as CTk
import time
import datetime
import json
from plyer import notification
import threading
import os
import csv
import discord
from dotenv import load_dotenv
import platform

operating_system = ""

tracking = False
pomodoro_break = False
readytostart = True
paused = False
p_string_store = ""
focus_time = 1500
break_time = 300
long_break_time = 900
p_focus_time = 1500
p_break_time = 300
p_long_break_time = 900
p_cycle_count = 1
start_time = 0
time_passed = 0
timer_id = ""
curr_week_str = ""

# region handle loading variables from JSON files
file_path = "variables.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

file_path = "punches.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

file_path = "walking.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

file_path = "description.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

file_path = "must_clear.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

file_path = ".env"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(".env", "w", newline='') as file:
        file.write("GeorgeCGeneral='None'\n")
        file.write("GeorgeCMisc='None'\n")
        file.write("Programming_Webhooks='None'\n")
        file.write("Exercise_Webhooks='None'\n")

file_path = "current_week.json"
# Check if the file exists
if not os.path.isfile(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

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
with open("must_clear.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("must_clear" not in data):
    data = {
        "must_clear": False,
        "current_week": -1
    }

must_clear = data["must_clear"]
current_week = data["current_week"]

# Open the JSON file
with open("current_week.json", "r") as file:
    # Load the JSON data
    data = json.load(file)

if ("current_week_str" not in data):
    data = {
        "curr_week_str": ""
    }

curr_week_str = data["curr_week_str"]
#endregion

daily_programming_times = [sunday_programming_time, monday_programming_time, tuesday_programming_time, wednesday_programming_time, thursday_programming_time, friday_programming_time, saturday_programming_time]
daily_punches = [sunday_punches, monday_punches, tuesday_punches, wednesday_punches, thursday_punches, friday_punches, saturday_punches]
daily_weights = [sunday_weight, monday_weight, tuesday_weight, wednesday_weight, thursday_weight, friday_weight, saturday_weight]
daily_walking_times = [sunday_walking_time, monday_walking_time, tuesday_walking_time, wednesday_walking_time, thursday_walking_time, friday_walking_time, saturday_walking_time]
daily_distances = [sunday_walking_distance, monday_walking_distance, tuesday_walking_distance, wednesday_walking_distance, thursday_walking_distance, friday_walking_distance, saturday_walking_distance]
daily_steps = [sunday_walking_steps, monday_walking_steps, tuesday_walking_steps, wednesday_walking_steps, thursday_walking_steps, friday_walking_steps, saturday_walking_steps]
daily_calories = [sunday_calories, monday_calories, tuesday_calories, wednesday_calories, thursday_calories, friday_calories, saturday_calories]

can_clear = True

must_clear = False

def send_data_modal():
    pass
def clear_data_modal():
    pass
def new_week_modal():
    pass
def walking():
    pass
def update_walking_stats():
    pass

def update_global_daily_lists():
    global daily_programming_times
    global daily_punches
    global daily_weights
    global daily_walking_times
    global daily_distances
    global daily_steps
    global daily_calories

    daily_programming_times = [sunday_programming_time, monday_programming_time, tuesday_programming_time, wednesday_programming_time, thursday_programming_time, friday_programming_time, saturday_programming_time]
    daily_punches = [sunday_punches, monday_punches, tuesday_punches, wednesday_punches, thursday_punches, friday_punches, saturday_punches]
    daily_weights = [sunday_weight, monday_weight, tuesday_weight, wednesday_weight, thursday_weight, friday_weight, saturday_weight]
    daily_walking_times = [sunday_walking_time, monday_walking_time, tuesday_walking_time, wednesday_walking_time, thursday_walking_time, friday_walking_time, saturday_walking_time]
    daily_distances = [sunday_walking_distance, monday_walking_distance, tuesday_walking_distance, wednesday_walking_distance, thursday_walking_distance, friday_walking_distance, saturday_walking_distance]
    daily_steps = [sunday_walking_steps, monday_walking_steps, tuesday_walking_steps, wednesday_walking_steps, thursday_walking_steps, friday_walking_steps, saturday_walking_steps]
    daily_calories = [sunday_calories, monday_calories, tuesday_calories, wednesday_calories, thursday_calories, friday_calories, saturday_calories]

def pause_resume():
    global paused
    global tracking
    global timer_id

    # pause resume switch
    if (not paused):
        paused = True
        tracking = False
        app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(text="Resume")
        app.after_cancel(timer_id)
    else:
        paused = False
        tracking = True
        app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(text="Pause")
        app.after_cancel(timer_id)
        update_time(True)

def create_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Productivity Tracker",
        app_icon="icon4.ico",
        timeout=10
    )
    app.attributes("-topmost", True)
    app.attributes("-topmost", False)

def format_pomodoro_time_label(p_time):
    hours = p_time // 3600
    minutes = (p_time % 3600) // 60
    seconds = p_time % 60
    p_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text=p_string)

def pomodoro():
    global pomodoro_break
    global p_focus_time
    global p_long_break_time
    global p_break_time
    global p_cycle_count
    global focus_time
    global break_time
    global long_break_time

    # Determine pomodoro state. Subtract time depending on state
    if (not pomodoro_break):
        # 25 min
        p_focus_time = p_focus_time - 1
        format_pomodoro_time_label(p_focus_time) 
    elif (pomodoro_break and p_cycle_count % 4 == 0):
        # 15 min
        p_long_break_time = p_long_break_time - 1
        format_pomodoro_time_label(p_long_break_time)
    else:
        # 5 min
        p_break_time = p_break_time - 1
        format_pomodoro_time_label(p_break_time)
        
    # Handle pomodoro state end (time reaches 00:00:00)
    if (app.weekly_daily_tabs.daily_tab.pomodoro_time_label._text == "00:00:00"):
        # Swap break state and increment cycle count if break
        if (pomodoro_break):
            p_cycle_count = p_cycle_count + 1
            app.weekly_daily_tabs.daily_tab.pomodoro_count_label.configure(text="#" + str(p_cycle_count))
            app.weekly_daily_tabs.daily_tab.pomodoro_focus_label.configure(text="Focus")
            pomodoro_break = False
        else:
            app.weekly_daily_tabs.daily_tab.pomodoro_focus_label.configure(text="Break")
            pomodoro_break = True
        
        # Reset Pomodoro vars
        p_break_time = break_time
        p_focus_time = focus_time
        p_long_break_time = long_break_time

        # Pause and reset label
        pause_resume()

        # Determine pomodoro state and create notification
        if (app.weekly_daily_tabs.daily_tab.pomodoro_switch.get() == 1):
            if (not pomodoro_break):
                # 25 min
                create_notification("Focus", "Focus for 25 minutes.")
                format_pomodoro_time_label(p_focus_time)
            elif (pomodoro_break and p_cycle_count % 4 == 0):
                # 15 min
                create_notification("Long Break", "Break for 15 minutes.")
                format_pomodoro_time_label(p_long_break_time)
            else:
                # 5 min
                create_notification("Short Break", "Break for 5 minutes.")
                format_pomodoro_time_label(p_break_time)

def handle_being_clocked_in_past_saturday_midnight():
    global current_week
    global can_clear
    global readytostart
    global paused
    global p_focus_time
    global p_break_time
    global p_long_break_time
    global focus_time
    global break_time
    global long_break_time
    global p_cycle_count
    global tracking

    # Test to see if current week is equal to the week we get now, if not then user must delete data
    week_num = datetime.datetime.now().strftime("%U %Y")
    if (current_week != week_num):
        can_clear = True
        
        # Reset UI and disable clock in
        app.buttons_frame.send_weekly_data_button.configure(state="normal")
        app.buttons_frame.clear_weekly_data_button.configure(state="normal")
        app.weekly_daily_tabs.weekly_tab.programming_frame.description_textbox.configure(state="normal")
        app.weekly_daily_tabs.daily_tab.start_end_button.configure(text="Start")
        app.weekly_daily_tabs.daily_tab.start_end_button.configure(state="disabled")
        app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(state="disabled")
        app.weekly_daily_tabs.daily_tab.total_time_label.configure(text="00:00:00")
        app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text="00:25:00")
        app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(text="Pause")
        app.weekly_daily_tabs.daily_tab.pomodoro_count_label.configure(text="#1")
        app.weekly_daily_tabs.daily_tab.pomodoro_focus_label.configure(text="Focus")
        
        # Reset Vars
        readytostart = True
        paused = False
        p_focus_time = focus_time
        p_break_time = break_time
        p_long_break_time = long_break_time
        p_cycle_count = 1

        # Spoof Punchout on Saturday 11:59:59 PM 
        saturday_punches.append("End: 11:59:59 PM")
        if (saturday_punches[0] == "None"):
            saturday_punches.pop(0)
        app.weekly_daily_tabs.weekly_tab.programming_frame.daily_punches_option_menus[6].configure(values=saturday_punches)

        update_global_daily_lists()

        # Save data to file
        data = {
        "thursday_punches": thursday_punches,
        "friday_punches": friday_punches,
        "saturday_punches": saturday_punches,
        "sunday_punches": sunday_punches,
        "monday_punches": monday_punches,
        "tuesday_punches": tuesday_punches,
        "wednesday_punches": wednesday_punches,
        }

        threading.Thread(target=write_punches_to_file, args=(data,)).start()

        create_notification("You've been clocked out!", "You've been clocked out due to being clocked in during a new week without clearing first.")

        new_week_modal()

        # Save must_clear as true so the user will have to clear before they clock in again
        must_clear = True

        data = {
            "must_clear": must_clear,
            "current_week": current_week
        }

        threading.Thread(target=write_must_clear_to_file, args=(data,)).start()

        # Break out of time tracker
        tracking = False
        app.after_cancel(timer_id)

def format_entry_time(entry, time):
        hours = time // 3600
        minutes = (time % 3600) // 60
        seconds = time % 60
        programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        entry.configure(state="normal")
        entry.delete(0, "end")
        entry.insert(0, programming_time_string)
        entry.configure(state="disabled")

def update_time(firstpass):
    global current_week
    global tracking
    global total_programming_time
    global timer_id
    global daily_programming_times

    # Save current_week if it hasn't been set yet, else see if user is clocked in past saturday at midnight
    if (current_week == -1):
        current_week = datetime.datetime.now().strftime("%U %Y")
        data = {
            "must_clear": must_clear,
            "current_week": current_week
        }
        threading.Thread(target=write_must_clear_to_file, args=(data,)).start()
    else:
        handle_being_clocked_in_past_saturday_midnight()

    if (tracking):
        # Allows for 1 second buffer
        if (firstpass):
            firstpass = False
        else:
            # Add time to total time
            label_text = app.weekly_daily_tabs.daily_tab.total_time_label._text
            hours, minutes, seconds = map(int, label_text.split(":"))
            label_value = hours * 3600 + minutes * 60 + seconds
            label_value = label_value + 1
            hours = int(label_value // 3600)
            minutes = int((label_value % 3600) // 60)
            seconds = int(label_value % 60)
            time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            app.weekly_daily_tabs.daily_tab.total_time_label.configure(text=time_string)
            
            # Call functions that handle selected options
            if (app.weekly_daily_tabs.daily_tab.pomodoro_switch.get() == 1):
                pomodoro()
            walking()
            update_walking_stats()
            
            # Use local day_as_number in case of day change while program running
            day_as_number = (datetime.datetime.now().weekday() + 1) % 7
            programming_time_entries = app.weekly_daily_tabs.weekly_tab.programming_frame.programming_time_entries
            for i in range(7):
                # Add time to current day
                if (day_as_number == i):
                    daily_programming_times[i] = daily_programming_times[i] + 1
                    format_entry_time(programming_time_entries[i], daily_programming_times[i])
                    
            update_global_daily_lists()

            # Calculate total programming time
            for i in range(7):
                total_programming_time = total_programming_time + daily_programming_times[i]
            
            format_entry_time(app.totals_frame.time_programming_entry, total_programming_time)

            # Write programming times to file
            data = {
                "thursday_programming_time": thursday_programming_time,
                "friday_programming_time": friday_programming_time,
                "saturday_programming_time": saturday_programming_time,
                "sunday_programming_time": sunday_programming_time,
                "monday_programming_time": monday_programming_time,
                "tuesday_programming_time": tuesday_programming_time,
                "wednesday_programming_time": wednesday_programming_time,
                "total_programming_time": total_programming_time,
            }

            threading.Thread(target=write_variables_to_file, args=(data,)).start()

        # Recursively call update_time every second. Save timer in timer_id
        timer_id = app.after(1000, update_time, False)

def write_variables_to_file(data):
    try:
        with open("variables.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_variables_to_file(data)

def write_walking_variables_to_file(data):
    try:
        with open("walking.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_walking_variables_to_file(data)

def write_punches_to_file(data):
    try:
        with open("punches.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_punches_to_file(data)

def write_description_to_file(data):
    try:
        with open("description.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_description_to_file(data)

def write_must_clear_to_file(data):
    try:
        with open("must_clear.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_must_clear_to_file(data)

def write_current_week_to_file(data):
    try:
        with open("current_week.json", "w") as file:
            json.dump(data, file)
    except Exception as e:
        write_current_week_to_file(data)

def get_date_range_for_current_week():
    """
    Returns the date range for the current week in the format 'MMM d(st/nd/rd/th) yyyy - MMM d(st/nd/rd/th) yyyy'.
    The week starts on Sunday and ends on Saturday.
    """
    today = datetime.date.today()
    current_weekday = today.isoweekday()

    # Calculate the start date (Sunday)
    start_date = today - datetime.timedelta(days=current_weekday % 7)

    # Calculate the end date (Saturday)
    end_date = start_date + datetime.timedelta(days=6)

    start_date_str = start_date.strftime("%b %d")
    end_date_str = end_date.strftime("%b %d")

    # Add proper day suffix
    start_date_str += get_day_suffix(int(start_date.strftime("%d")))
    end_date_str += get_day_suffix(int(end_date.strftime("%d")))

    # Add year to the date strings
    start_date_str += f" {start_date.year}"
    end_date_str += f" {end_date.year}"

    date_range = f"{start_date_str} - {end_date_str}"
    return date_range

def get_day_suffix(day):
    """
    Returns the proper day suffix (st, nd, rd, th) for the given day.
    """
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd"][day % 10 - 1]
    return suffix

def append_pop_configure_punches(punches, day_as_number, start_end_str):
    # Append start punch
    start_str = start_end_str + str(datetime.datetime.now().strftime("%I:%M:%S %p"))
    punches.append(start_str)
    
    # Pop None punch if it exists
    if (punches[0] == "None"):
        punches.pop(0)
    
    # Display on UI
    punch_option_menus = app.weekly_daily_tabs.weekly_tab.programming_frame.daily_punches_option_menus
    punch_option_menus[day_as_number].configure(values=punches)

def append_and_save_start_end_punch(start_end_str):
    # Use local day_as_number in case of day change while program running
    day_as_number = (datetime.datetime.now().weekday() + 1) % 7

    # Call function with different parameters based on day
    if (day_as_number == 0):
        append_pop_configure_punches(sunday_punches, day_as_number, start_end_str)
    elif (day_as_number == 1):
        append_pop_configure_punches(monday_punches, day_as_number, start_end_str)
    elif (day_as_number == 2):
        append_pop_configure_punches(tuesday_punches, day_as_number, start_end_str)
    elif (day_as_number == 3):
        append_pop_configure_punches(wednesday_punches, day_as_number, start_end_str)
    elif (day_as_number == 4):
        append_pop_configure_punches(thursday_punches, day_as_number, start_end_str)
    elif (day_as_number == 5):
        append_pop_configure_punches(friday_punches, day_as_number, start_end_str)
    else:
        append_pop_configure_punches(saturday_punches, day_as_number, start_end_str)

    update_global_daily_lists()

    # Save punch data to file
    data = {
        "sunday_punches": sunday_punches,
        "monday_punches": monday_punches,
        "tuesday_punches": tuesday_punches,
        "wednesday_punches": wednesday_punches,
        "thursday_punches": thursday_punches,
        "friday_punches": friday_punches,
        "saturday_punches": saturday_punches
    }

    threading.Thread(target=write_punches_to_file, args=(data,)).start()

def start_end():
    global current_week
    global readytostart
    global curr_week_str
    global can_clear
    global start_time
    global tracking
    global timer_id
    global paused
    global p_focus_time
    global p_break_time
    global p_long_break_time
    global p_cycle_count
    global daily_weights

    # Check if data exists in the previous week. If so then don't allow user to clock in and display message/notification
    if (current_week != datetime.datetime.now().strftime("%U %Y") and current_week != -1):
        app.weekly_daily_tabs.daily_tab.start_end_button.configure(state="disabled")
        # Create a notification
        notification.notify(
            title="You've been clocked out!",
            message="You've been clocked out due to being clocked in during a new week without clearing first.",
            app_name="Productivity Tracker",
            app_icon="icon4.ico",
            timeout=10  
        )
        app.attributes("-topmost", True)
        app.attributes("-topmost", False)
        new_week_modal()
    else:
        can_clear = False
        app.buttons_frame.send_weekly_data_button.configure(state="disabled")
        app.buttons_frame.clear_weekly_data_button.configure(state="disabled")
        app.weekly_daily_tabs.weekly_tab.programming_frame.description_textbox.configure(state="disabled")

        for i in range(7):
            entry = app.weekly_daily_tabs.weekly_tab.exercise_frame.daily_weight_entries[i]
            daily_weight = daily_weights[i]
            
            # Clear all weight entries that only have 0 in them
            if (entry.get() != ""):
                if (float(entry.get()) == 0):
                    entry.delete(0, "end")

            # If weight entered ends with ".", insert float from daily_weight
            if (entry.get().endswith(".")):
                entry.delete(0, "end")
                entry.insert(0, str(daily_weight))

            # Formatting for when clocked in
            entry.configure(placeholder_text="NONE")
            entry.configure(state="disabled")

        if (readytostart):
            # Clock In
            readytostart = False
            start_time = time.time()
            tracking = True
            app.weekly_daily_tabs.daily_tab.start_end_button.configure(text="End")
            app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(state="normal")
            
            append_and_save_start_end_punch("Start: ")

            # Save current week to curr_week_str if one isn't already set
            if (curr_week_str == ""):
                curr_week_str = get_date_range_for_current_week()
                data = {
                    "curr_week_str": curr_week_str
                }
                threading.Thread(target=write_current_week_to_file, args=(data,)).start()

            # Do the same as above but for must clear file
            if (current_week == -1):
                current_week = datetime.datetime.now().strftime("%U %Y")
                data = {
                    "must_clear": must_clear,
                    "current_week": current_week
                }
                threading.Thread(target=write_must_clear_to_file, args=(data,)).start()
            
            # Flush out timer if one is set and start clock
            if (timer_id != ""):
                app.after_cancel(timer_id)

            # Begin Timer
            update_time(True)
        else:
            # Clock Out
            can_clear = True
            
            app.buttons_frame.send_weekly_data_button.configure(state="normal")
            app.buttons_frame.clear_weekly_data_button.configure(state="normal")
            app.weekly_daily_tabs.weekly_tab.programming_frame.description_textbox.configure(state="normal")
            
            # Use local day_as_number in case of day change while program running
            day_as_number = (datetime.datetime.now().weekday() + 1) % 7
            daily_weight_entries = app.weekly_daily_tabs.weekly_tab.exercise_frame.daily_weight_entries
            # Flip and format weight entries depending on day
            for i in range(7):
                if (i == day_as_number):
                    daily_weight_entries[i].configure(state="normal")
                    daily_weight_entries[i].configure(placeholder_text="Enter Weight")
                else:
                    daily_weight_entries[i].configure(placeholder_text="NONE")
                    daily_weight_entries[i].configure(state="disabled")

            # Reset Buttons and Time Labels
            app.weekly_daily_tabs.daily_tab.start_end_button.configure(text="Start")
            app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(state="disabled")
            app.weekly_daily_tabs.daily_tab.total_time_label.configure(text="00:00:00")
            app.weekly_daily_tabs.daily_tab.pomodoro_time_label.configure(text="00:25:00")
            app.weekly_daily_tabs.daily_tab.pause_resume_button.configure(text="Pause")
            app.weekly_daily_tabs.daily_tab.pomodoro_count_label.configure(text="#1")
            app.weekly_daily_tabs.daily_tab.pomodoro_focus_label.configure(text="Focus")

            # Reset Vars
            readytostart = True
            paused = False
            p_focus_time = focus_time
            p_break_time = break_time
            p_long_break_time = long_break_time
            p_cycle_count = 1

            append_and_save_start_end_punch("End: ")

            # Flush out timer
            app.after_cancel(timer_id)

def get_operating_system():
    global operating_system
    # Determine operating system being used
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

def write_current_vars_to_walking_json():
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

class ProgrammingFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        global daily_programming_times
        global daily_punches

        # Title Label
        self.title = CTk.CTkLabel(self, text="Programming", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=4, sticky="ew")
        
        # Category Labels
        category_labels = ["Time Programming", "Time Punches", "Description of Weekly Work Completed"]
        for i in range(3):
            label = CTk.CTkLabel(self, text=category_labels[i])
            label.grid(row=1, column=(i + 1))
        
        # Weekday Labels
        left_right_padding = 0
        if (operating_system == "Linux"):
            left_right_padding = 10
        else:
            left_right_padding = 12

        days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i in range(7):
            label = CTk.CTkLabel(self, text=days_of_the_week[i])
            label.grid(row=(i + 2), column=0, padx=(left_right_padding, 5), sticky="w")
        
        # Weekday Hour Entries
        self.programming_time_entries = []
        for i in range(7):
            entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
            entry.configure(state="disabled")
            entry.grid(row=(i + 2), column=1, padx=(5, 5))

            if (daily_programming_times[i] != 0):
                hours = daily_programming_times[i] // 3600
                minutes = (daily_programming_times[i] % 3600) // 60
                seconds = daily_programming_times[i] % 60
                programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                entry.configure(state="normal")
                entry.insert(0, programming_time_string)
                entry.configure(state="disabled")

            self.programming_time_entries.append(entry)
        
        # Weekday Punches Option Menus
        self.daily_punches_option_menus = []
        for i in range(7):
            option_menu = CTk.CTkOptionMenu(self, values=daily_punches[i])
            option_menu.set("Punches")
            option_menu.grid(row=(i + 2), column=2, padx=(5, 5), pady=(5,5))
            # Taking out selected_option causes this to break. It may be a bug with customtkinter
            option_menu.configure(command=lambda selected_option="Punches", option_menu=option_menu: self.reset_option_menu(option_menu, selected_option))
            self.daily_punches_option_menus.append(option_menu)

        # Description Text Box
        self.description_textbox = CTk.CTkTextbox(self, width=440, height=258, wrap="word")
        self.description_textbox.grid(row=2, column=3, rowspan=7, padx=(5, left_right_padding))
        # Calls function to save description to json on each key press.
        self.description_textbox.bind("<KeyRelease>", self.save_description)

        # If description hasn't been edited, display instructions, else display edited text.
        placeholder_string = "INSTRUCTIONS:\n\n- Edit the .env file in the dist folder to include any discord webhooks that you want to send data to.\n\n- Use the Start Button in the Daily Tracker Tab to clock in.\n\n- Once you clock in, you'll have the option to pause or resume your session.\n\n- End your session by clicking the End Button\n\n- When you aren't in a session, you'll have the ability to Send Weekly Data and Clear Weekly Data.\n\n- Sending weekly data sends your data to the discord by using webhooks. Your data will be automatically formatted to be readable and will show what dates the week covered.\n\n- Clearing Weekly Data will erase everything and set it all back to default. This will mostly be used when you want to start a new week. Be sure to send your data before doing this.\n\n- The Walking and Pomodoro switches are options that you can add to your session.\n\n- Walking assumes you are walking on a treadmill at 2mph and tracks your distance, steps, and calories burned. Calories burned are determined by the weight that you enter in the Weekly Log Exercising Tab. \n\n- Pomodoro pauses and gives a notification everytime the timer runs out. The timers go as follows: 25, 5, 25, 5, 25, 5, 25, 15\n\n- You'll only be able to type in this text box when you're not in a session. Erasing these instructions and typing a new message will save your new message."        
        if (description != ""):
            self.description_textbox.insert(1.0, description)
        else:
            self.description_textbox.insert(0.0, placeholder_string)

    # Sets Option Menus back to "Punches" after they've been changed. Taking out selected option causes this to break. It may be a bug with customtkinter.
    def reset_option_menu(self, option_menu, selected_option):
        option_menu.set("Punches")

    def save_description(self, event):
        global description
        data = {
            "description": app.weekly_daily_tabs.weekly_tab.programming_frame.description_textbox.get("1.0", "end-1c")
            }
        write_description_to_file(data)
        description = data["description"]

class ExerciseFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        global daily_weights
        global daily_walking_times
        global daily_distances
        global daily_steps
        global daily_calories

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
        for i in range(5):
            label = CTk.CTkLabel(self, text=category_labels[i])
            label.grid(row=1, column=(i + 1))
        
        # Weekday Labels
        days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i in range(7):
            label = CTk.CTkLabel(self, text=days_of_the_week[i])
            label.grid(row=(i + 2), column=0, padx=(left_right_padding, 5), sticky="w")
        
        # Weight Entries
        self.daily_weight_entries = []
        for i in range(7):
            entry = CTk.CTkEntry(self, placeholder_text="Enter Weight", justify="center")
            entry.grid(row=(i + 2), column=1, padx=(5, 5), pady=(5,5))
            entry.bind("<KeyRelease>", self.validate_float)

            if (daily_weights[i] != 0):
                weight_string = str(daily_weights[i])
                entry.insert(0, weight_string)

            day_as_number = (datetime.datetime.now().weekday() + 1) % 7
            if (i != day_as_number):
                entry.configure(placeholder_text="NONE")
                entry.configure(state="disabled")

            self.daily_weight_entries.append(entry)

        # Time Walked Entries
        self.daily_walking_entries = []
        for i in range(7):
            entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
            entry.configure(state="disabled")
            entry.grid(row=(i + 2), column=2, padx=(5, 5))

            if (daily_walking_times[i] != 0):
                hours = daily_walking_times[i] // 3600
                minutes = (daily_walking_times[i] % 3600) // 60
                seconds = daily_walking_times[i] % 60
                walking_time_string = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
                entry.configure(state="normal")
                entry.insert(0, walking_time_string)
                entry.configure(state="disabled")

            self.daily_walking_entries.append(entry)

        # Distance, Steps, and Calories Entries
        self.daily_distance_entries = []
        self.daily_steps_entries = []
        self.daily_calories_entries = []
        for i in range(3):
            for j in range(7):
                entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
                entry.configure(state="disabled")
                
                right_padding = 0
                if (i != 2):
                    right_padding = 5
                else:
                    right_padding = left_right_padding

                entry.grid(row=(j + 2), column=(i + 3), padx=(5, right_padding))

                if (i == 0):
                    if (daily_distances[j] != 0):
                        walking_distance_string = str(daily_distances[j])
                        entry.configure(state="normal")
                        entry.insert(0, walking_distance_string)
                        entry.configure(state="disabled")

                    self.daily_distance_entries.append(entry)
                
                elif (i == 1):
                    if (daily_steps[j] != 0):
                        steps_string = str(daily_steps[j])
                        entry.configure(state="normal")
                        entry.insert(0, steps_string)
                        entry.configure(state="disabled")

                    self.daily_steps_entries.append(entry)

                else:
                    if (daily_calories[j] != 0):
                        calories_string = str(daily_calories[j])
                        entry.configure(state="normal")
                        entry.insert(0, calories_string)
                        entry.configure(state="disabled")

                    self.daily_calories_entries.append(entry)
    
        self.weight_as_float = 0

    def validate_float(self, event):
        weight_entry = event.widget
        try:
            # if entry empty, insert "0"
            if (weight_entry.get() == ""):
                weight_entry.delete(0, "end")
                weight_entry.insert(0, "0")

            # Delete first character (ex. 03.0 -> 3.0)
            if (weight_entry.get().startswith("0") and not weight_entry.get().endswith(".")):
                weight_entry.delete(0)

            # Attempt to cast weight_entry to float then save
            self.weight_as_float = float(weight_entry.get())
            self.assign_weight_to_correct_day(weight_entry)
            update_global_daily_lists()
            self.calc_weight_loss()
            write_current_vars_to_walking_json()

        except ValueError:
            # In the case of float conversion failing
            weight_entry = event.widget
            # Insert 0 and save if entry is empty ("")
            if (weight_entry.get() == ""):
                weight_entry.delete(0, "end")
                weight_entry.insert(0, "0")
                self.weight_as_float = float(weight_entry.get())
                self.assign_weight_to_correct_day(weight_entry)
                update_global_daily_lists()
                self.calc_weight_loss()
                write_current_vars_to_walking_json()
            else:
                # Revert to previous weight_as_float if character entered could not be casted as float
                weight_entry.delete(0, "end")
                weight_entry.insert(0, str(self.weight_as_float))

    def assign_weight_to_correct_day(self, widget):
        global sunday_weight
        global monday_weight
        global tuesday_weight
        global wednesday_weight
        global thursday_weight
        global friday_weight
        global saturday_weight

        # Assign weight to correct global var
        widget_name = str(widget).split(".")[6]
        if ("2" in widget_name):
            monday_weight = self.weight_as_float
        elif ("3" in widget_name):
            tuesday_weight = self.weight_as_float
        elif ("4" in widget_name):
            wednesday_weight = self.weight_as_float
        elif ("5" in widget_name):
            thursday_weight = self.weight_as_float
        elif ("6" in widget_name):
            friday_weight = self.weight_as_float
        elif ("7" in widget_name):
            saturday_weight = self.weight_as_float
        else:
            # 1st entry doesn't have unique identifier
            sunday_weight = self.weight_as_float

    def calc_weight_loss(self):
        global daily_weights
        global total_weight_lost
        
        first_weight = 0
        last_weight = 0
        weigh_in_count = 0
        
        # Assign first weight to first non-empty weight entry
        for i in range(7):
            # Get first weight
            if (first_weight == 0 and self.daily_weight_entries[i].get() != ""):
                first_weight = daily_weights[i]
            # Get last weight
            if (self.daily_weight_entries[i].get() != ""):
                last_weight = daily_weights[i]
                weigh_in_count = weigh_in_count + 1
        weight_lost_str = ""
        #Check to make sure both vars are not equal
        if (first_weight != last_weight):
            weight_lost = first_weight - last_weight
            weight_lost = round(weight_lost, 2)        
            
            # Choose whether to display positive or negative value depending on subtraction
            if (weight_lost > 0):
                weight_lost_str = "-" + str(weight_lost)
            elif (weight_lost < 0):
                weight_lost_str = "+" + str(abs(weight_lost))
            
            app.totals_frame.total_weight_lost_entry.configure(state="normal")
            app.totals_frame.total_weight_lost_entry.delete(0, "end")
            app.totals_frame.total_weight_lost_entry.insert(0, weight_lost_str)
            app.totals_frame.total_weight_lost_entry.configure(state="disabled")
            
        # Check to make sure both vars set, if so then insert "0"
        elif ((first_weight != 0 or last_weight != 0) and weigh_in_count > 1):
            app.totals_frame.total_weight_lost_entry.configure(state="normal")
            app.totals_frame.total_weight_lost_entry.delete(0, "end")
            app.totals_frame.total_weight_lost_entry.insert(0, "0")
            app.totals_frame.total_weight_lost_entry.configure(state="disabled")

        # Set total_weight_lost
        total_weight_lost = weight_lost_str

class DailyFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        timer_font_size = 0
        walking_switch_padding = 0
        bottom_padding = 0
        
        if (operating_system == "Linux"):
            timer_font_size = 58
            walking_switch_padding = 42
            bottom_padding = 64
        else:
            timer_font_size = 75
            walking_switch_padding = 55
            bottom_padding = 47

        # Title Label
        self.title = CTk.CTkLabel(self, text="Time Trackers", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=4, sticky="ew")

        # Header Labels
        self.session_time_worked_today_header_label = CTk.CTkLabel(self, text="Session Time Worked")
        self.session_time_worked_today_header_label.grid(row=1, column=0, padx=(50,0), pady=(55,0))

        self.pomodoro_header_label = CTk.CTkLabel(self, text="Pomodoro Timer")
        self.pomodoro_header_label.grid(row=1, column=2, padx=(0,50), pady=(55,0))

        # Labels for tracking total daily and pomodoro time
        self.total_time_label = CTk.CTkLabel(self, text="00:00:00", font=("", timer_font_size, "bold"))
        self.total_time_label.grid(row=2, column=0, padx=(51,0))

        self.pomodoro_time_label = CTk.CTkLabel(self, text="00:25:00", font=("", timer_font_size, "bold"))
        self.pomodoro_time_label.grid(row=2, column=2, padx=(0,51))

        # Labels for tracking pomodoro status
        self.pomodoro_focus_label = CTk.CTkLabel(self, text="Focus")
        self.pomodoro_focus_label.grid(row=3, column=2, padx=(0,50))

        self.pomodoro_count_label = CTk.CTkLabel(self, text="#1")
        self.pomodoro_count_label.grid(row=4, column=2, padx=(0,50), pady=(0, 55))

        # Options for walking and pomodoro
        self.walking_switch = CTk.CTkSwitch(self, text="Walking")
        self.walking_switch.grid(row=3, column=0, padx=(walking_switch_padding, 0))

        self.pomodoro_switch = CTk.CTkSwitch(self, text="Pomodoro")
        self.pomodoro_switch.grid(row=4, column=0, padx=(50,0), pady=(0, 55))

        # Buttons for start/end and resume/pause
        self.start_end_button = CTk.CTkButton(self, text="Start", command=start_end)
        self.start_end_button.grid(row=3, column=1, pady=(10, 0))

        if (must_clear):
            self.start_end_button.configure(state="disabled")

        self.pause_resume_button = CTk.CTkButton(self, text="Pause", state="disabled", command=pause_resume)
        self.pause_resume_button.grid(row=4, column=1, pady=(10,bottom_padding))

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

        self.daily_tab = DailyFrame(self.tab("Daily Tracker"))
        self.daily_tab.grid(row=0, column=0, pady=(53,5))

class TotalsFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        global total_programming_time
        global total_weight_lost
        global total_walking_time
        global total_walking_distance
        global total_walking_steps
        global total_calories
        
        # Title Label
        self.title = CTk.CTkLabel(self, text="Total Weekly Statistics", fg_color="gray30")
        self.title.grid(row=0, column=0, columnspan=6, sticky="ew")
        
        # Category Labels
        self.time_programming_label = CTk.CTkLabel(self, text="Time Programming")
        self.time_programming_label.grid(row=1, column=1, padx=(108, 50))

        self.weight_lost_label = CTk.CTkLabel(self, text="Weight Lost")
        self.weight_lost_label.grid(row=1, column=2, padx=(50, 50))
        
        self.time_walked_label = CTk.CTkLabel(self, text="Time Walked")
        self.time_walked_label.grid(row=1, column=3, padx=(50, 108))

        self.distance_label = CTk.CTkLabel(self, text="Distance")
        self.distance_label.grid(row=3, column=1, padx=(108, 50))

        self.steps_label = CTk.CTkLabel(self, text="Steps")
        self.steps_label.grid(row=3, column=2, padx=(50, 50))

        self.calories_burned_label = CTk.CTkLabel(self, text="Calories Burned")
        self.calories_burned_label.grid(row=3, column=3, padx=(50, 108))
        
        # Total Time Programming Entry
        self.time_programming_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.time_programming_entry.configure(state="disabled")
        self.time_programming_entry.grid(row=2, column=1, padx=(110, 50), pady=(5,5))

        if (total_programming_time != 0):
            hours = total_programming_time // 3600
            minutes = (total_programming_time % 3600) // 60
            seconds = total_programming_time % 60
            programming_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_programming_entry.configure(state="normal")
            self.time_programming_entry.insert(0, programming_time_string)
            self.time_programming_entry.configure(state="disabled")

        # Total Weight Lost
        self.total_weight_lost_entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
        self.total_weight_lost_entry.configure(state="disabled")
        self.total_weight_lost_entry.grid(row=2, column=2, padx=(50, 50), pady=(5,5))

        if (total_weight_lost != ""):
            weight_lost_string = str(total_weight_lost)
            self.total_weight_lost_entry.configure(state="normal")
            self.total_weight_lost_entry.insert(0, weight_lost_string)
            self.total_weight_lost_entry.configure(state="disabled")

        # Total Time Walked Entry
        self.time_walked_entry = CTk.CTkEntry(self, placeholder_text="00:00:00", justify="center")
        self.time_walked_entry.configure(state="disabled")
        self.time_walked_entry.grid(row=2, column=3, padx=(50, 110), pady=(5,5))

        if (total_walking_time != 0):
            hours = total_walking_time // 3600
            minutes = (total_walking_time % 3600) // 60
            seconds = total_walking_time % 60
            walking_time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_walked_entry.configure(state="normal")
            self.time_walked_entry.insert(0, walking_time_string)
            self.time_walked_entry.configure(state="disabled")

        # Total Walking Stats Entries
        total_walking_stats = [total_walking_distance, total_walking_steps, total_calories]
        self.walking_stats_entries = []
        for i in range(3):
            pad_left = 50
            pad_right = 50
            if (i == 0):
                pad_left = 108
            elif (i == 2):
                pad_right = 108

            entry = CTk.CTkEntry(self, placeholder_text="0", justify="center")
            entry.configure(state="disabled")
            entry.grid(row=4, column=(i + 1), padx=(pad_left, pad_right), pady=(5,5))

            if (total_walking_stats[i] != 0):
                walking_stat_string = str(total_walking_stats[i])
                entry.configure(state="normal")
                entry.insert(0, walking_stat_string)
                entry.configure(state="disabled")

            self.walking_stats_entries.append(entry)

class ButtonsFrame(CTk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        # Add Send Weekly Data Button
        self.send_weekly_data_button = CTk.CTkButton(self, text="Send Weekly Data", command=send_data_modal)
        self.send_weekly_data_button.grid(row=0, column=0, padx=(0,30), pady=(10,0))

        # Add Clear Weekly Data Button
        self.clear_weekly_data_button = CTk.CTkButton(self, text="Clear Weekly Data", command=clear_data_modal)
        self.clear_weekly_data_button.grid(row=0, column=1, padx=(30,0), pady=(10,0))

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
        self.totals_frame = TotalsFrame(self)
        self.totals_frame.grid(row=1, column=0, padx=10)

        # #Add Buttons
        self.buttons_frame = ButtonsFrame(self)
        self.buttons_frame.grid(row=2, column=0)

#Run app in dark mode
get_operating_system()
CTk.set_appearance_mode("dark")
color = ""
if (operating_system == "Linux"):
    color = "green"
else:
    color = "dark-blue"
CTk.set_default_color_theme(color)
app = App()
app.mainloop()