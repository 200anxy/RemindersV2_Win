import tkinter as tk
from tkinter import *
import time
from plyer import notification
title1 = "Hello"
message1 = "hello"
# def destroyLabel(time,LabelVariable):
#     LabelVariable.after(time,LabelVariable.destroy())

#function to get text from remindTimevar
def getAllvalues():
    timeNeeded = float(remindTimevar.get())
    titleOfnotification = titleNeededvar.get()
    contentNotification = contentNeededvar.get()
    # notification.notify(
    #     title = "Notification Placement Succesful",
    #     message = "Your notification has been succesfully placed! Please keep the window in which you entered the details open!",
    #     app_icon = "C:\\Users\\Aadarsh Nair\\Downloads\\alarm (2).ico",
    #     timeout = 10



    # )
    notification.notify(
    title = "Notification Placement Successfull! 😁",

    message = "Notification Placement is succesful. Please keep the tab in which you entered the details open!",

    app_icon = r"C:\Users\Aadarsh Nair\Downloads\sucess_icon.ico",

    timeout = 2,

    )
    time.sleep(timeNeeded*60)
    notification.notify(
        title= titleOfnotification,
        message = contentNotification,
        app_icon = "C:\\Users\\Aadarsh Nair\\Downloads\\alarm (2).ico",
        timeout = 10
        
    )









        
        
    
    
        
   




root = tk.Tk()

root.title("Reminders")
root.geometry('300x500+50+50')

remindTimevar = StringVar()
titleNeededvar = StringVar()
contentNeededvar = StringVar()


#Display Info
message = tk.Label(root, text = "Welcome to the Reminders app!")
#Input in how much time it should remind
messageRemind = tk.Label(root, text = "Time in which to remind",padx=10,pady=10)
remindTime = tk.Entry(root,textvariable=remindTimevar)
x = remindTimevar.get()
#Input in what the title should be
messageTitle = tk.Label(root, text = "What should the title of the reminder be?")
title = tk.Entry(root,textvariable=titleNeededvar)
#Input what the content should be
messageContent = tk.Label(root, text = "What should be the message inside the notification?")
content = tk.Entry(root,textvariable=contentNeededvar)



acceptButton = tk.Button(root,text='Submit',command=getAllvalues)









message.pack()
messageRemind.pack()
remindTime.pack()

messageTitle.pack()
title.pack()
messageContent.pack()
content.pack()
acceptButton.pack()






root.mainloop()