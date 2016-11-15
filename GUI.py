import Tkinter
import tkMessageBox

time = 0
checkin = 0
checkout = 0
FMT = '%H:%M:%S'

from datetime import datetime


top = Tkinter.Tk()

def check_in():
    checkin = datetime.now().strftime(" %H:%M:%S")
    tkMessageBox.showinfo("Success", "You've clocked in!" + str(checkin))
    return checkin

def check_out():
    checkout = datetime.now().strftime(" %H:%M:%S")
    tkMessageBox.showinfo("Success", "You've clocked out!" + str(checkout))
    return checkout
    
def total_time():
    tot = checkout - checkin
    tkMessageBox.showinfo("INFO", "Here's your total time worked: %" % (datetime.total_seconds(tot)))
    
b = Tkinter.Button (top, text = "Clock In", command = check_in)
c = Tkinter.Button (top, text = "Clock out", command = check_out)
d = Tkinter.Button (top, text = "Total Time", command = total_time)

b.pack()
c.pack()
d.pack()
top.mainloop()