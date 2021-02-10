import tkinter as tk
from tkinter import *

#Blank sample button for other menu bar options
def donothing():
    hide_all_frames()
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


###################################################################
#   Menu bar functions
def new_schedule():
    filewin = Toplevel(root)
    button = Button(filewin, text="You clicked new schedule")
    button.place(relx=0, rely=0)

def open_schedule():
    filewin = Toplevel(root)
    button = Button(filewin, text="You clicked open schedule")
    button.place(relx=0, rely=0)

def save_schedule():
    filewin = Toplevel(root)
    button = Button(filewin, text="You clicked save schedule")
    button.place(relx=0, rely=0)

def delete_schedule():
    filewin = Toplevel(root)
    button = Button(filewin, text="You clicked delete schedule")
    button.place(relx=0, rely=0)

def export_schedule():
    filewin = Toplevel(root)
    button = Button(filewin, text="You clicked export schedule")
    button.place(relx=0, rely=0)

def recent_schedule():
    filewin = Toplevel(root)
    button = Button(filewin, text="You clicked recent schedule")
    button.place(relx=0, rely=0)

def print_schedule():
    filewin = Toplevel(root)
    button = Button(filewin, text="You clicked print schedule")
    button.place(relx=0, rely=0)

################################################################

################################################################

# Hides all frames on the screen

def hide_all_frames():
    recent_sched_frame.place_forget()
    select_sched_frame.place_forget()
    student_info_frame.place_forget()
    background_label.place_forget()


##########################################################
# Initialize GUI
root = tk.Tk()

canvas = tk.Canvas(root, height=650, width=1300)
canvas.pack()

#Set background image
bground_image = tk.PhotoImage(file='supic.png')
background_label = tk.Label(root, image=bground_image)
background_label.place(relx=0.15, rely=0.05, relwidth=1, relheight=1)

##########################################################

##########################################################
# Create frames for different main screen aspects
recent_sched_frame = Frame(root, width=400, height=400, bg='black')
recent_sched_frame.place(relx=0.011, rely=0.372)
recent_label = Label(recent_sched_frame, text="Selected Courses", bg='black', fg='white').place(relx=0.4, rely=0.5)

select_sched_frame = Frame(root, width=400, height=225, bg='gray')
select_sched_frame.place(relx=0.011, rely=0.01)
selecte_label = Label(select_sched_frame, text="Recent Schedule", bg='gray', fg='white').place(relx=0.4, rely=0.5)

student_info_frame = Frame(root, width=850, height=50, bg='cyan')
student_info_frame.place(relx=0.325, rely=0.02)
student_label = Label(student_info_frame, text="Student Info", bg='cyan', fg='black').place(relx=0.45, rely=0.3)

##############################################################

##############################################################
# Create different menu bar options for new schedule menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Schedule", command=new_schedule)
filemenu.add_command(label="Open Schedule", command=open_schedule)
filemenu.add_command(label="Save Schedule", command=save_schedule)
filemenu.add_command(label="Delete Schedule", command=delete_schedule)
filemenu.add_command(label="Export Schedule", command=export_schedule)
filemenu.add_command(label="Recent Schedules", command=recent_schedule)
filemenu.add_command(label="Print Schedule", command=print_schedule)

filemenu.add_separator()

filemenu.add_command(label="Clear Screen", command=hide_all_frames)
filemenu.add_command(label="Exit", command=root.quit)

##################################################################

##################################################################
# Create menu bar options for Major menu
menubar.add_cascade(label="Schedule", menu=filemenu)
schedmenu = Menu(menubar, tearoff=0)

schedmenu.add_command(label="Accounting", command=donothing)
schedmenu.add_command(label="Art", command=donothing)
schedmenu.add_command(label="Biology", command=donothing)
schedmenu.add_command(label="Chemistry", command=donothing)
schedmenu.add_command(label="Communication", command=donothing)
schedmenu.add_command(label="Computer Science", command=donothing)

######################################################

######################################################
# Create menu bar options for help menu
menubar.add_cascade(label="Major", menu=schedmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Menu", command=donothing)
helpmenu.add_command(label="About", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

#######################################################

root.config(menu=menubar)

root.mainloop()