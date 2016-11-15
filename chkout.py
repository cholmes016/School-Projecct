#This application will be used to keep track of teacher's time card
time = 0
checkin = 0
checkout = 0

from datetime import datetime

def clockin():
    checkin = raw_input("What time did you arrive?: ")
    checkout = raw_input("What time are you leaving?: ")
    checkin = datetime.strptime(checkin, "%I:%M")
    checkout = datetime.strptime(checkout, "%I:%M")
    print checkin
    return True
    
clockin()