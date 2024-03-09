import tkinter as tk
from tkinter import *
import time
from plyer import notification
import threading
def run_tkinter():
    root = tk.Tk()
    root.title("Reminders")
    root.geometry('400x500+50+50')

    # Styling
    root.configure(bg='#F0F0F0')
    root.option_add('*Font', 'Arial 10')

    # Labels
    message = tk.Label(root, text="Welcome to the Reminders app!", font=('Arial', 12, 'bold'), pady=10)
    messageRemind = tk.Label(root, text="Time in which to remind", font=('Arial', 10), pady=5)
    messageTitle = tk.Label(root, text="What should the title of the reminder be?", font=('Arial', 10), pady=5)
    messageContent = tk.Label(root, text="What should be the message inside the notification?", font=('Arial', 10), pady=5)

    # Entries
    global remindTimevar
    global titleNeededvar
    global contentNeededvar
    remindTimevar = StringVar()
    titleNeededvar = StringVar()
    contentNeededvar = StringVar()
 
    remindTime = tk.Entry(root,textvariable=remindTimevar, width=20, font=('Arial', 10))
    title = tk.Entry(root, textvariable=titleNeededvar, width=30, font=('Arial', 10))
    content = tk.Entry(root, textvariable=contentNeededvar, width=30, font=('Arial', 10))

    # Button
    acceptButton = tk.Button(root, text='Submit', command=getAllvalues, width=10, font=('Arial', 10), bg='#4CAF50', fg='white')

    # Packing elements
    message.pack()
    messageRemind.pack()
    remindTime.pack()
    messageTitle.pack()
    title.pack()
    messageContent.pack()
    content.pack()
    acceptButton.pack(pady=10)

    # Customizing the window
    root.iconbitmap(r".\assets\appIcon.ico")
    root.resizable(False, False)

    # Running the application
    root.mainloop()

def getAllvalues():
    try:
         float(remindTimevar.get())
    except ValueError:
        notification.notify(
            title="Invalid Time!",
            message="Please enter a valid time in minutes.",
            app_icon=r".\assets\error.ico",
            timeout=5
        )
        return
    timeNeeded = float(remindTimevar.get())
    titleOfnotification = titleNeededvar.get()
    contentNotification = contentNeededvar.get()
    
    notification.notify(
        title="Notification Placement Successful! 😁",
        message="Notification Placement is successful. You may close the window if you wish",
        app_icon=r".\assets\appIcon.ico",
        timeout=2
    )
    
    time.sleep(timeNeeded * 60)
    
    notification.notify(
        title=titleOfnotification,
        message=contentNotification,
        app_icon=r".\assets\appicon2.ico",
        timeout=10
    )

threading.Thread(target=run_tkinter).start()
    