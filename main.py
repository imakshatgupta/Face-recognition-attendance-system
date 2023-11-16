import tkinter as tk
from tkinter import messagebox as mess
import os
import csv

def change_password():
    # Placeholder functionality for changing password
    mess.showinfo('Change Password', 'Placeholder: Functionality for changing password')

def contact_us():
    # Placeholder functionality for contacting support
    mess.showinfo('Contact Us', 'Placeholder: Contact support at contact@example.com')

def take_images():
    roll_number = txt.get()
    full_name = txt2.get()

    if roll_number and full_name:
        # Placeholder functionality for taking images
        mess.showinfo('Take Images', f"Images captured for {full_name}, Roll No: {roll_number}")
    else:
        mess.showerror('Error', 'Please enter Roll No and Full Name')

def save_profile():
    roll_number = txt.get()
    full_name = txt2.get()

    if roll_number and full_name:
        # Placeholder functionality for saving profiles
        mess.showinfo('Save Profile', f"Profile saved for {full_name}, Roll No: {roll_number}")
    else:
        mess.showerror('Error', 'Please enter Roll No and Full Name')

def take_attendance():
    # Placeholder functionality for taking attendance
    mess.showinfo('Take Attendance', 'Attendance taken')

def clear_entry(entry):
    entry.delete(0, tk.END)

def clear_roll_number():
    clear_entry(txt)

def clear_full_name():
    clear_entry(txt2)

def quit_app():
    window.destroy()

# Create a window
window = tk.Tk()
window.geometry("800x600")
window.title("Attendance System")

# Header Label
header_label = tk.Label(window, text="Face Recognition Based Attendance System", font=('Arial', 20), pady=20)
header_label.pack()

# Frame for Registration Section
registration_frame = tk.Frame(window)
registration_frame.pack(pady=20)

# Labels and Entry for Registration Section
roll_label = tk.Label(registration_frame, text="Enter Roll No.", font=('Arial', 14))
roll_label.grid(row=0, column=0, padx=10, pady=10)

txt = tk.Entry(registration_frame, font=('Arial', 14))
txt.grid(row=0, column=1, padx=10, pady=10)

name_label = tk.Label(registration_frame, text="Enter Full Name", font=('Arial', 14))
name_label.grid(row=1, column=0, padx=10, pady=10)

txt2 = tk.Entry(registration_frame, font=('Arial', 14))
txt2.grid(row=1, column=1, padx=10, pady=10)

# Buttons for Registration Section
clear_roll_button = tk.Button(registration_frame, text="Clear Roll No.", command=clear_roll_number)
clear_roll_button.grid(row=0, column=2, padx=10, pady=10)

clear_name_button = tk.Button(registration_frame, text="Clear Name", command=clear_full_name)
clear_name_button.grid(row=1, column=2, padx=10, pady=10)

take_images_button = tk.Button(registration_frame, text="Take Images", command=take_images)
take_images_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

save_profile_button = tk.Button(registration_frame, text="Save Profile", command=save_profile)
save_profile_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Frame for Attendance Section
attendance_frame = tk.Frame(window)
attendance_frame.pack(pady=20)

# Attendance Button
take_attendance_button = tk.Button(attendance_frame, text="Take Attendance", command=take_attendance)
take_attendance_button.pack(pady=10)

# Quit Button
quit_button = tk.Button(window, text="Quit", command=quit_app)
quit_button.pack(pady=20)

window.mainloop()
